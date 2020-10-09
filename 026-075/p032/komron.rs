use std::collections::HashSet;

// fn next_perm(vect: &mut Vec<usize>) {
//     let mut i = vect.len() - 1; // pivot-to-be (index)

//     while i > 0 && vect[i - 1] >= vect[i] {
//         i -= 1;
//     }

//     if i == 0 {
//         panic!("last permutation!");
//     }

//     // smallest larger than pivot (index)
//     // inside the suffix
//     let mut j = vect.len() - 1;

//     // walks the suffix
//     while vect[j] <= vect[i - 1] {
//         // if current number larger than pivot
//         // but still minimum value
//         j -= 1;
//     }

//     // swap pivot with smallest larger than pivot
//     vect.swap(j, i - 1);
//     vect[i..].reverse();
// }

// fn seq_to_num(vec)

// fn main() {
//     let mut pand_nums= HashSet::new();

//     // generate the identities and see if they equal the product
//     let mut nums = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
//     let perm_num = 362880 // = 9!

//     for _ in 0..perm_num - 1 {
//         // multiplications makes only sense:
//         // 1x4, 4x1, 2x2, 2x3, 3x2
//         unimplemented!();

//         next_perm(nums);
//     }

//     println!("{}", pand_nums.iter().sum::<usize>()),
// }

// generating nums with permutations is stupid

fn is_unique(x: usize, digs: &mut [bool]) -> bool {
    let mut xi = x;

    while xi > 0 {
        let last = xi % 10;

        if digs[last] == true {
            return false;
        } else {
            digs[last] = true;
        }

        xi /= 10;
    }

    return true;
}

fn pandigital(into: Vec<usize>) -> bool {
    let mut digs = [false; 10];

    for num in into.into_iter() {
        if !is_unique(num, &mut digs) {
            return false
        }
    }

    // pandigital only
    if digs[1..].iter().any(|&x| x == false) || digs[0] == true {
        return false
    }

    return true
}

fn main() {
    let mut sum = HashSet::new();
    for i in 1..100 {
        for k in i..9876 {
            let prod = i * k;
            if pandigital(vec![i, k, prod]) && !sum.contains(&prod) {
                println!("{} x {} = {}", i, k, prod);
                sum.insert(prod);
            }
        }
    }

    let total: usize = sum.into_iter().sum();
    println!("{}", total);

    println!("{}", pandigital(vec![1, 23, 456789]));
}