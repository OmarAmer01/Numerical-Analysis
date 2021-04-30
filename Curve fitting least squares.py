import numpy as np
import matplotlib.pyplot as plt
import sympy as s


def sep():
    print(100 * '-')


print("Omar Tarek Ahmed Mohamed Ali Amer")
print("ID: 1180004")
print("Curve Fitting: Q12")
sep()
#########################################
X = []
Y = []
yapp = []
yMinusYapp = []
yMinusAvg = []
xSymb, ySymb, aSymb, bSymb = s.symbols("x y a b")

choice = input("Solve Demo Question (Sheet Question 12) [y/n]? :")
if choice == "y":
    x = "0.2 0.5 0.8 1"
    y = "102 22 20 25"
    inputXpr = s.sympify("((a*x^2 +b/x))^2")
    print("y = ((a*x^2 +b/x))^2\n"
          "x*sqrt(y) = a1*x^3 + a0")
    yExpr = s.sympify("x * sqrt(y)")
    xExpr = s.sympify("x^3")
    sep()
else:
    x = input("Input the values of x separated by spaces: ")
    y = input("Input the values of y separated by spaces: ")
    print("Unlinearized equation: y = f(x)")
    inputXpr = s.sympify(input("f(x) [in terms of a, b and x] = "))
    print("Linearized Equation: Y = a0 + a1X")
    yExpr = s.sympify(input("Enter Y in terms of ""x"" and ""y"": "))
    xExpr = s.sympify(input("Enter X in terms of ""x"": "))

x = x.split(" ")

for i in range(len(x)):
    x[i] = float(x[i])

y = y.split(" ")

for i in range(len(y)):
    y[i] = float(y[i])

if len(y) != len(x):
    print("Size Mismatch!! [Exiting...]")
    exit(-1)

for i in range(len(x)):
    # X.append(x[i] ** 3)
    X.append(xExpr.subs(xSymb, x[i]).evalf())

for i in range(len(y)):
    Y.append(yExpr.subs(ySymb, y[i]).subs(xSymb, x[i]).evalf())

phiMat = np.array([[len(x), sum(X)], [sum(X), sum(i * i for i in X)]], dtype=np.float_)
xyMat = np.array([[sum(Y)], [np.dot(X, Y)]], dtype=np.float_)

sol = np.linalg.solve(phiMat, xyMat)
a0 = sol[0]
a1 = sol[1]

for i in range(len(x)):
    yapp.append(inputXpr.subs([(aSymb, float(a1)), (bSymb, float(a0)), (xSymb, x[i])]).evalf())
for i in range(len(y)):
    yMinusYapp.append(y[i] - yapp[i])

yAvg = np.average(y)
for i in range(len(y)):
    yMinusAvg.append(y[i] - yAvg)

print("%-21s %-10s %-15s " % ("Phi", "a", "xy"))
print("%-10f %-10f %-10s %-10f" % (phiMat[0][0], phiMat[0][1], "a0", xyMat[0]))
print("%-10f %-10f %-10s %-10f" % (phiMat[1][0], phiMat[1][1], "a1", xyMat[1]))

print(f"\na0 = {a0}\n"
      f"a1 = {a1} ")

sep()

headings = ["x", "y", "X", "Y", "y approximate", "y - y approximate", "y - Avg y"]
print("%-10s %-10s %-10s %-10s %-17s %-20s %-20s" % (headings[0], headings[1], headings[2],
                                                     headings[3], headings[4], headings[5], headings[6]))
for i in range(len(x)):
    print("%-10f %-10f %-10f %-10f %-17f %-20f %-20f" % (x[i].__round__(4), y[i].__round__(4), X[i].__round__(4), Y[i],
                                                         yapp[i], yMinusYapp[i], yMinusAvg[i]))
sep()
st = sum(i * i for i in yMinusAvg)
sr = sum(i * i for i in yMinusYapp)
r = (((st - sr) / st) ** 0.5) * 100
print("Standard true error (st) =       %f\nStandard regression error (sr) = %f " % (st, sr))
print("Correlation factor (r) =         %f %%" % r)

orig = plt.plot(x, y)
app = plt.plot(x, yapp)
plt.show()
