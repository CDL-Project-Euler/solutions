fn main() {
    let mut total = 0;

    let mut last = 0;
    let mut tmp = 0;
    let mut current = 1;

    while current <= 4000000 {
        tmp = current;
        current = last + current;
        last = tmp;

        if current % 2 == 0 {
            total += current;
        };
    };

    println!("{}", total);
}