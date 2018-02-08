import numpy as np
import pandas as pd

#df=pd.DataFrame(pd.read_csv('name.csv',header=1))
#df=pd.DataFrame(pd.read_excel('name.xlsx'))

df=pd.DataFrame({
    'id':[1001,1002,1003,1004,1005,1006],
    'data':pd.date_range('20130102',periods=6),
    'city':['Beijing','SH','guangzhou','shenzhen','shanghai','beijing'],
    'age':[23,44,54,32,34,32],
    'price':[1200,np.nan,2133,5422,np.nan,4322]
},columns=['id','data','city','age','price'])
df.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc')
df.to_csv('excel_to_python.csv')
print(df.shape)
print(df.info())
print(df.dtypes)


