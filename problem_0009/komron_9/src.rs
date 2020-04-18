fn main() {
    let upper: u32 = 1000;

    for i in 1..upper {
        for j in 1..upper {
            let k: f32 = (i.pow(2) as f32 + j.pow(2) as f32).sqrt();
            if k.fract() == 0.0 && i + j + k as u32 == upper {
                println!("{}", i * j * k as u32);
                break;
            }
        }
    }
}