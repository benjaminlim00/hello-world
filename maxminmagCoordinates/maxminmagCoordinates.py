'''Files and I/O: A file named xy.dat contains two columns of numbers, corresponding to
the x and y coordinates on a curve. The start of the file looks as follows, with x-coordinates
in the left column and y-coordinates in the right column:
-1.0000 -0.0000
-0.9933 -0.0087
-0.9867 -0.0179
-0.9800 -0.0274
-0.9733 -0.0374
Write a function named get_maxmin_mag(f) that takes a file object f as an argument (ie.,
f=open (‘xy.dat’,‘r’)). You must not call f=open(‘xy.dat’,‘r’) in your function.
The function should read the first column as an x coordinate and the second column
as a y coordinate. Take note that the two columns are separated by spaces (\t character).
The function then returns two Coordinate instances, where the first contains the
coordinates for the maximum magnitude, and the second contains that for the minimum
magnitude'''

import sys
import math

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    maxf = sys.float_info.min
    minf = sys.float_info.max
    
    Max = Coordinate()
    Min = Coordinate()
    s = f.readline()
    
    while s:
        s = s.split('\t')
        x, y = float(s[0]), float(s[1])
        mag = math.sqrt(x**2 + y**2)
        if mag > maxf:
            maxf = mag
            Max.x = x
            Max.y = y
        if mag < minf:
            minf = mag
            Min.x = x
            Min.y = y
        s = f.readline()
    f.close
    return Max, Min

f = open('xy.dat', 'r')
Max,Min = get_maxmin_mag(f)
print(Max.x, Max.y, Min.x, Min.y)