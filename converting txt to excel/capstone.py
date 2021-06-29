import os
import csv
import pandas

def toDict(key_list):
    data=[]
    for file in os.listdir():
        if file.endswith("txt"):
            with open (file) as txt_file:
                txt={}
                for key,info in zip(key_list,txt_file):
                    txt[key]=info.strip("\n")
                data.append(txt)
    return data

def toCsv(data,key_list,file):
    with open (file,'w',newline='') as f1:
        csv_file=csv.DictWriter(f1,fieldnames=key_list)
        csv_file.writeheader()
        csv_file.writerows(data)

def toExcel(file1,file2):
    csv_file=pandas.read_csv(file1)
    excel_file=pandas.ExcelWriter(file2)
    csv_file.to_excel(excel_file,index=False)
    excel_file.save()

if __name__=='__main__':
    key_list=["Name","Phone","Country"]
    data=toDict(key_list)
    print(data)
    toCsv(data,key_list,"capstone.csv")
    toExcel("capstone.csv","capstone.xlsx")
