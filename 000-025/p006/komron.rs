fn main() {
    let range: Vec<i32> = (0..=100).collect();

    let squared_ind: i32 = range
        .iter()
        .map(|&x| x.pow(2))
        .sum();
    
    let squared_sum: i32 = range
        .iter()
        .sum::<i32>()
        .pow(2);
    
    println!("diff: {}", squared_sum - squared_ind);
}