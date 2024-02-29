import math
import numpy
import path
def fourier(func, i):
    N = len(func)
    fun = 0
    for k in range(N):
        re_func = func[k]['x']-200
        im_func = func[k]['y']-200
        phi = (2*math.pi*i*k)/N
        fun += ((re_func + im_func*1j)*(math.e**(phi*-1j)))/N
    angle = math.atan2(fun.imag,fun.real)
    length = math.sqrt(fun.imag**(2)+fun.real**(2))
    return [length, angle]
