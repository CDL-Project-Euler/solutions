use num::{BigInt, FromPrimitive};

fn is_prime(x: f64) -> bool {
    if x == 0.0 || x == 1.0 {
        return false
    }

    let range = x.powf(0.5);

    for i in 2..=range as i32 {
        if x % i as f64 == 0.0 {
            return false;
        }
    };

    return true;
}

fn main() {
    let mut sum = BigInt::from_u8(0).unwrap();

    for i in 0_i64..2_000_000_i64 {
        if is_prime(i as f64) {
            sum += i;
        }
    }

    println!("{}", sum.to_string());
}