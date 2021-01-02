# Getting Started with CircuitPython on nRF52840

1. [CircuitPython](#circuitpython)
2. [Interacting with nRF52840](#interacting-with-nRF52840)
3. [Install and Deploy your own Program](#install-and-deploy-your-own-program)

## CircuitPython

Basically you need:

- the firmware for the microcontroller nRF52840. This should already be installed on the supplied hardware!
- an editor. We will use the [Mu editor](https://codewith.mu/), which you should already have installed.

Use the steps described in the [Installing CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) from the [CircuitPython Guide](https://learn.adafruit.com/welcome-to-circuitpython/overview). The main steps in our setup are:

1. Check if the Mu editor is installed. If not, follow [these steps](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor).

2. Check that the [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) is connected via USB to your computer.

3. Check that you see the drive `CIRCUITPY` drive on your desktop.

**You are now ready for CircuitPython Programming**.

If you don't see the `CIRCUITPY` drive, you have to install the firmware yourself, but this should be optional:

1. [Get the firmware](https://circuitpython.org/board/feather_nrf52840_express/) for the Feather nRF52840 Express. Choose the latest stable firmware release. If your are still using Windows 7, install the [drivers](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython#windows-7-drivers-2977910-9). No additional drivers are needed for Mac, Linux or Windows 10.

2. [Start the bootloader mode](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython#start-the-uf2-bootloader-2977081-13) to be able to copy the firmware onto the microprocessor. Sometimes it takes a few tries.

3. Drag the firmware file to the boot drive `FEATHERBOOT`. The Boot Drive will automatically ejected and restarted as new drive called `CIRCUITPY`.

## Interacting with nRF52840

Using the Mu editor it is easy to interact with your nRF52840 microcontroller from your computer. There are two possibilities: 

1. Serial Console
2. REPL

### Using the Serial Console

If you have statements like `print("Hello World!)` in your code, the output must be written to a console which should be visible to you. It is the serial console, that receives such output from your CircuitPython board. The output is sent over USB to your computer so you can see it. But the serial console requires a terminal program, which is the visual interface between the console and the user.

Such a setup is really easy with the Mu editor, because the terminal and the serial console are already built in. Read [this chapter](https://learn.adafruit.com/welcome-to-circuitpython/kattni-connecting-to-the-serial-console#are-you-using-mu-2978926-4) to open the `Serial Console`.

If you are not using Mu, you have [other options](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux) to open a serial connection to your board.

### Using the REPL

REPL (Read-Evaluate-Print-Loop) is also available with the MU-Editor. Read [this chapter](https://learn.adafruit.com/welcome-to-circuitpython/the-repl) to start REPL from the Serial Console.


## Install and Deploy your own Program

Follow these instructions to install a [*Blink* program](blink) permanently on your microcontroller.

