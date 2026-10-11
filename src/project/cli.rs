use clap::Parser;
use rustyline::error::ReadlineError;
use rustyline::{DefaultEditor, Result};


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

pub fn shell() -> Result<()> {
    let mut rl = DefaultEditor::new()?;

    loop {
        println!("┌── BLACKMINDREPO SHELL");
        let readline = rl.readline("└─$ ");
        match readline {
            Ok(line) => {
               match command_handler(&line) {
                    Ok(true) => break,     // exit
                    Ok(false) => {}        // continue
                    Err(e) => eprintln!("Error: {e}"),
                } 
            },
            Err(ReadlineError::Interrupted) => {
                continue;
            },
            Err(ReadlineError::Eof) => {
                println!("CTRL-D");
                break;
            },
            Err(err) => {
                println!("Error: {:?}", err);
                break;
            }
        }
    }

    Ok(())
}

fn command_handler(command: &str) -> Result<bool> {
    match command {
        "help" => {
            println!("Command: help, exit");
            Ok(false)
        }
        "exit" => Ok(true),
        other => {
            println!("Type \"help\"");
            Ok(false)
        }
    }
}
