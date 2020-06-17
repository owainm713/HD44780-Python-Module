#!/usr/bin/env python3

"""HD44780example, example program to use with the HD44780.py module

created June 11, 2020 OM
modified June 11, 2020 OM """

"""
Copyright 2020 Owain Martin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import HD44780
import time

# set 16 character x 2 row LCD screen with rw pin, 4 bit mode
LCD = HD44780.HD44780(4, 17, 27, [5,6,13,19], rows = 2, characters = 16, mode = 0, font = 0)

# set 16 character x 2 row LCD screen without rw pin, 4 bit mode
#LCD = HD44780.HD44780(4, -1, 27, [5,6,13,19], rows = 2, characters = 16, mode = 0, font = 0)

# set 20 character x 4 row LCD screen without rw pin, 4 bit mode
#LCD = HD44780.HD44780(4, -1, 27, [5,6,13,19], rows = 4, characters = 20, mode = 0, font = 0)

# set 20 character x 4 row LCD screen with rw pin, 8 bit mode
#LCD = HD44780(4, 17, 27, [16,20,21,26,5,6,13,19], rows = 4, characters = 20, mode = 1, font = 0)

LCD.display_string("glue")
time.sleep(1)
LCD.display(False)              # turn display off
time.sleep(2)
LCD.display()                   # turn display on
LCD.set_cursor(2,1)             # move cursor to 2nd row, 1st position
LCD.display_string("stick")
time.sleep(2)

LCD.blink()         # blink cursor position
time.sleep(2)
LCD.blink(False)    # turn blinking off
time.sleep(2)

LCD.cursor(False)   # turn cursor off
time.sleep(2)
LCD.cursor()        # turn cursor on
time.sleep(2)

LCD.scroll_right(4, 0.5) # scoll display right with 0.5s delay between steps
time.sleep(1)
LCD.scroll_left(4, 0.5) # scoll display left with 0.5s delay between steps
time.sleep(1)
LCD.cursor_left(2) # move cursor left
time.sleep(2)
LCD.cursor_right(2) # move cursor right
time.sleep(2)

LCD.clear_display()

