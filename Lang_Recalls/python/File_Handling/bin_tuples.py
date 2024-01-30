import pickle
#Storing records as list
f = open("Bin_Tuples.dat", "wb")
Rec = []
while True:
    roll = int(input("Roll No.: "))
    name = input("Enter name: ")
    R = [roll, name]
    Rec.append(R)
    ch = input("Do you want to enter more records? (y/n)")
    if ch in 'nN':
        pickle.dump(Rec, f) #Dumps the entire list/ Writing binary file
        f.close()
        break

fr = open("Bin_Tuples.dat", "rb")
read = pickle.load(fr) #Loads the entire list/ Reading binary file
print(read)
fr.close()