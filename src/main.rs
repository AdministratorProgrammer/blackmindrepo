use clap::Parser;
use std::io;

/// BLACKMINDREPO
#[derive(Parser)]
#[command(name = "blackmindrepo", version, about)]
struct Cli {
    /// Project name
    project_name: Option<String>,

    /// Don't save the project to disk (in that case, the [PROJECT_NAME] parameter is not required)
    #[arg(short = 'd', long = "no-save")]
    no_save: bool,
}

fn create_project(project_name: String) {
    println!("\"{project_name}\" project was created.");
}

fn main() -> Result<(), io::Error> {
    let cli = Cli::parse();

    if !cli.no_save {
        match cli.project_name {
            Some(name) => create_project(name),
            None => {
                println!("Usage: blackmindrepo <PROJECT_NAME> \n");
                println!("For more information, try '--help'.");
            }
        };
    }

    // End of program
    Ok(())
}
