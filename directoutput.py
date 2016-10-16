import csv
from FormattedData import FormatData

def SaveData(Filename = "", DataList = []):
        with open(filename, "a", newline= '\n') as csvfile:
            DataWriter = csv.writter(csvfile,delimiter='\n',quotechar=" ")
            DataWriter.writerow(DataList)
            csvfile.close()
            print("Data Saved")
    
mylist = SaveData()
