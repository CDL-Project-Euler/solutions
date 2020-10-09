use std::{fs, str::from_utf8};
use digits_iterator::*;

fn main() {
    let str_num = fs::read_to_string("number.txt").unwrap();
    let num = str_num.as_bytes();

    let mut greatest_p = 0;

    for i in 0..num.len()-13 {
        let mut product: u128 = 1;
        let slice = from_utf8(&num[i..i+13])
            .unwrap()
            .parse::<u64>().unwrap();

        for j in slice.digits() {
            product *= j as u128;
        }

        if product > greatest_p {
            greatest_p = product;
        }
    }

    println!("{:?}", greatest_p);
}