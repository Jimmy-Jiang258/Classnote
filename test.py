import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
# area=pd.Series({'California': 423967, 'Texas': 695662,'New York': 141297, 'Florida': 170312,'Illinois': 149995})
# pop=pd.Series({'California': 38332521, 'Texas': 26448193,'New York': 19651127, 'Florida': 19552860,'Illinois': 12882135})
# data=pd.DataFrame({'area':area,'pop':pop})
# # print(data)
# data['density']=data['pop']/data['area']
# print(data)
# print(data.loc[data['pop']<20000000,:])
# df1=pd.DataFrame({'A':[1,2],'B':[3,4]})
# df2=pd.DataFrame({'B':[5,6],'C':[7,8]})
# print(pd.concat([df1,df2],join='inner'))
# df1=pd.DataFrame({'key':['A','B','C'],'value_df1':[1,2,3]})
# df2=pd.DataFrame({'key':['B','C','D'],'value_df2':[4,5,6]})
# print(pd.merge(df1,df2,on='key',how='right'))

# df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],"date":pd.date_range('20130102', periods=6),"city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],"age":[23,44,54,32,34,32],"category":['100-A','100-B','110-A','110-C','210-A','130-F'],"price":[1200,np.nan,2133,5433,np.nan,4432]},columns =['id','date','city','category','age','price'])
# print(df.shape)
# print(df.info())

# data=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]},index=['x','y','z'])
# data=pd.DataFrame({'state':['California','Texas','New York','Florida','Illinois'],'area':[423967,695662,141297,170312,149995],'pop':[38332521,26448193,19651127,19552860,12882135]})
# print(data[data['pop']<20000000][['state','area']])
# print(['state','area'][data['pop']<20000000])

df=pd.DataFrame({'A':[1,2,None],'B':[3,4,5],'C':[6,7,8]})
# print(df.isnull().sum())
# grid=plt.GridSpec(4,4,wspace=0.4,hspace=0.4)
# x=np.linspace(0,10,100)
# plt.subplot(grid[:3,0])
# plt.plot(x,np.sin(x),color='red')
# plt.subplot(grid[:3,1:])
# plt.plot(x,np.sin(x),color='red')
# plt.subplot(grid[3,1:])
# plt.plot(x,np.sin(x),color='red')



# births_per_day=np.random.randint(4400,5400,size=365)
# days = np.arange(1, 366)
# months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# plt.plot(days, births_per_day, label='Births per day')
# plt.xlabel('Month')
# plt.xticks(ticks=np.linspace(1, 365, 12), labels=months)
# plt.ylabel('Number of births')
# plt.title('Number of births per day over a year')
# plt.legend()

# poi_day = 200
# poi_births = births_per_day[poi_day - 1]
# plt.scatter(poi_day, poi_births, color='red')
# plt.text(poi_day, poi_births + 100, 'POI', color='red', ha='center')
# plt.show()


# sns.set_theme(style="dark")

# # Simulate data from a bivariate Gaussian
# n = 10000
# mean = [0, 0]
# cov = [(2, .4), (.4, .2)]
# rng = np.random.RandomState(0)
# x, y = rng.multivariate_normal(mean, cov, n).T

# # Draw a combo histogram and scatterplot with density contours
# f, ax = plt.subplots(figsize=(6, 6))
# sns.scatterplot(x=x, y=y, s=5, color=".15")
# sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
# sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

