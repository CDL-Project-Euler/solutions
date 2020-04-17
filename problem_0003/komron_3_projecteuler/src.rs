fn main() {
    let upper: f64 = 600851475143.0;
    let mut largest = 0.0;
    let range = upper.powf(0.5);

    for i in 2..=range as i32 {
        if (upper % i as f64 == 0.0) && is_prime(i as f64) {
            largest = i as f64;
        }
    }

    println!("{}", largest)
}

fn is_prime(x: f64) -> bool {
    let range = x.powf(0.5);

    for i in 2..=range as i32 {
        if x % i as f64 == 0.0 {
            return false;
        }
    };
    
    return true;
}
