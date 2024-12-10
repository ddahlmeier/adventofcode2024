from itertools import zip_longest
import sys

def read_disk(input):
    # files are on even positions
    file_blocks = [int(input[i]) for i in range(0, len(input), 2)]
    # free space on odd positions
    free_blocks = [int(input[i]) for i in range(1, len(input), 2)]
    diskmap = []
    for id_num, (file_block, free_block) in enumerate(zip_longest(file_blocks, free_blocks, fillvalue=0)):
        diskmap += [str(id_num)] * file_block
        diskmap += ["."] * free_block
    return diskmap

def move_right(idx, diskmap):
    while (idx < len(diskmap) and diskmap[idx] != '.'):
        idx +=1
    return idx

def move_left(idx, diskmap):
    while (idx > 0 and diskmap[idx] == '.'):
        idx -=1
    return idx

def compact_disk(diskmap):
    left = 0
    right = len(diskmap)-1
    while (left < right):
        left = move_right(left, diskmap)
        right = move_left(right, diskmap)
        if (left >= right):
            break
        diskmap[left] = diskmap[right]
        diskmap[right] = "."

def checksum(diskmap):
    return sum(idx * int(file_id) for idx, file_id in enumerate(diskmap) if file_id != ".")
        
    
if __name__ == "__main__":
    with open(sys.argv[1]) as fin:
        input = fin.readline().strip()
    diskmap = read_disk(input)
    compact_disk(diskmap)
    print(checksum(diskmap))