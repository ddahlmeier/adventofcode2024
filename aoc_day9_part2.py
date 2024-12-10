from itertools import zip_longest
import sys

def read_disk(input):
    # files are on even positions
    file_blocks = [int(input[i]) for i in range(0, len(input), 2)]
    # free space on odd positions
    free_blocks = [int(input[i]) for i in range(1, len(input), 2)]
    filemap = {}
    free_space = []
    start_idx = 0
    for id_num, (file_block_len, free_block_len) in enumerate(zip_longest(file_blocks, free_blocks, fillvalue=0)):
        filemap[id_num] = (start_idx, file_block_len)
        start_idx += file_block_len
        if free_block_len > 0:
            free_space.append([start_idx, free_block_len])
            start_idx += free_block_len
    return filemap, free_space

def compact_disk(filemap, free_space):
    for id_num in sorted(filemap.keys(), reverse=True):
        file_idx, fileblock_len = filemap[id_num]
        large_enough = filter(lambda x: x[1] >= fileblock_len, free_space)
        first_free = next(large_enough, None)
        if first_free and first_free[0] < file_idx:
            # move file
            free_idx, free_len = first_free            
            filemap[id_num] = (free_idx, fileblock_len)
            # reduce free block where file is moved
            if (fileblock_len == free_len):
                free_space.remove(first_free)                
            else:
                first_free[0] += fileblock_len
                first_free[1] -= fileblock_len
            # add a new free block where file was moved from
            free_space.append([file_idx, fileblock_len])
            # TODO need to merge adjacent blocks of free space

    return filemap, free_space

def diskmap_list(filemap, free_space):
    blocks = [(idx, id_num, block_len) for id_num, (idx, block_len) in filemap.items()] 
    blocks += [(idx, ".", block_len) for idx, block_len in free_space]
    blocks.sort(key=lambda x: x[0])
    diskmap = []
    for _, id_num, block_len in blocks:
        diskmap += [str(id_num)] * block_len
    return diskmap
    
def checksum(diskmap):
    return sum(idx * int(file_id) for idx, file_id in enumerate(diskmap) if file_id != ".")
        
if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.readline().strip()
    file_map, free_space = read_disk(input)
    file_map, free_space = compact_disk(file_map, free_space)
    diskmap = diskmap_list(file_map, free_space)
    print(diskmap)
    print(checksum(diskmap))