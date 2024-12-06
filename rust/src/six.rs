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

fn next_location(location: (i16, i16), direction: Direction) -> (i16, i16) {
    match direction {
        Direction::NORTH => (location.0 - 1, location.1),
        Direction::EAST  => (location.0, location.1 + 1),
        Direction::SOUTH => (location.0 + 1, location.1),
        Direction::WEST  => (location.0, location.1 - 1)
    }
}

pub fn main() {
    let mut obstructions = [false; 130 * 130];
    let mut guard_start: (i16, i16) = (0, 0);
    let mut visited: HashSet<(i16, i16)> = HashSet::with_capacity(130*130);

    let data = fs::read_to_string(data_path("6.txt")).expect("Something went wrong reading the file");
    let rows = data.split_whitespace();
    for (y, row) in rows.enumerate() {
        for (x, cell) in row.chars().enumerate() {
            match cell {
                '.' => {},
                '#' => obstructions[y*130 + x] = true,
                '^' => guard_start = (y as i16, x as i16),
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
    let mut counter:i16 = 0;
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

fn is_loop(_guard: (i16, i16), _dir: Direction, _obstacles: [bool; 130 * 130]) -> bool {
    let mut _dir = _dir;
    let mut _guard = _guard;
    let mut visited: HashSet<(i16, i16, Direction)> = HashSet::with_capacity(130*130*4);
    visited.insert((_guard.0, _guard.1, _dir));
    loop {
        let new_loc = next_location(_guard, _dir);
        if visited.contains(&(new_loc.0, new_loc.1, _dir)) {
            return true;
        }
        else if new_loc.0 < 0 || new_loc.0 > 129 || new_loc.1 < 0 || new_loc.1 > 129 {
            return false;
        }
        else if _obstacles[(new_loc.0 * 130 + new_loc.1) as usize] {
            _dir = _dir.next();
        }
        else {
            visited.insert((new_loc.0, new_loc.1, _dir));
            _guard = new_loc;
        }
    }
}