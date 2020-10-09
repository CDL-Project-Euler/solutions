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
    let upper: i32 = 20;
    let nums: Vec<i32> = (0..=upper).collect();
    let mut smallest_num = 1;

    let primes: Vec<i32> = nums.into_iter()
        .filter(|x| is_prime(*x as f64))
        .collect();

    for p in primes.into_iter() {
        let mut i = 1;
        while i * p <= upper {
            i *= p;
        }
        smallest_num *= i;
    }
    println!("{:?}", smallest_num);
}