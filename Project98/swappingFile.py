def openFile():
    data_a = input("Enter File name here: ") 
    data1 = open(data_a, "r")
    print(data1)
openFile()