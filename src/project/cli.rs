use clap::Parser;

/// BLACKMINDREPO
#[derive(Parser)]
#[command(name = "blackmindrepo", version, about)]
pub struct Cli {
    /// Project name
    #[arg(required_unless_present = "no_save")]
    pub project_name: Option<String>,

    /// Don't save the project to disk (in that case, the [PROJECT_NAME] parameter is not required)
    #[arg(short = 'd', long = "no-save")]
    pub no_save: bool,

    /// Open project. Use with [PROJECT_NAME] parameter. Ignored when using --no-save.
    #[arg(short = 'o', long = "open")]
    pub open: bool
}
