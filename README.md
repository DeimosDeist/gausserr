# gausserr
This is a sympy and tkinter gui tool written in python to just get gaussian errors for expressions. 

I think there are better ones out there, I just could not find a good enough website that did not make me want to quit.

## Features

- Enter an equation with variables and their associated errors.
- Optional: Provide values for the variables to compute actual and relative errors.
- Displays symbolic and numerical results.

## Usage
Run the program as an executable (find the releases [here](https://github.com/DeimosDeist/gausserr/releases)) or as a script and enter the equations. Variables _can_ be longer than just one letter.
The result can be copied afterwards.

## Known issues
If there are numbers in your Equation (e.g. 3*b + x) then there is a bug where it does not give a symbolic answer. The answer seems to be correct nevertheless and if you need the symbolic you can just add a variable instead of the number with error 0 and then replace it again. This works fine.

---
## Building

To build the executable from source, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/DeimosDeist/gausserr.git
   cd gausserr
   ```
   Then get the requirements up to date
   ```bash
   pip install -r requirements.txt
   ```
   and then just build it:
   ```bash
   pyinstaller --onefile --windowed your_script_name.py
   ```

   alternatively just run the script as a .py file


---
## Disclaimer

This software is provided "as-is", without any express or implied warranty. In no event shall the author or contributors be held liable for any damages arising from the use of this software. By using this software, you agree to use it at your own risk.

While I strive to ensure that this software functions as intended, it is provided for educational purposes and should not be relied upon for any critical or sensitive work.

Downloading and running the provided executable files is at the user's discretion, and it is recommended to review the source code and build the executable yourself to ensure safety and security.
