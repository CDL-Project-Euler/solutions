fn main() {
    let top = 1000;
    let mut total = 0;
    let multiples: [i32; 2] = [3, 5];
    
    for i in 0..top {
        if (i % multiples[0] == 0) && !(i % multiples[1] == 0) {
            total += i;
        } else if (i % multiples[1] == 0) && !(i % multiples[0] == 0) {
            total += i;
        } else if (i % multiples[0] == 0) && (i % multiples[1] == 0) {
            total += i;
        };
    };

    println!("{}", total);
}
