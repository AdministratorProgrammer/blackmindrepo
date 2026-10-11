mod project;

use std::io;
use clap::Parser;

fn main() -> Result<(), io::Error> {
    let cli = project::cli::Cli::parse();

    // Clap requiered "project_name" parameter (if --no-save or -d is not used).
    // When using --no-save (or -d), this condition is not met.
    if let Some(name) = cli.project_name {
        if cli.open {
            project::general::open_project(&name);
        } else {
            project::general::create_project(&name);
        }
    }

    project::cli::shell();

    // End of program
    Ok(())
}
