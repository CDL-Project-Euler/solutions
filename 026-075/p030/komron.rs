fn main() {
    let mut sum = 0;
    // testing has found above 200K we get same thing until tested 1M
    for i in 10..200_000 {
        let mut n = i;
        let mut digs_sum = 0;

        while n > 0 {
            let last_digit = n % 10;

            digs_sum += match last_digit {
                // compute all ints to pow 5
                0 => 0,
                1 => 1,
                2 => 32,
                3 => 243,
                4 => 1024,
                5 => 3125,
                6 => 7776,
                7 => 16807,
                8 => 32768,
                9 => 59049,
                _ => 0,
            };

            n /= 10;
        }

        
        if digs_sum == i {
            sum += i;
        }
    }

    println!("{}", sum);
}