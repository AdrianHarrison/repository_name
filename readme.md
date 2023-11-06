# Single File Cli Utility

## What is it?

Barebones CLI tool for passing arguments into an equation. Basically just some function boilerplate and an [argparse](https://docs.python.org/3/library/argparse.html) wrapper.

Rename anything you don't like or that doesn't make sense. More details in the `single_file_cli_utility.py` file / comments about how things are actually implemented.

## Dependencies

* None, just the python standard library.
* If for some reason you have Python2 installed just replace it with [Python3](https://www.python.org/downloads/).
* If you don't know what version of python you have type `python --version` into your command line.
* If you don't have a code editor grab [VS Code](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/)

## How to run it:

In `powershell` or `cmd` you should have the `python` or `python3` command available to you. Depending on the function you're working on you can call either:

### A) Roll Resist

```python single_file_cli_utility.py -f roll -fr 1.0 -cr 2.0 -fn 3.0```

or the more verbose

```python single_file_cli_utility.py --function roll --roll_force 1.0 --roll_resist 2.0 --norm_force 3.0```

### B) Drag Force

```python single_file_cli_utility.py -f drag -fp 1.0 -p 2.0 -v 3.0```

or the more verbose

```python3 single_file_cli_utility.py --function drag --drag_force 1.0 --fluid_density 2.0 --velocity 3.0```

## Hidden Args

I assumed drag coefficeint and frontal view were the constant values defined. If you want to override them you can just add them in using the:
* `--coeff_drag` or `-ca` flag
* `--frontal_view` or `-a` flag