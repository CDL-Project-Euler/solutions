fn rotations(x: usize) -> Vec<usize> {
    let mut rots = vec![x];
    let mut xi = x;
    let length = ((x as f64).log10() + 1.0_f64) as usize;

    for _ in 1..length {
        let ldig = xi % 10;
        xi /= 10;

        let new_rot = xi + (ldig * 10_usize.pow((length - 1) as u32));

        xi = new_rot;

        rots.push(new_rot);
    }

    rots
}

fn prime_sieve() -> [bool; 1_000_000] {
    let mut prime = [true; 1_000_000];
    prime[0] = false;
    prime[1] = false;

    let sqrt_range = ((prime.len() as f64).sqrt() as usize) + 1;
    let max_range = prime.len();

    // removing all evens except 2
    let mut composite = 2;
    for step in (composite * composite..max_range).step_by(composite) {
        prime[step] = false;
    }

    composite = 3;
    while composite < sqrt_range {
        if prime[composite] == true {
            for step in (composite * composite..max_range).step_by(2 * composite) {
                prime[step] = false;
            }
        }

        composite += 2;
    }

    prime
}

fn main() {
    let sieve = prime_sieve();
    let mut ct = 0;

    for n in (1..=1_000_000).step_by(2) {
        if rotations(n).into_iter().all(|x| sieve[x] == true) {
            println!("{}", n);
            ct += 1
        }
    }

    ct += 1; // 2 is skipped above

    println!("count {}", ct);
}