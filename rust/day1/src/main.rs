use std::fs;


fn main() {
    
    // Read in string file
    let test_input = fs::read_to_string("./test_intput.txt");

    println!("{:?}", test_input);

    let splitted = test_input.unwrap();

    let elves: Vec<(i32, String)> = Vec::new();
    let current_elf: (i32, &str) = (-1, "");

    for line in splitted.to_string().split('\n').into_iter() {
        let digit = line.split("\r").collect::<Vec<&str>>()[0].as_bytes();

        if digit.len() != 0 && digit[0].is_ascii_digit()  {
            println!("Print Digit! {:?}", digit);

            if current_elf.0 == -1 && current_elf.1.is_empty() {
                
                // current_elf = (elves.len(), )

            }

        }
        else {
            println!("Spacing!")
        }


        // println!("{:?}", line.split("\r").collect::<Vec<&str>>()[0])
    }
    
}

