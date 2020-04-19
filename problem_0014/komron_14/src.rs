fn main() {
    let mut current_longest = 0;

    for i in (1..1_000_000_u128) {
        let i_len = len_collatz(i);

        if i_len > current_longest {
            current_longest = i_len;
            println!("{}", i);
        }
    }
}

fn len_collatz(n: u128) -> u128 {
    let mut current = n;
    let mut count = 0;

    while current != 1 {
        if current % 2 == 0 {
            current /= 2
        } else {
            current = current * 3 + 1
        }

        count += 1
    }

    count
}