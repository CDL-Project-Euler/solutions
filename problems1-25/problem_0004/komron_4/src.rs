fn main() {
    let mut current = 0;

    for i in (500..999).rev() {
        for j in (500..999).rev() {

            let prod = i * j;

            if is_palindrome(prod) {
               if prod > current {
                   current = prod;
               }
           }
        }
    }

    println!("{}", current);
}

// efficient palindrome, originally i just reversed a string...
// thanks https://leetcode.com/articles/palindrome-number/#
fn is_palindrome(num: i32) -> bool {
    let mut num = num;
    if num % 10 == 0 && num != 0 {
        return false;
    }

    let mut reverted = 0;

    while num > reverted {
        reverted = reverted * 10 + num % 10;
        num = num / 10;
    }

    num == reverted || num == reverted / 10
}