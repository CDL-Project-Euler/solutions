use num::BigUint;
use num::pow::Pow;

fn main() {
    let a = BigUint::from(2_u8).pow(1000_u32);
    let sum: u32 = a.to_string()
        .chars()
        .map(|x| x.to_digit(10).unwrap())
        .fold(0, |sum, x| sum + x);

    println!("{}", sum);
}
