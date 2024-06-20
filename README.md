# Personal Game Font

This is a custom font created using the **PYGAME** module for Python. There are 2 files that you must integrate into your project in order to use this font.
`gamefont.py`
`pixel.py`

(The good news is that you can use `pixel.py` to draw objects using the same method as I did to create my font face)

## Reason for this Module
To bypass Pygame's convoluted font/text object calls and functionality, to simplify and make it better.

## About the Maintenance
This will be updated as needed.

## How to Use
### 1. Import the module
You must use the following:
```Python
from gamefont import GUI
```
at the start of your .py code file to implement.

### 2. Create your GUI font object
The `GUI` class takes **1 mandatory argument** and 2 optional arguments.
#### Mandatory Call Example
```Python
fontObj = GUI(PygameSurface)
```
This keeps everything at default: white color font, pixel size 1

#### Optional Call Example
```Python
fontObj = GUI(PygameSurface, color = (255, 255, 0), size = 3)
```
Aside from the mandatory Pygame surface call, this creates a yellow fontface with a pixel size of 3

#### CAUTION
The 'size' is **NOT** the font size (for example, 12pt. font - if you declare `size = 12` you're going to have one big mess of a font!)
Instead, a 12-point font might be `size = 2`. The spacing is in multiples of 5 and 7, so the code reflects this. Sizes 1 through 3 are recommended
depending on the screen resolution of your game. For larger resolutions, you can use probably up to 10 or so).

### 3. The `gPrint()` function
Within the `GUI` class is a `gPrint()` function. This allows you to print your strings to the screen. It takes up to 3 args: **1 mandatory, 2 optional**
```Python
fontObj.gPrint("Hello World")
```
Prints `Hello World` at the **top-left** corner of the screen (defaults to x0, y0).

#### Args
```Python
fontObj.gPrint(string, x = 0, y = 0)
```

### Your Own Customization
You can add and change the design of the letters by editing the array/lists in `gamefont.py`

Make your changes in the following:
```Python
self.numbers_blueprint[]
self.letters_blueprint[]
```

Then, scroll down to `self.font_dict{}` and line-up your newly added characters to dictionary. 
This will correspond with the characters you type in your `string` arg for `gPrint` and generate your
custom font onto the screen.


### License
This is open-source with creative commons By 4.0 ![alt text](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png)
The following is granted and requested:
- Change, Edit, or Add however and whatever you wish
- You can even use this for **commercial use** (monetization is OK)
- Like Blockbuster used to say, *Please be kind and shout me out in the credits of your project, **ESPECIALLY** monetized ones*
  
The license explanation in legalese, is here: https://creativecommons.org/share-your-work/cclicenses/

### Contact
If you like this font but don't know how to edit it yourself, that's okay - if you want to add some things to it but don't have the
technical knowhow to figure it out, please send me a message at mikesdump@protonmail.ch and I will be more than happy to look into it (*so long as I **can** do it, that is*)


### One last thing
Have fun!
