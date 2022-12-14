import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
from sklearn.linear_model import LinearRegression

#12개월마다 포문을 돌렸으니 12개씩 띄워서 저장한다
#csv파일 값만 있기때문에 연도,월 요소값을 넣어 데이터 프레임 생성
Year=[]
Month=[]
Category=[]

for i in range(1970,2020):
    for j in range(0,36):
        Year.append(i)
        if j < 12:
            m=j+1
            Month.append(m)
            Category.append('최고기온')
        elif j<24:
            m=j-11
            Month.append(m)
            Category.append('최저기온')
        elif j<36:
            m=j-23
            Month.append(m)            
            Category.append('강수량')
csv=pd.read_csv('jeju.csv',sep=',')
df = pd.DataFrame({'Year':Year[:],
                   'Month':Month[:],
                   'Elemente':Category[:],
                   'Value':csv['0']})


grpY_year = df.groupby(['Year','Elemente'])[['Value']].mean()
pd.options.display.float_format = '{:.3f}'.format
avg_H=grpY_year.xs('최고기온',level='Elemente')
avg_L=grpY_year.xs('최저기온',level='Elemente')
avg_P=grpY_year.xs('강수량',level='Elemente')


plt.style.use('default')
plt.rcParams['figure.figsize'] = (9, 5)
plt.rcParams['font.size'] = 12
x=np.arange(1970,2020)
y1 = avg_H.iloc[:,0]
y2 = avg_L.iloc[:,0]
y3 = avg_P.iloc[:,0]
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='purple',label='Highest temp', markersize=1, linewidth=2, alpha=1)
ax1.plot(x, y2, color='orange',label='Lowest temp', markersize=1, linewidth=2, alpha=1)
ax1.set_ylim(0, 40)
ax1.set_xlabel('Year')
ax1.set_ylabel('℃')
ax1.legend(loc=2)
ax1.tick_params(axis='both', direction='in')
ax2 = ax1.twinx()
ax2.bar(x, y3, color='blue', label='Precipitation', alpha=0.3, width=0.7)
ax2.set_ylim(0, 230)
ax2.set_ylabel('mm')
ax2.tick_params(axis='y', direction='in')
ax2.legend(loc=1)
plt.title("Temperatures and Precipitation in Jeju",size = 15,fontweight='bold')
plt.show()


years_1970s=grpY_year.iloc[list(range(30))]
years_1980s=grpY_year.iloc[list(range(30,60))]
years_1990s=grpY_year.iloc[list(range(60,90))]
years_2000s=grpY_year.iloc[list(range(90,120))]
years_2010s=grpY_year.iloc[list(range(120,150))]
grp_years_1970s = years_1970s.groupby(['Elemente'])[['Value']].mean()
grp_years_1980s = years_1980s.groupby(['Elemente'])[['Value']].mean()
grp_years_1990s = years_1990s.groupby(['Elemente'])[['Value']].mean()
grp_years_2000s = years_2000s.groupby(['Elemente'])[['Value']].mean()
grp_years_2010s = years_2010s.groupby(['Elemente'])[['Value']].mean()
decade_years = pd.concat([grp_years_1970s,grp_years_1980s
                         ,grp_years_1990s,grp_years_2000s,grp_years_2010s])
Years_list=['1970s','1970s','1970s',
           '1980s','1980s','1980s',
           '1990s','1990s','1990s',
           '2000s','2000s','2000s',
           '2010s','2010s','2010s',]
decade_years.reset_index(drop = False,inplace=True)
decade_years.insert(0,"Years",Years_list[:],True)
decade_avg_p=decade_years.iloc[0:18:3]["Value"]
decade_avg_h=decade_years.iloc[1:18:3]["Value"]
decade_avg_l=decade_years.iloc[2:18:3]["Value"]


plt.style.use('default')
plt.rcParams['figure.figsize'] = (8, 4)
plt.rcParams['font.size'] = 12
x=list(range(1970,2020,10))
y1 = decade_avg_l
y2 = decade_avg_h
y3 = decade_avg_p
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='grey',label='Lowest temp', markersize=1, linewidth=3, alpha=1)
ax1.plot(x, y2, color='yellow',label='Highest temp', markersize=1, linewidth=3, alpha=1)
ax1.set_ylim(11, 22)
ax1.set_xlabel('Year')
ax1.set_ylabel('℃')
ax1.legend(loc=2)
ax1.tick_params(axis='both', direction='in')
ax2 = ax1.twinx()
ax2.bar(x, y3, color='blue', label='Precipitation', alpha=0.3, width=1.5)
ax2.set_ylim(0, 230)
ax2.set_ylabel('mm')
ax2.tick_params(axis='y', direction='in')
ax2.legend(loc=1)
plt.title("Temperature and precipitation in Jeju",size = 15,fontweight='bold')
plt.show()



grp_month = df.groupby(['Month','Elemente'])[['Value']].mean()
avgH_month =grp_month.xs('최고기온',level='Elemente')
avgL_month =grp_month.xs('최저기온',level='Elemente')
avgP_month =grp_month.xs('강수량',level='Elemente')
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8, 4)
plt.rcParams['font.size'] = 12
x=list(range(1,13))
y1 = avgH_month.iloc[:,0]
y2 = avgL_month.iloc[:,0]
y3 = avgP_month.iloc[:,0]
fig, ax3 = plt.subplots()
ax3.plot(x, y1, color='red',label='Highest temp', markersize=1, linewidth=3, alpha=1)
ax3.plot(x, y2, color='yellow',label='Lowest temp', markersize=1, linewidth=3, alpha=1)
ax3.set_ylim(-5, 35)
ax3.set_xlabel('Month')
ax3.set_ylabel('℃')
ax3.legend(loc=2)
plt.xticks(np.arange(0, 14, 1),
           labels=['','1', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', '11','12',''])
ax3.tick_params(axis='both', direction='in')
ax4 = ax3.twinx()
ax4.bar(x, y3, color='blue', label='Precipitation', alpha=0.3, width=0.8)
ax4.set_ylim(0, 500)
ax4.set_ylabel('mm')
ax4.tick_params(axis='y', direction='in')
ax4.legend(loc=1)
plt.title("Temperature and precipitation in Jeju",size = 15,fontweight='bold')
plt.show()

MH_data = avg_H.reset_index()
X=MH_data["Year"]
y=MH_data["Value"]

line_fitter = LinearRegression()
line_fitter.fit(X.values.reshape(-1,1), y)
line_fitter.predict([[2022]])
print(line_fitter.predict([[2022]]))
plt.plot(X, y, 'X')
plt.plot(X,line_fitter.predict(X.values.reshape(-1,1)))
plt.show()