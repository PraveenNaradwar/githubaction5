import pandas as pd

print("Extract data")

data={

    "id":[101,102,103],
    "emp_name":['komal','omkar','pooja'],
    "address":['pune','mumbai','noida']
}

df=pd.DataFrame(data)
print(df)