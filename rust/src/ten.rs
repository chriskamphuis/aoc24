use crate::utils::data_path;
use std::fs;

pub fn main() {
    // part b
    let mut grid: [u8; 47*47] = [0u8; 47*47];
    let mut scores: [Option<u8>; 47*47] = [None; 2209];
    let mut starts: Vec<(u8, u8)> = Vec::new();
    let mut count = 0u32;

    fn routes(y:u8, x:u8) -> u32 {
        match grid[y as usize * 47 + x as usize] {

        }
    }

    let data = fs::read_to_string(data_path("10b.txt")).expect("Something went wrong reading the file");
    for (y, line) in data.lines().enumerate() {
       for (x, c) in line.chars().enumerate() {
           match c {
               '0' => {
                   grid[y*47+x] = 0u8;
                   starts.push((y as u8, x as u8))
               },
               '9' => {
                   scores[y*47+x] = Option::from(1u8);
                   grid[y*47+x] = 9u8;
               }
               other => {
                   grid[y*47+x] = other.to_digit(10).unwrap() as u8;
               }
           }
       }
    }
    for (y, x) in starts {
        count += routes(y, x);
    }
    println!("count: {}", count);
}
