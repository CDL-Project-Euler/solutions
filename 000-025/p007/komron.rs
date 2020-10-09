fn main() {
    let nth_prime = 10_001;
    let mut counter = 0;
    let mut current = 0;
    let mut current_prime = 0;

    while counter < nth_prime {
        if is_prime(current as f64) {
            current_prime = current;
            counter += 1;
        }

        current += 1;
    }

    println!("{}", current_prime);
}

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
