use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    let input = fs::read_to_string(file_path).expect("Should have been able to read the input");
    let records = input.lines();
    let mut count_safe = 0;

    for record in records {
        let items :Vec<&str> = record.split_whitespace().collect();
        let values: Vec<i32> = items.into_iter().filter_map(|word| word.parse::<i32>().ok()).collect();
        let pairs: Vec<(i32, i32)> = values
        .iter()
        .zip(values.iter().skip(1))
        .map(|(&a, &b)| (a, b))  // Dereference the references to get values
        .collect();

        let is_ascending = pairs.iter().all(|&(a, b)| a < b);
        let is_descending = pairs.iter().all(|&(a, b)| a > b);
        let has_okay_stepsize = pairs.iter().all(|&(a, b)| 1 <= (a-b).abs() && (a-b).abs() <= 3);
        if (is_ascending | is_descending) && has_okay_stepsize {
            count_safe += 1;
        }
    }   
    println!("{count_safe}");

}
