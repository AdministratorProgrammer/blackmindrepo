use clap::Parser;

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


fn main() {
    let cli = Cli::parse();

    let project_name = match cli.project_name {
        Some(name) => name,
        None => "tmp".to_string(),
    };

    println!("{}", project_name);
}
