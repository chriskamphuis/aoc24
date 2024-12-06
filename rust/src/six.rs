use std::collections::HashSet;
use std::fs;
use crate::utils::data_path;

#[derive(Eq, Hash, PartialEq, Clone, Copy)]
enum Direction {
    NORTH,
    EAST,
    SOUTH,
    WEST,
}

impl Direction {
    fn next(&self) -> Direction {
        match self {
            Direction::NORTH => Direction::EAST,
            Direction::EAST => Direction::SOUTH,
            Direction::SOUTH => Direction::WEST,
            Direction::WEST => Direction::NORTH,
        }
    }
}

fn next_location(location: (u8, u8), direction: Direction) -> (u8, u8) {
    match direction {
        Direction::NORTH => {
            if location.0 == 0 {
                return (255, 255)
            }
            (location.0 - 1, location.1)
        }
        Direction::EAST => {
            if location.1 == 129 {
                return (255, 255)
            }
            (location.0, location.1 + 1)
        },
        Direction::SOUTH => {
            if location.0 == 129 {
                return (255, 255)
            }
            (location.0 + 1, location.1)
        },
        Direction::WEST => {
            if location.1 == 0 {
                return (255, 255)
            }
            (location.0, location.1 - 1)
        },
    }
}

pub fn main() {
    let mut obstructions: HashSet<(u8, u8)> = HashSet::new();
    let mut guard_start: (u8, u8) = (0, 0);
    let mut visited: HashSet<(u8, u8)> = HashSet::with_capacity(130*130);

    let data = fs::read_to_string(data_path("6.txt")).expect("Something went wrong reading the file");
    let rows = data.split_whitespace();
    for (y, row) in rows.enumerate() {
        for (x, cell) in row.chars().enumerate() {
            match cell {
                '.' => continue,
                '#' => {
                    obstructions.insert((y as u8, x as u8));
                    continue
                },
                '^' => {
                    guard_start = (y as u8, x as u8);
                    continue
                }
                _ => panic!("Should not be possible")
            }
        }
    }

    let mut guard = guard_start;
    let mut direction = Direction::NORTH;
    visited.insert(guard);
    loop {
        let nl = next_location(guard, direction);
        if nl == (255, 255) {
            break;
        }
        else if obstructions.contains(&nl) {
            direction = direction.next();
        }
        else {
            visited.insert(nl);
            guard = nl;
        }
    }
    println!("{:?}", visited.len());

    visited.remove(&guard_start);
    let mut counter:i16 = 0;
    for v in visited {
        obstructions.insert(v);
        let g = guard_start;
        if is_loop(g, Direction::NORTH, obstructions.clone()) {
            counter += 1;
        }
        obstructions.remove(&v);
    }
    println!("{:?}", counter);
}

fn is_loop(_guard: (u8, u8), _dir: Direction, _obstacles: HashSet<(u8, u8)>) -> bool {
    let mut _dir = _dir;
    let mut _guard = _guard;
    let mut visited: HashSet<(u8, u8, Direction)> = HashSet::with_capacity(130*130*4);
    visited.insert((_guard.0, _guard.1, _dir));
    loop {
        let new_loc = next_location(_guard, _dir);
        if visited.contains(&(new_loc.0, new_loc.1, _dir)) {
            return true;
        }
        else if new_loc == (255, 255) {
            return false;
        }
        else if _obstacles.contains(&new_loc) {
            _dir = _dir.next();
        }
        else {
            visited.insert((new_loc.0, new_loc.1, _dir));
            _guard = new_loc;
        }
    }
}