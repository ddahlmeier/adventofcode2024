use std::collections::HashMap;
use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    let input = fs::read_to_string(file_path).expect("Should have been able to read the input");
    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();
    
    for line in input.lines() {
        let tup: Vec<&str> = line.split_whitespace().collect();
        list1.push(tup[0].parse().expect("not a number"));
        list2.push(tup[1].parse().expect("not a number"));
    } 

    // part 1
    list1.sort();
    list2.sort();
    let mut distance = 0;

    for (left, right) in list1.iter().zip(list2.iter()) {
        distance += (left - right).abs();
    }
    println!("Part1 {distance}");

    // part 2
    let mut counts = HashMap::new();
    for item in list2 {
        *counts.entry(item).or_insert(0) += 1;
    }
    
    let mut similarity = 0;
    for item in list1 {
        let multiplier = *counts.entry(item).or_insert(0);
        similarity += item * multiplier;
    }
    println!("Part2 {similarity}");
}
