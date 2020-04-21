// Starting in the top left corner of a 2×2 grid, and only being able to move
// to the right and down, there are exactly 6 routes to the bottom right
// corner.
// How many such routes are there through a 20×20 grid?
//
// F(1) = 2
// F(2) = 6
// F(3) = 20
//
// takes 2n steps in an n*n grid, e.g. for 20*20 it's 40
// which of the 40 are in y-direction and which are in the x-direction
// permutations: 2n! / (n!)(n!)
// = 40!/20!^2

use num::{BigUint};
use num::pow::Pow;

fn main() {
    let grid = BigUint::from(20_u32);

    println!("{}", factorial(2_u32 * grid.clone()) / factorial(grid.clone()).pow(2_u32))
}

fn factorial(x: BigUint) -> BigUint {
    let one = BigUint::from(1_u32);
    let zero = BigUint::from(0_u32);

    if x == zero || x == one {
        return BigUint::from(1_u32);
    } else {
        return factorial(x.clone() - BigUint::from(1_u32)) * x;
    }
}
