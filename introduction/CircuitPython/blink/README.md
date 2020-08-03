# Blink Application

## Intro

After reading the chapter about [Creating and Editing Code](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code), you will know that the CircuitPython looks for a code file named `code.txt`, `code.py`, `main.txt` or `main.py` to start first. One of them will be the main program that starts the entire application.

## Challenge

The file `blink.py` has defined the function `do_blink()` to toggle the onboard led (red) endlessly. If you copy this file onto your microcontroller, nothing happens. Your code will not be called by CircuitPython.

Questions: 
 - How is it possible to integrate own code into a CircuitPython application?
 - What is the link between the main program and your code, e.g. `blink.py`?

## Solution

To structure your application, you can place your code in different `*.py` files. Only the names `boot.py`, `settings.py`, `code.py` or `main.py` are reserved (see [Behavior](https://circuitpython.readthedocs.io/en/5.3.x/docs/index.html#behavior)).

**Example**: 

Place your startup code into a file named `code.py`:

```python
import blink

blink.do_blink()
```

This will call the function `do_blink()` after the startup.

