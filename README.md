# MATH-181 Project

Colin McDonald, Luke McEldowney, Evan Watt

This program, written in Python 3.7 using Matplotlib and NumPy, graphs the Nth Riemann sum of simple polynomials,
with a configurable a, b, and method for sampling points (currently left, middle, and right are supported.)

Functions should be entered in the form `A * x^B + B * x^C + ... + D`. For example, `5 * x^4 + 1.4 * x^3.5 - x^2 + 10`
is a valid function (note that although this program handles non-integer values properly, it does not gracefully
handle the function being undefined). In general, anything that is a valid Python expression will run fine.

a and b are floats, positive or negative. a can be greater than b, in which
case the sum will be negated (which is mathematically correct). The program also does handle the case where a = b.

n is simply the number of rectangles to use (which is what defines the nth Riemann sum). We have tested up to
n = 10000, which will plot correctly (given enough memory and time).

## Usage:
1. Make sure matplotlib and numpy are installed on your computer (`pip3 install matplotlib numpy`)
2. Invoke the program with `python3.7 gui.py`

## Known issues:
* Going from a=5 to b=0 (aka backwards) will get the right answer but the x axis will be flipped
* Doing the above w/ a sqrt (or something else that is invalid) isn't handled nicely. Python inherently tries to
    use complex numbers, which our calculations do not support (and is out of the scope of this class).
* The equations have to be written with a lot of parenthesis+operators (ex `1.5 * (x ^ (3/2))` instead of `1.5x^3/2`)
    due to how they are evaluated. Perhaps in the future we could develop more advanced parsing, but for now this is
    sufficient.