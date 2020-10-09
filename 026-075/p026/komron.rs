// fn main() {
//     let ten: f64 = 10.0;
//     let mut longest = 0;
//     let mut longest_i = 0;

//     for i in 1..1000 {
//         // easy pickings
//         // 10's proper divisors except 1
//         if i % 2 == 0 || i % 5 == 0 {
//             continue;
//         }

//         // long division
//         // once the remainder reaches 1 again, the sequence repeats
//         let mut len = 0;
//         for j in 1.. {
//             let rem = (ten.powi(j) as i128) % i;
//             println!("i: {}, j: {}, rem: {}", i, j, rem);

//             if rem == 1 {
//                 len = j;
//                 break;
//             } else if rem == 0 {
//                 len = 0;
//                 break;
//             } else if ten.powi(j) == std::f64::INFINITY {
//                 len = j;
//                 break;
//             }
//         }

//         if len > longest {
//             longest = len;
//             longest_i = i;
//         }
//     }

//     println!("{}: {}", longest_i, longest);
// }

fn main() {
    // better solution may be generating primes

    let mut max_len: usize = 0;
    let mut max_den: usize = 0;
    let mut den: usize = 999;

    while max_len < den {
        let size = {
            let mut num: usize = 1;
            let mut a = [0; 1000];
            let mut index: usize = 0;
            let mut last_index: usize;

            loop {
                num %= den;
                last_index = a[num];

                if last_index != 0 {
                    break index - last_index;
                }

                a[num] = index;
                num *= 10;
                index += 1;
            }
        };

        if size > max_len {
            max_len = size;
            max_den = den
        }
        den -= 2;
    }

    println!("{}", max_den);
}