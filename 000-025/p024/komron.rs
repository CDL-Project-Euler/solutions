
fn next_perm(vect: &mut Vec<usize>) {
    let mut i = vect.len() - 1; // pivot-to-be (index)

    while i > 0 && vect[i - 1] >= vect[i] {
        i -= 1;
    }

    if i == 0 {
        panic!("last permutation!");
    }

    // smallest larger than pivot (index)
    // inside the suffix
    let mut j = vect.len() - 1;

    // walks the suffix
    while vect[j] <= vect[i - 1] {
        // if current number larger than pivot
        // but still minimum value
        j -= 1;
    }

    // swap pivot with smallest larger than pivot
    vect.swap(j, i - 1);
    vect[i..].reverse();
}

fn main() {
    let mut a: Vec<usize> = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    for _ in 0..1_000_000 - 1 {
        next_perm(&mut a);
    }

    println!("{:?}", a);
}