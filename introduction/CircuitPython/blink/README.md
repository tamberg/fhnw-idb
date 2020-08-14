# Blink

## Intro

After reading this tutorial on [Creating and Editing Code](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code), you should be aware of the following specialities:

- CircuitPython looks for a code file named `code.py` (also `code.txt`,  `main.txt` or `main.py`) to run.

- Microcontroller programs - and therefore our CircuitPython programs - usually have the following code structure:

  ```python
  # Libraries
  # Import all libraries you will need in your program
  import ...

  # Constants
  # Define the constants
  MY_CONST = ...

  # Setup
  # Use the setup to initialize variables, pin modes, set up
  # libraries, etc. The setup runs once, after each
  # powerup or reset of the board.
  my_var = ...

  # Main Loop
  # Loops consecutively, allowing the program to 
  # measure inputs and control outputs.
  while True:
     # do your work here
     ...
  ```

## Question

The program `blink.py` toggles the onboard led (red) endlessly.

 - How is it possible to run this CircuitPython program on your board?
 - What happens if you reconnect your board? Does the program restart?

## Solution

Copy the file `blink.py` to the board into a file called `code.py`. 

- Using the `teminal` applicaton on MacOS:

  ```shell
  $ cp blink.py /Volumes/CIRCUITPY/code.py
  ```

- Using the `cmd` application on Windows (`CIRCUITPY` as `D:`):

  ```shell
  % copy blink.py D:\code.py
  ```

- Using the Mu editor:

  Create the new file `code.py` and copy the content of `blink.py` into this file. Save the file on the drive `CIRCUITPY`.

Read the chapter [Behavior](https://circuitpython.readthedocs.io/en/5.3.x/docs/index.html#behavior) to find out, what files are run after a restart and how CircuitPython recovers from a powerup or reset.

