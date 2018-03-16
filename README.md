# prsim

![screenshot](https://raw.githubusercontent.com/f8122dac/prsim/master/screenshot.png)

--- 

Project: Sorting the Infinite: Google's PageRank Algorithm

Members: Yifei Chen, Sara LaPlante, Jesse Cho, Zixiao Huang

## Release v0.0.2
Download links for the executables:
- [Windows](https://github.com/f8122dac/prsim/releases/download/v0.0.2/prsim-0.0.2.exe)
- [OS X](https://github.com/f8122dac/prsim/releases/download/v0.0.2/Prsim-0.0.2.dmg)


## How to run the source code
### Dependancy
[Python3](https://www.python.org/downloads/), tkinter, matplotlib

tkinter and matplotlib are python packages that we used in this project and required to run the script. According to [the Wikipedia page](https://en.wikipedia.org/wiki/Tkinter), tkinter is included with the standard Microsoft Windows and Mac OS X install of Python. 

On Linux or OS X, you can install matplotlib by `pip install matplotlib` or `python3 -mpip install matplotlib` 

On Windows, if you have a python3 installation you can probably install using pip with the the same command(though I haven't checked).

### Running
#### On POSIX systems(Linux, OS X, etc):
    $ ./run.sh

or

    $ python3 src/main.py
   
#### on Windows:
If you have setupt the dependancy, you can start by executing `main.py` file in `src` directory.


## Keys:
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
