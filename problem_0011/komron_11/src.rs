use std::fs;

fn main() {
    let text = fs::read_to_string("../11_input.txt").unwrap();

    let lines: Vec<&str> = text
        .split("\n")
        .collect();
    
    let mut matrix: Vec<Vec<i32>> = Vec::new();

    for line in lines.into_iter() {
        matrix.push(
            line.split(" ")
                .map(|x| x.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
        )
    }

    print!("{}", product_dir(&matrix, 4));
}

fn product_dir(matrix: &[Vec<i32>], size: usize) -> i32 {
    let mut greatest_product = 0;

    // horizontal
    for i in 0..matrix.len() {
        for j in 0..=matrix[i].len()-size {
            let current = matrix[i][j..j+size].iter().product();

            if current > greatest_product {
                greatest_product = current;
            }
        }
    }

    // vertical
    for i in 0..=matrix.len()-size {
        for j in 0..matrix[i].len() {
            let mut current = 1;
            for k in 0..size {
                current *= matrix[i+k][j];
            }

            if current > greatest_product {
                greatest_product = current;
            }
        }
    }

    // ascending
    for i in 0..=matrix.len()-size {
        for j in 0..=matrix[i].len()-size {
            let mut current = 1;
            for k in 0..size {
                current *= matrix[i+k][j+k];
            }

            if current > greatest_product {
                greatest_product = current;
            }
        }
    }

    // descending
    for i in size+1..matrix.len() {
        for j in 0..=matrix[i].len()-size {
            let mut current = 1;
            for k in 0..size {
                current *= matrix[i-k][j+k];
            }

            if current > greatest_product {
                greatest_product = current;
            }
        }
    }

    greatest_product
}