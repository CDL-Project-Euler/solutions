use num::{Integer, Num, BigUint};
use std::fmt::Debug;

// extremely inefficient
// memoization works best
fn fibonacci<T>(x: T) -> T
where T: Integer + Debug + Clone,
      <T as Num>::FromStrRadixErr : Debug,
{
    let zero = <T as Num>::from_str_radix("0", 10).unwrap();
    let one = <T as Num>::from_str_radix("1", 10).unwrap();
    let two = <T as Num>::from_str_radix("2", 10).unwrap();

    if x == zero {
        panic!("no fib for 0!");
    } else if x == one || x == two {
        return one;
    } else {
        return fibonacci(x.clone() - one) + fibonacci(x - two);
    }
}

fn main() {
    let mut length = 1_u32;
    let mut i = 2_u32;

    while length < 1000 {
        length = fibonacci(BigUint::from(i)).to_string().len() as u32;
        i += 1;
        println!("{}: {}", i, length);
    }
}
