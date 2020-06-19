import csv
import os
class CsvReader:
    def __init__(self,filename):
        print(f'file directory: {os.path.abspath(os.path.join("./Package/tests",filename))}')
        self.filename = os.path.abspath(os.path.join('./Package/tests',filename))
    def readFile(self):
        newList = list()
        with open(self.filename,mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                try:
                    newList.append((row['Value 1'],row['Value 2'], row['Result']))
                except KeyError:
                    newList.append((row['Value 1'], row['Result']))
            return newList
        
                
                
        