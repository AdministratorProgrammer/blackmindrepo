use clap::Parser;
use std::io;

/// BLACKMINDREPO
#[derive(Parser)]
#[command(name = "blackmindrepo", version, about)]
struct Cli {
    /// Project name
    #[arg(required_unless_present = "no_save")]
    project_name: Option<String>,

    /// Don't save the project to disk (in that case, the [PROJECT_NAME] parameter is not required)
    #[arg(short = 'd', long = "no-save")]
    no_save: bool,

    /// Open project. Use with [PROJECT_NAME] parameter. Ignored when using --no-save.
    #[arg(short = 'o', long = "open")]
    open: bool
}

fn create_project(project_name: &str) {
    println!("\"{project_name}\" project was created.");
}

fn open_project(project_name &str) {
    println!("\"{project_name}\" project was opened.");
}

fn main() -> Result<(), io::Error> {
    let cli = Cli::parse();

    // Clap requiered "project_name" parameter (if --no-save or -d is not used).
    // When using --no-save (or -d), this condition is not met.
    if let Some(name) = cli.project_name {
        open_project(&name);
    } else {
        cleate_project(&name);
    }

    // End of program
    Ok(())
}
