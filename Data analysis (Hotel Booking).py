#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading the dataset

# In[29]:


df = pd.read_csv('hotel_bookings 2.csv')


# # Exploratory Data Analysis and Data Cleaning

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format='%d/%m/%Y')


# In[9]:


df.describe(include = 'object')


# In[10]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[11]:


df.isnull().sum()


# In[12]:


df.drop(['company','agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[13]:


df.isnull().sum()


# In[14]:


df.describe()


# In[15]:


df = df[df['adr']<5000]


# # Data Analysis and Visualizations

# In[16]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5, 4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[17]:


plt.figure(figsize =(8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels',size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[18]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[19]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[20]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel =city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[21]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[22]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright' )
legend_labels,_ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status per month')
plt.xlabel('month')
plt.ylabel('number of reservation')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[23]:


plt.figure(figsize = (15, 8))
plt.title('ADR per month', fontsize = 30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled']==1].groupby('month')['adr'].sum().reset_index())
plt.show()


# In[24]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts().head(10)

plt.figure(figsize=(8, 8))
plt.title('Top 10 countries with reservations canceled')
plt.pie(top_10_country, autopct='%.2f', labels=top_10_country.index)
plt.show()


# In[25]:


df['market_segment'].value_counts()


# In[26]:


df['market_segment'].value_counts(normalize = True)


# In[27]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[ ]:




