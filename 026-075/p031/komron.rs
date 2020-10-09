// fn main() {
//     let curr: Vec<u32> = vec![200, 100, 50, 20, 10, 5, 2, 1];
//     let needed: u32 = 200;
//     let mut i = 0;

//     let mut curr_needed: u32 = needed;
//     while curr.len() > 0 { // popping of "used" combinations
//         while curr_needed != 0 {
//             let tot = 0;
//             let max_largest = needed / curr[0];
//             needed -= max_largest * curr[0];
//         }

//     }
    
// }

// need to write a recusrive function

fn main() {
    println!("{}", coin_combs(200, 8));
}


fn coin_combs(amount: u32, allowed: usize) -> u32 {
    let coins: Vec<u32> = vec![200, 100, 50, 20, 10, 5, 2, 1];

    match allowed {
        1 => 1,
        2..=8 => {
            let max_largest = amount / coins[coins.len() - allowed];
            let left = 0..=max_largest;
            left.map(|x| coin_combs(amount - x * coins[coins.len() - allowed], allowed - 1))
                .sum()
        },
        _ => 0,
    }
}
