import os
import shutil
import pandas as pd


#temp locations
def dir():
    temp="temp/"
    os.makedirs(temp,exist_ok=True)

def file_process(file):
    dir()
     #need to change all things to src
    file_location = f"temp/{file.filename}"

    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)  

    df = pd.read_csv(file_location)
    df["numbers"]  = df["numbers"].astype(str)
    print(df)
    numbers = df["numbers"].tolist()
    print(numbers)

    msisdn=[]
    for number in numbers:
        msisdn.append({"mobile" : number})
    print(msisdn)

    shutil.rmtree("temp")
    return msisdn