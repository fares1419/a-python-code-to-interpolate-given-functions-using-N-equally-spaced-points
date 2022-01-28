import numpy as np
import math
import matplotlib.pyplot as plt




#for cox(pi*x)

x = np.linspace(0, 1.5, 3)
y = np.cos(math.pi * x)

x_new = np.linspace(0, 1.5, 300)
y_new = np.cos(math.pi * x_new)
fx=[0 for i in range(len(x_new))]


def lagrange(x,x_new,y):
 for w in range(len(x_new)):
    xp = x_new[w]
    yp = 0
    for i in range(len(x)):
        p = 1

        for j in range(len(x)):
            if j != i:
             p *= ((xp - x[j]) / (x[i] - x[j]))


        yp+= y[i] * p

    fx[w]=yp
lagrange(x,x_new,y)
plot1 = plt.figure(1)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['cos πx with n=3 and x∈[0,1.5] ', 'interpolated function'], loc='best')
#end
x = np.linspace(-5, 5, 4)

y = np.cos(math.pi * x)

x_new = np.linspace(-5, 5, 300)

y_new = np.cos(math.pi * x_new)
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot2 = plt.figure(2)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function (cos πx with n=4 and x∈[-5,5])', 'interpolated function'], loc='best')
#end2
x = np.linspace(-5, 5, 5)
y = np.cos(math.pi * x)

x_new = np.linspace(-5, 5, 300)
y_new = np.cos(math.pi * x_new)

fx=[0 for i in range(len(x_new))]

lagrange(x,x_new,y)

plot3 = plt.figure(3)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function (cos πx with n=5 and x∈[-5,5]', 'interpolated function'], loc='best')
#end 3
x = np.linspace(-5, 5, 8)
y = np.cos(math.pi * x)

x_new = np.linspace(-5, 5, 300)

y_new = np.cos(math.pi * x_new)
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)

plot4 = plt.figure(4)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function (cos πx with n=8 and x∈[-5,5])', 'interpolated function'], loc='best')
#end4
x = np.linspace(-5, 5, 10)
y = np.cos(math.pi * x)

x_new = np.linspace(-5, 5, 300)
y_new = np.cos(math.pi * x_new)
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot5 = plt.figure(5)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function (cos πx with n=10 x∈[-5,5])', 'interpolated function'], loc='best')




#end cosx
#يلاحظ أنه كلما زادت الn
# زادت نعومة القراف


# 1/1+(25x^2)
#مطابقة تماما للinterpolation
#لست متاكد من الحل حتى الان

x = np.linspace(-2, 2, 3)
y = 1/(1+(25*(x*x)))

x_new = np.linspace(-2, 2, 300)
y_new = 1/(1+(25*(x_new*x_new)))
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot6 = plt.figure(6)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function 1/1+(25x^2) with n=3 x∈[-2,2])', 'interpolated function'], loc='best')
#end


x = np.linspace(-2, 2, 5)
y = 1/(1+(25*(x*x)))

x_new = np.linspace(-2, 2, 300)
y_new = 1/(1+(25*(x_new*x_new)))
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot7 = plt.figure(7)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function 1/1+(25x^2) with n=5 x∈[-2,2])', 'interpolated function'], loc='best')

#end2
x = np.linspace(-2, 2, 10)
y = 1/(1+(25*(x*x)))

x_new = np.linspace(-2, 2, 300)
y_new = 1/(1+(25*(x_new*x_new)))
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot8 = plt.figure(8)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function 1/1+(25x^2) with n=10 x∈[-2,2])', 'interpolated function'], loc='best')
#end of  1/(1+(25*(x*x))


#sinx/x

x = np.linspace(-3, 3, 3)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(-3, 3, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot9 = plt.figure(9)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=3 x∈[-3,3])', 'interpolated function'], loc='best')
#end2

x = np.linspace(-2, 2, 10)
y = 1/(1+(25*(x*x)))

x_new = np.linspace(-2, 2, 300)
y_new = 1/(1+(25*(x_new*x_new)))
fx=[0 for i in range(len(x_new))]
lagrange(x,x_new,y)
plot8 = plt.figure(8)
plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.plot(x_new,fx)
plt.legend(['original function 1/1+(25x^2) with n=10 x∈[-2,2])', 'interpolated function'], loc='best')
#end of  1/(1+(25*(x*x))


#sinx/x

x = np.linspace(-3, 3, 5)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(-3, 3, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot10 = plt.figure(10)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=5 x∈[-3,3])', 'interpolated function'], loc='best')
#end

x = np.linspace(-10, 10, 5)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(-10, 10, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot11 = plt.figure(11)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=5 x∈[-10,10])', 'interpolated function'], loc='best')
#end2
x = np.linspace(-3, 3, 3)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(-3, 3, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot12 = plt.figure(12)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=3 x∈[-3,3])', 'interpolated function'], loc='best')
#end3
x = np.linspace(-10, 10, 11)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(-10, 10, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot13 = plt.figure(13)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=11 x∈[-10,10])', 'interpolated function'], loc='best')
#end4

x = np.linspace(0, 10, 6)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(0,10, 300)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot14 = plt.figure(14)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=6 x∈[0,10])', 'interpolated function'], loc='best')

#end5
x = np.linspace(0, 10, 10)
y =[0 for i in range(len(x))]
for i in range(len(x)):
    if (x[i] != 0):
     y[i] = np.sin(x[i])/x[i]
    else:
     y[i]=1

x_new = np.linspace(0,10, 500)
y_new =[0 for i in range(len(x_new))]
for i in range(len(x_new)):
    if (x_new[i] != 0):
      y_new[i] = np.sin(x_new[i])/x_new[i]
    else:
      y_new[i]=1

fx = [0 for i in range(len(x_new))]
lagrange(x, x_new, y)
plot15 = plt.figure(15)
plt.scatter(x, y)
plt.plot(x_new, y_new)
plt.plot(x_new, fx)
plt.legend(['original function sin(x)/x with n=10 x∈[0,10])', 'interpolated function'], loc='best')
plt.show()