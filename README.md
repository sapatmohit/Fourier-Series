# Fourier-Series
Creating the map of India using the fourier series.
## How to run:
Run fourierTransform.py

## Indian map with 21 rotating Vectors:
![image](https://user-images.githubusercontent.com/44916178/72863878-200fd880-3d0d-11ea-83d7-9ef4de1c4b8b.png)

## Indian map with 500 rotating Vectors
![image](https://user-images.githubusercontent.com/44916178/72863867-15edda00-3d0d-11ea-823c-69ecbdb82b60.png)

## How does it work?
I have used descrete fourier transform to compute the initial angles and the length of the vectors. 
```
X(n) = 1/N*\sum_{k=0}^{N-1}f(k)*[cos(2*pi*n*k)/N)-i*sin(2*pi*n*k)/N)]
```
length of the nth vector = sqrt(real^2+imaginary^2)
``` python
length = math.sqrt(fun.imag**(2)+fun.real**(2))
```
initial angle(phase) of the nth vector = arctan(imag/real)
``` python
angle = math.atan2(fun.imag,fun.real)
```

