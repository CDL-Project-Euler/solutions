use std::collections::HashSet;

fn find_factors(x: usize) -> HashSet<usize> {
    let sqrt = ((x as f64).sqrt() + 1.0) as usize;

    let factors: HashSet<usize> = (1..sqrt)
        .filter(|i| x % i == 0)
        .map(|i| vec![i, (x / i)])
        .flatten()
        .collect();

    factors
}

fn gen_triangle_number(nth: usize) -> usize {
    (0..=nth).fold(0, |sum, x| sum + x)
}

fn main() {
    let mut counter: usize = 0;
    let upper: usize = 500;

    loop {
        let num = gen_triangle_number(counter);
        let len_factors = find_factors(num).len();
        println!("num: {}", num);

        if len_factors > upper {
            println!("{}", num);
            break;
        }

        counter += 1;
    }
}