// quadratic formulas calculated:
// right-ascending: n^2
// right-descending: 4n^2 - 10n + 7
// left-descending: 4n^2 - 8n + 5
// left-ascending: 4n^2 - 6n + 3

// combined with sum formula:
// 1/3(16n^3 - 18n^2 + 14n - 9)

const N: isize = 1001;
const N_SEQ: isize = N / 2 + 1;

fn main() {
    let eq = |n: isize| -> isize {
        (1.0 / 3.0 * (16 * n.pow(3) - 18 * n.pow(2) + 14 * n - 9) as f64) as isize
    };

    println!("{}", eq(N_SEQ));
}
