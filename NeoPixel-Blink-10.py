# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[0]=((255, 0, 0))
    pixels[1]=((0, 255, 0))
    pixels[2]=((0, 0, 255))
    pixels[3]=((255, 0, 0))
    pixels[4]=((0, 255, 0))
    pixels[5]=((0, 0, 255))
    pixels[6]=((255, 0, 0))
    pixels[7]=((0, 255, 0))
    pixels[8]=((0, 0, 255))
    pixels[9]=((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)

