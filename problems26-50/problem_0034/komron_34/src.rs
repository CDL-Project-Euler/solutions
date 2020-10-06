fn factorial(x: usize) -> usize {
    (1..=x).product()
}

fn digit_factorial(x: usize) -> usize {
    let mut total: usize = 0;
    let mut xi = x;

    while xi > 0 {
        let last_dig = xi % 10;

        total += factorial(last_dig);

        xi /= 10;
    }

    total
}

fn main() {
    let mut sum = 0;
    for i in 3..50000  {
        if i == digit_factorial(i) {
            sum += i;
            println!("{}", i);
        }
    }

    println!("sum: {}", sum);
    
}