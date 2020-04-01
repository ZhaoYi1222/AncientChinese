import pandas as pd
filename = './table_3.xlsx'
data = pd.read_excel(filename)
data = data[['year','province','city','content','ref']]
print(data.values[2,2])

print(data.values.shape)

count=0
for i in data.values:
    if(count>10):
        break
    else:
        count+=1
        for j in i:
            print(j,end=' ')
        print('\n')















