use num::{BigInt, FromPrimitive};
use std::fs;

fn main() {
    let file = fs::read_to_string("13_input.txt").unwrap();

    let nums: Vec<BigInt> = file.split("\n")
        .map(|x| x.parse::<BigInt>().unwrap())
        .collect();
    
    let sum = nums.into_iter()
        .fold(BigInt::from_u8(0).unwrap(), |sum, x| sum + x);
    
    println!("{:#?}", &sum.to_string()[..10]);
}
