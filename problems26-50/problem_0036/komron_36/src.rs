fn base10_pal(x: usize) -> bool {
    let mut xi = x;
    let mut rev = 0;

    while xi > 0 {
        rev = rev * 10 + xi % 10;
        xi /= 10;
    }

    rev == x
}

fn base2_pal(x: usize) -> bool {
    (x.clone().reverse_bits() >> x.leading_zeros()) == x
}

fn main() {
    let mut sum = 0;
    for i in 1..=1_000_000 {
        if base2_pal(i) && base10_pal(i) {
            sum += i;
            println!("{}; {:b}", i, i);
        }
    }

    println!("total: {}", sum);
}