# CP Utilities

To support IDE-like compilation and running of code in
various languages at one place, you may use the following setup.

## Prerequisites

- Python 3.0 or above
- Environment variable `CP_COMMON_UTIL_DIR` pointing to this directory

***

## Setup on Visual Studio Code

- From the command palette (ctrl+shift+p) open "Tasks: Open User tasks"
0 Select 'Other'
- Paste the contents of `tasks.json` there.

Now, test the setup:
- Open a folder
- Create some source code (say C++)
- Create input in `input.txt`
- Run Build task (default hotkey ctrl+shift+b) to compile
- Run Test task to run code (producing `output.txt`)

***

## Setup on Vim

- Simply use the vimrc (and gvimrc if using GVim)

***

## Configuration File

The configuration file `config.json` has format:
```
{
    "langs": [
        {
            "name": "", // Name of lang
            "ext": "", // File extension of source code
            "commands": {
                "compile": "", // Compile command using % for source file name (optional)
                "run": "" // Run command using % for source file name
            }
        },
        ...
    ]
    "runConfig": {
        "terminalIO": true/false, // Use shell IO or file IO
        "inputFile": "", // Name of input file
        "outputFile": "", // Name of output file
        "useSameDir": true/false, // If true directory for
        // input/output files will be same as that of source file
        // Otherwise, this (utilities) directory will be used
        "timeLimit": Integer, // Time limit of execution in seconds
    },
    "useColors": true/false // Use colors for messages such as error
}
```

***
