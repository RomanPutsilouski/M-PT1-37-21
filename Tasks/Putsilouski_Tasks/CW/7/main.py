import os
import csv
import json
import pickle
# print(f"current directory is {os.getcwd()}")


# os.mkdir("test") - создает директории
# os.makedirs("test\\test ") -  создает директории c вложенными

# d = os.path.join("pach","pach") - написали папки через запятую

# os.remove("text\\neqfdsf.txt") - удаляет файл




with open("audi.csv", "w") as csvfile:
    l = csv.writer(csvfile)
    l.writerow(["Model", "year", "Horspower","Engine Size"])
    l.writerow(["80 1.6 Specs","1989","69","1595 cm3 (97,3 cu-in)"])
    l.writerow(["80 1.6 Specs","1993","102", "1595 cm3 (97,3 cu-in)"])
    l.writerow(["80 2.0 16v Quattro Specs","1990","140", "1984 cm3 (97,3 cu-in)"])
print(f"current directory is {os.getcwd()}")
csvfile.close()






with open("audi.json", "w") as write_file:
    with open("audi.csv", "r") as csvfile:
        a = csv.reader(csvfile)
        for i in a:
            json.dump(i,write_file)
write_file.close()

with open("audi.txt", "wb") as j:
    with open("audi.csv", "r") as csvfile:
        a = csv.reader(csvfile)
        for i in a:
            print(type(i))
            pickle.dump(i,j)
