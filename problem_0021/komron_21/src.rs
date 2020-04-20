use std::collections::HashSet;

// unoptimized; returns a set, instead of integer count
fn proper_divisors(x: usize) -> HashSet<usize> {
    let sqrt = ((x as f64).sqrt() + 1.0) as usize;

    let mut factors: HashSet<usize> = (1..sqrt)
        .filter(|i| x % i == 0)
        .map(|i| vec![i, (x / i)])
        .flatten()
        .collect();

    if !factors.remove(&x) {
        panic!("improper divisors!");
    }

    factors
}

fn main() {
    let mut amigos: HashSet<usize> = HashSet::new();

    // unoptimized; calculates ints that are already known amicable
    for i in 2..10000 {
        let sum = proper_divisors(i).iter().sum();
        let sum2 = proper_divisors(sum).iter().sum();

        if i == sum2 && i != sum {
            amigos.insert(i);
            amigos.insert(sum2);
        }
    }

    println!("{:#?}", amigos.iter().sum::<usize>());
}