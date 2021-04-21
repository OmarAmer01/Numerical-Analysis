import numpy as np


def reArrange(xArr, yArr, val):
    sortedX = []
    sortedY = []
    arrPriority = []
    for i in range(len(xArr)):
        diff = abs(xArr[i] - val)
        element = (xArr[i], diff, yArr[i])
        arrPriority.append(element)

    arrPriority.sort(key=lambda x: x[1])
    for i in range(len(arrPriority)):
        sortedX.append(arrPriority[i][0])
        sortedY.append(arrPriority[i][2])
    return sortedX, sortedY


def divDiffTable(xArr, yArr, order):
    div = []
    diffTable = []
    newOrder = order
    if order >= len(xArr):
        newOrder = len(xArr) - 1
    for i in range(newOrder):  # calculates the nth divided difference

        if len(diffTable) == 0:
            newYarr = yArr
        else:
            newYarr = diffTable[i - 1]

        for j in range(len(newYarr)-1):  # calculates the values themselves
            divDiff = (newYarr[j + 1] - newYarr[j]) / (xArr[j + i + 1] - xArr[j])
            div.append(divDiff)
        diffTable.append(div)
        div = []
    return diffTable


def newtonInterp(xArr, yArr, val, order=np.inf):
    table = reArrange(xArr, yArr, val)
    x = table[0]
    y = table[1]
    result = 0
    subResult = 1
    if order == np.inf:
        maxOrder = len(xArr) - 1
    else:
        maxOrder = order 

    diffTable = divDiffTable(x, y, maxOrder)
    diffTable.insert(0,y)
    for i in range(len(diffTable)):
        for j in range(i):
            subResult *= val - x[j]
        result += subResult * diffTable[i][0]
        subResult = 1
    return result

def newtonResidual(xArr, yArr, val, order):
    maxOrderVal = newtonInterp(xArr, yArr, val)
    lesserOrderVal = newtonInterp(xArr, yArr, val, order)
    return maxOrderVal - lesserOrderVal

def quadSpline(xArr,yArr):
    contNo = len(xArr) - 2
    for i in range(len(xArr) - 1): # print the limited value equations
        print(f"{y[i]} = a{i}({x[i]})^2 + b{i}({x[i]}) + c{i}")
        print(f"{y[i+1]} = a{i}({x[i+1]})^2 + b{i}({x[i+1]}) + c{i}")

    for i in range(contNo):
        ip = i + 1
        print(f"2a{i}({x[i+1]}) + b{i} = 2a{ip}({x[i+1]}) + b{ip} ")
    
    print("a0 = 0")
 

x = []
y = []

while True:
    print("*********************")
    print("1- Solve using given inputs [SOLVE QUESTION 3, DEMO EXAMPLE]\n2- Estiamte a value [General Newton Interpolation, Quadratic spline equations for a given set of values]")
    choice = input("What do you want to do? [Enter Number]: ")
    if choice == "1":

        inputArr = "15 45 75 105 135 0.9659 0.7071 0.2588 -0.2588 -0.7071"
        inputArr = inputArr.split(" ")

        x = inputArr[:int(len(inputArr) / 2)]
        for i in range(len(x)):
            x[i] = np.longdouble(x[i])

        x = np.deg2rad(x)

        y = inputArr[int(len(inputArr) / 2):]
        for i in range(len(y)):
            y[i] = np.longdouble(y[i])

        table = [(x[i], y[i]) for i in range(0, len(x))]
        

        print("X                            Y")
        for i in range(len(table)):
            print(table[i])
        print("\n\n")
        print("P3(85): ",newtonInterp(x,y,np.radians(85),3))
        print("R3(85): ",newtonResidual(x, y, np.radians(85),3))
        print("Root:   ",newtonInterp(y[1:],x[1:],0))
        print("Quadratic Spline Equations: ")
        quadSpline(x, y)
        continue

    elif choice =="2":
        inputArr = input("Enter the values of x then the values of y separated by spaces: ")
        inputArr = inputArr.split(" ")
        x = inputArr[:int(len(inputArr) / 2)]
        y = inputArr[int(len(inputArr) / 2):]

        for i in range(len(x)):
            x[i] = np.longdouble(x[i])

        for i in range(len(y)):
            y[i] = np.longdouble(y[i])

        radCheck = input("Convert X to radian? [y/n]: ")
        while not(radCheck == "y" or radCheck == "Y" or radCheck == "n" or radCheck == "N"):
            radCheck = input("Convert X to radian? [y/n]: ")
        
        if radCheck == "y" or radCheck == "Y":
            x = np.deg2rad(x)

    table = [(x[i], y[i]) for i in range(0, len(x))]
    print("X                            Y")
    for i in range(len(table)):
        print(table[i])

    val = input("Enter the value you want to estimate: [TYPE 'MENU' TO GO BACK TO THE MAIN MENU, 'R' for roots, 'S' for quadratic spline equations. ]")
    while not(val.lower() == "menu"):
        if val.lower() == "r":
            print("Root: {:f}".format(newtonInterp(y, x, 0)))

        elif val.lower() == "s":
            quadSpline(x, y)

        elif val.isnumeric():
            print("Y({:f}) = {:f}".format(float(val), newtonInterp(x, y, float(val))))
        
        val = input("Enter the value you want to estimate: [TYPE 'MENU' TO GO BACK TO THE MAIN MENU, 'R' for roots, 'S' for quadratic spline equations. ]")
    continue
