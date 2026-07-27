'''from datetime import datetime
current_ = datetime.now()
print(current_)
print(current_.strftime('%y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))
print(current_.strftime('%H'))
#print(current_.strftime('%I'))
print(current_.strftime('%M'))
print(current_.strftime('%S'))
print(current_.strftime('%p'))

import numpy as np
arr1=np.array([[1,2,3,4,5],[23,45,67,32,12]])
print(arr1)
print(arr1.reshape(5,2))


import pandas as pd
Data=pd.Series([2000,7000,100000],['charger','mobile','laptop'])
print(Data)


import pandas as pd
df={
    "product":['Laptop','charge','mobile'],
    "Brand":['MAC','Realme','vivo'],
    'price':[1000,500,4000]
    }
so=pd.DataFrame(df)
print(so)'''
import calendar
print(calendar.month(2026,7))
print(calendar.calendar(2026))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2026))
