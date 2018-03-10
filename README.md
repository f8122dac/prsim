# prsim

## Dependancy
[Python3](https://www.python.org/downloads/), tkinter, matplotlib

tkinter and matplotlib are python packages that we used in this project and required to run the script. According to [the Wikipedia page](https://en.wikipedia.org/wiki/Tkinter), tkinter is included with the standard Microsoft Windows and Mac OS X install of Python. 

On Linux or OS X, you can install matplotlib by `pip install matplotlib` or `python3 -mpip install matplotlib` 

On Windows, if you have a python3 installation you can probably install using pip with the the same command(though I haven't checked).

If you don't have python3 installed and just want to run the program(and have more than 500MB to spare on your machine), [anaconda](https://www.anaconda.com/download/) is a nice default python installation that comes with a bunch of scientific computing packages, and it will just run with the default. Alternatively, install [miniconda](https://conda.io/miniconda.html) and on a terminal or Windows command line execute `conda install matplotlib tkinter`.

## How to run
### On POSIX systems(Linux, OS X, etc):

    $ ./run.sh

or

    $ python3 src/main.py
   
### on Windows:

If you have setupt the dependancy, you can start by executing `main.py` file in `src` directory.

### Keys:
- Main window
  - `r`: show/hide report window
  - `n`: generate a new model
  - `p`: plot current model
  - `x`: close plot window
  - `j`: decrease # of pages
  - `k`: increase # of pages
  - `J`: decrease # of pages by big steps
  - `K`: increase # of pages by big steps
  - `h`: decrease # of links
  - `l`: increase # of links
  - `H`: decrease # of links by big steps
  - `L`: increase # of links by big steps
- Report window  
  - `i`: decrease iteration slider
  - `o`: increase iteration slider
  - `I`: decrease iteration slider by big steps
  - `O`: increase iteration slider by big steps
