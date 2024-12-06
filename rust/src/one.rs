use crate::utils::data_path;
use std::fs;
pub fn main() {
    let input = fs::read_to_string(data_path("1.txt")).expect("Something went wrong reading the file");
    let x = input.split("\n")
        .map(|x| x.split_whitespace()
            .map(|e| e.parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
        ).collect::<Vec<Vec<i32>>>();
    println!("{:?}", x);
}