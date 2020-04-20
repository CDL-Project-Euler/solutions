// 10 and 100 don't change the sum.
// 2, 20 doubles the first digit
// 3, 30 triples the first digit
// 4, 40 quadruples ...
// combinatorics is lost on me...
use num::{BigUint};

fn main() {
    let result = factorial(BigUint::from(100_u32));

    let sum: u32 = result
        .to_string()
        .chars()
        .map(|x| x.to_digit(10).unwrap())
        .fold(0_u32, |sum, x| sum + x);
    
    println!("{}", sum);
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