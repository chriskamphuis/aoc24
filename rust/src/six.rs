use std::collections::HashSet;
use std::fs;
use crate::utils::data_path;

#[derive(Eq, Hash, PartialEq, Clone, Copy)]
enum Direction {
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3,
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

    fn to_int(&self) -> i32
    {
        match self {
            Direction::NORTH => 0,
            Direction::EAST => 1,
            Direction::SOUTH => 2,
            Direction::WEST => 3,
        }
    }
}

fn next_location(location: (i32, i32), direction: Direction) -> (i32, i32) {
    match direction {
        Direction::NORTH => (location.0 - 1, location.1),
        Direction::EAST  => (location.0, location.1 + 1),
        Direction::SOUTH => (location.0 + 1, location.1),
        Direction::WEST  => (location.0, location.1 - 1)
    }
}

pub fn main() {
    let mut obstructions = [false; 130 * 130];
    let mut guard_start: (i32, i32) = (0, 0);
    let mut visited: HashSet<(i32, i32)> = HashSet::with_capacity(130*130);

    let data = fs::read_to_string(data_path("6.txt")).expect("Something went wrong reading the file");
    let rows = data.split_whitespace();
    for (y, row) in rows.enumerate() {
        for (x, cell) in row.chars().enumerate() {
            match cell {
                '.' => {},
                '#' => obstructions[y*130 + x] = true,
                '^' => guard_start = (y as i32
                                      , x as i32
                ),
                _ => panic!("Should not be possible")
            }
        }
    }

    let mut guard = guard_start;
    let mut direction = Direction::NORTH;
    visited.insert(guard);
    loop {
        let nl = next_location(guard, direction);
        if nl.0 < 0 || nl.1 < 0 || nl.0 > 129 || nl.1 > 129 {
            break;
        }
        else if obstructions[(nl.0 * 130 + nl.1) as usize] {
            direction = direction.next();
        }
        else {
            visited.insert(nl);
            guard = nl;
        }
    }
    println!("{:?}", visited.len());

    visited.remove(&guard_start);
    let mut counter:i32
        = 0;
    for v in visited {
        obstructions[(v.0 * 130 + v.1) as usize] = true;
        let g = guard_start;
        if is_loop(g, Direction::NORTH, obstructions) {
            counter += 1;
        }
        obstructions[(v.0 * 130 + v.1) as usize] = false;
    }
    println!("{:?}", counter);
}

fn is_loop(_guard: (i32
                    , i32
), _dir: Direction, _obstacles: [bool; 130 * 130]) -> bool {
    let mut _dir = _dir;
    let mut _guard = _guard;
    let mut visited = [false; 130*130*4];
    visited[(_guard.0 * 130 * 4 + _guard.1 * 4 + _dir.to_int()) as usize] = true;

    loop {
        let new_loc = next_location(_guard, _dir);    // let mut obstructions: HashSet<(u8, u8)> = HashSet::with_capacity(130*130);
        if new_loc.0 < 0 || new_loc.0 > 129 || new_loc.1 < 0 || new_loc.1 > 129 {
            return false;
        }
        else if visited[(new_loc.0 * 130 * 4 + new_loc.1 * 4 + _dir.to_int()) as usize] {
            return true;
        }
        else if _obstacles[(new_loc.0 * 130 + new_loc.1) as usize] {
            _dir = _dir.next();
        }
        else {
            visited[(new_loc.0 * 130 * 4 + new_loc.1 * 4 + _dir.to_int()) as usize] = true;
            _guard = new_loc;
        }
    }
}