import csv

print("")
print("The Data Centralizer")
print("")
print("Hello. I'm The Data Centralizer. Given here is a list of height and weights of and whole population aged above 18. Hope you enjoy visualizing and plotting your graph!")
print("")
print('What data would you like to view. The Heights or the Weights:-')
print("")
print("Heights")
print("Weights")
print("")
data = input("Please enter your choice:- ")
print("")
if(data == "Heights"):

        
    print("Choose your calculation process:-")
    print("")
    print("Mean")
    print("Median")
    print("Mode")
    print("")
    calc = input("Please enter you choice:-")
    print("")
    if(calc == "Mean"):
        
        #mean
        with open("index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][1]
            new_values.append(float(num))

        n = len(new_values)
        sum = 0

        for i in new_values:
            sum += i

        mean = sum/n
        print("The mean of the heights is:" + str(mean))
    
    if(calc == "Median"):

        #median
        with open("Index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][1]
            new_values.append(float(num))

        n = len(new_values)

        new_values.sort()

        if(n%2 == 0):
            m1 = new_values[n//2]
            m2 = new_values[n//2-1]
            median = (m1+m2)/2

        else:
            median = new_values[n//2]

        print("Median of the heights is :", median)

    if(calc == "Mode"):
        

        #mode
        with open("Index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][1]
            new_values.append(float(num))

        from collections import Counter

        data = Counter(new_values)

        interval = {"50-60": 0,  "60-70" : 0, "70-80" : 0}

        for height, occurence in data.items():
            if(50<float(height)<60):
                interval["50-60"] += occurence

            elif(60<float(height)<70):
                interval["60-70"] += occurence

            elif(70<float(height)<80):
                interval["70-80"] += occurence

        modeHeight, modeOccurence = 0,0

        for range, occurence in interval.items():
            if(occurence>modeOccurence):
                modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

        mode = float((modeRange[0] + modeRange[1] ) / 2)
        print(f"mode is : {mode:2f}")


if(data == "Weights"):
             
    print("Choose your calculation process:-")
    print("")
    print("Mean")
    print("Median")
    print("Mode")
    print("")
    calc = input("Please enter you choice:-")
    print("")
    if(calc == "Mean"):
        
        #mean
        with open("index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][2]
            new_values.append(float(num))

        n = len(new_values)
        sum = 0

        for i in new_values:
            sum += i

        mean = sum/n
        print("The mean of the weights is:" + str(mean))
        print("")
    
    if(calc == "Median"):

        #median
        with open("Index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][2]
            new_values.append(float(num))

        n = len(new_values)

        new_values.sort()

        if(n%2 == 0):
            m1 = new_values[n//2]
            m2 = new_values[n//2-1]
            median = (m1+m2)/2

        else:
            median = new_values[n//2]

        print("Median of the weights is :", median)
        print("")

    if(calc == "Mode"):
        

        #mode
        with open("Index.csv", newline = "") as index:
            data = csv.reader(index)
            values = list(data)

        values.pop(0)

        new_values = []

        for i in range(len(values)):
            num = values[i][2]
            new_values.append(float(num))

        from collections import Counter

        data = Counter(new_values)

        interval = {"100-110": 0,  "110-120" : 0, "120-130" : 0, "130-140" : 0, "140-150" : 0, "150-160" : 0}

        for weight, occurence in data.items():
            if(100<float(weight)<110):
                interval["100-110"] += occurence

            elif(110<float(weight)<120):
                interval["110-120"] += occurence

            elif(120<float(weight)<130):
                interval["120-130"] += occurence

            elif(130<float(weight)<140):
                interval["130-140"] += occurence

            elif(140<float(weight)<150):
                interval["140-150"] += occurence

            elif(150<float(weight)<160):
                interval["150-160"] += occurence

        modeWeight, modeOccurence = 0,0

        for range, occurence in interval.items():
            if(occurence>modeOccurence):
                modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

        mode = float((modeRange[0] + modeRange[1] ) / 2)
        print(f"Mode of the weights is : {mode:2f}")
        print("")

print("")
print("Thanks for using The Data Centralizer! Hope you liked it.")
print("")