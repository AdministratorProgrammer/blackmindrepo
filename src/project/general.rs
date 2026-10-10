use std::fs;
use std::io::ErrorKind;

pub fn create_project(project_name: &str) {
    match fs::create_dir_all(project_name) {
        Ok(_) => {
            println!("\"{}\" project was created.", project_name);
        },
        Err(e) => match e.kind() {
            ErrorKind::AlreadyExists => {
               println!("\"{}\" directory already exists!", project_name);
            }
            _ => eprintln!("{}", e)
        }
    }
}

pub fn open_project(project_name: &str) {
    println!("\"{}\" project was opened.", project_name);
}
