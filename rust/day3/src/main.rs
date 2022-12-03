use std::fs;
use std::str::Chars;


fn check_string(first: &str, second: &str) -> String {
    let mut res = String::from("");

    for char in first.chars() {
        if second.contains(char) {
            res = String::from(char);
            // return char;
        }
    }

    return res;
}

fn get_first_and_second(characters: Chars, length: usize ) -> (String, String) {
    // println!("{:?}", characters);

    let mut counter: i8 = 0;
    let mut first: String = String::from("");
    let mut second: String = String::from("");

    for char in characters.into_iter() {
        // println!("{:?}", char);

        if counter < ((length/2)).try_into().unwrap() {
            first += &char.to_string();
        }
        else {
            second += &char.to_string();
        }
        
        counter += 1;
    }

    return (first, second);
}   

fn convert_to_asci(test: String) -> u32 {
    let chars: Vec<_> = test.chars().collect();
    let char = chars[0];
    
    if char.is_uppercase() {
        // println!("{:?}", value);
        return (char as u32) - 64 + 26;
    }
    else {
        return (char as u32) - 96
    }

}

fn check_similar(first: String, second: String, third: String) -> String {
    let mut res = String::from("");

    for char in first.chars() {
        if second.contains(char) && third.contains(char) {
            res = String::from(char);
        }
    }

    return res;
}

fn main() {
    // let input = fs::read_to_string("./test_input.txt");
    let input = fs::read_to_string("./input.txt");
    
    //let input_2 = fs::read_to_string("./test_input.txt");
    let input_2 = fs::read_to_string("./input.txt");


    // let lines: Vec<String> = test_input.unwrap().split('\n').collect();
    // println!("{:?}", lines);

    let mut total_value = 0;

    // === Part 1 ===

    for mut line  in input.unwrap().split('\n').collect::<Vec<&str>>() {
        line = line.trim_end();
        // let length = line.chars().count();
        // let line_chars = line.chars();

        let (first, second) = get_first_and_second(line.chars(), line.chars().count());

        // println!("{:?}", first);
        // println!("{:?}", second);

        let char = check_string(&first, &second);
        // println!("{:?}", char);

        let value = convert_to_asci(char);
        // println!("{:?}", value);

        total_value += value;

    }

    println!("Total value - part 1: {:?}", total_value);

    
    // === Part 2 ===

    total_value = 0;

    let mut buffer_lines = vec![];

    for mut line  in input_2.unwrap().split('\n').collect::<Vec<&str>>() {
        line = line.trim_end();
        buffer_lines.push(line);

        if buffer_lines.len() == 3 {
            let similar_char = check_similar(buffer_lines[0].to_string() , buffer_lines[1].to_string(), buffer_lines[2].to_string());

            let value = convert_to_asci(similar_char);
            
            total_value += value;

            buffer_lines = vec![];
        }


    }

    println!("Total value - part 2: {:?}", total_value);

}
