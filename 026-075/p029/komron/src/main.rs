use std::collections::HashSet;
use num::{BigUint, pow};

fn main() {
    let mut terms: HashSet<BigUint> = HashSet::with_capacity(10_000);

    for a in 2..=100 {
        for b in 2..=100 {
            terms.insert(pow(BigUint::from(a as u32), b));
        }
    }

    println!("{}", terms.len());
}