# HD44780-Python-Module
Python 3.x to use with the HD44780 LCD controller. Testing done using a 16x2 LCD and 20x4 LCD, both from Adafruit and a Pi3

This requires the RPI.GPIO module.

Also included is an example file which demonstrates some of the base functions.

Connections I used between the Pi and LCD are as follows:

LCD Gnd to Pi Gnd

LCD VDD to Pi 5V

LCD V0 to middle pin of a 10k Potentiometer - Potentiometer required for contrast 

10k Potentiometer outer leg 1 to Pi Gnd 

10k Potentiometer outer leg 2 to Pi 5V

LCD RS to Pi 4

LCD RW to Pi 17 when used, otherwise to Pi Gnd

LCD E to Pi 27

LCD DB0-DB3 - not connected

LCD DB4 to Pi 5

LCD DB5 to Pi 6

LCD DB6 to Pi 13

LCD DB7 to Pi 19

LCD BL1 to Pi 5V - Backlight power

LCD BL2 to 160 ohm resistor which connects to Pi Gnd


Current functions include:

- initialization - LCD = HD44780.HD44780(rs, rw, e, dbList = [], rows = 1, characters = 16, mode = 0, font = 0)
- rs, rw, e are the pi pin numbers to connect to the LCD rs, rw & e pins
- rw is optional - if not using, assign to -1 and tie LCD rw pin to Pi Gnd
- dbList is a list of pi pin numbers to connect to the LCD/HD44780 DB0-DB7 pins
- rows - number of rows on the LCD display, only 1, 2 & 4 are currently valid
- characters - number of characters per row on the LCD display
- mode - 0 for 4 bit mode, 1 for 8 bit mode
- font - 0 for 5x8 dot font, 1 for 5x10 dot font

- display_string(msg)
- set_cursor(row, column)
- blink(blink = True)
- cursor(cursor = True)
- display(display = True)
- scroll_left(numSpaces = 1, delay = 0)
- scroll_right(numSpaces = 1, delay = 0)
- cursor_left(numSpaces = 1, delay = 0)
- cursor_right(numSpaces = 1, delay = 0)
- clear_display()
- return_home()

- set_display(on = 0, cursor = 0, blinking = 0)
- set_entry_mode(ID = 1, displayShift = 0)

Notes:

The HD44780 can be connected in 4 or 8 bit modes. In 8 bit mode, all 8 of DB0-DB7 are used whereas in 4 bit mode
only DB4-DB7 are used.  If using 4 bit mode, only a list of the 4 pi pins used is required to be passed in the dbList
for initialization, see example below.

I haven't tried reading data back from the HD44780, if you try, consider using a logic level shifter as
the HD44780 will output 5V which could fry your pi, then you'd cry. As such if you don't plan on reading
info back from the HD44780 then there really is no need to use the RW pin.  

To not use the RW pin, connect the RW pin on the HD44780/LCD to Pi Gnd and assign it to -1 in the initialization
statement, i.e. LCD = HD44780.HD44780(4, -1, 27, [5,6,13,19], rows = 2, characters = 16, mode = 0, font = 0)

The HD44780 data sheet is useful and can be downloaded from the Adafruit website.
