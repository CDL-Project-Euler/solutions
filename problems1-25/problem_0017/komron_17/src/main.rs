use english_numbers::{Formatting, convert}; // bit o cheating ;)

fn main() {
    let mut form = Formatting::none();
    form.conjunctions = true;

    let sum: u64 = (1..=1000)
        .map(|x| convert(x, form).len())
        .fold(0, |a, b| a + b as u64);
    
    println!("{}", sum);
}
