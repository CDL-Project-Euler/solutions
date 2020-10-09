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

fn truncate(x: usize) -> Vec<usize> {
    let mut xi = x;
    let mut xk = x;
    let mut truncs: Vec<usize> = vec![];

    xi /= 10;
    while xi > 0 {
        truncs.push(xi);
        xi /= 10;
    }

    while xk > 0 {
        truncs.push(xk);
        xk %= 10_usize.pow((xk as f64).log10() as u32);
    }

    truncs
}

fn main() {
    let sieve = prime_sieve();
    let mut sum = 0;
    let mut ct = 1;

    for n in (11..=1_000_000).step_by(2) {
        if truncate(n).into_iter().all(|x| sieve[x] == true) {
            println!("{}. {}", ct, n);
            sum += n;
            ct += 1;
        }
    }

    println!("{}", sum);
}