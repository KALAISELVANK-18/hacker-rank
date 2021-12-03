import pandas as pd
import matplotlib as mt
data1={'Name':['mercy','dds'],'age':[3,8]}
df1=pd.DataFrame(data1,index=['k0',['k1']])
frames=[df1]
res=pd.concat(frames,ignore_index=True)
print(df1.head(2))
print(res)


