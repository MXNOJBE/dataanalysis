# %% [markdown]
# ## FORMULA 1 DATA ANALAYSIS

# %% [markdown]
# Formula 1 is the most advanced form of motorsports, Known for its intensive use of science and technolgy. It has a name "PINNACLE OF MOTORSPORT"
# About the sport:
# Teams in the recent hybrid era have been 10, known as constructors also.
# Every team has two drivers and two cars.
# so 20 drivers
# there will be around 20-22 races per year.
# each race will be held in differrent tracks all around the world.
# The race weekend will start from
# friday which has 2 practices
# saturday one practice session winded up with a qualifier session
# sprint races are another form of races which will be held at some special tracks.

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# %%

results = pd.read_csv('results.csv')
races = pd.read_csv('races.csv')
drivers = pd.read_csv('drivers.csv')
constructors = pd.read_csv('constructors.csv')

# %%
df = pd.merge(
    results, races[['raceId', 'year', 'name', 'round']], on='raceId', how='left')
df = pd.merge(df, drivers[['driverId', 'driverRef',
              'nationality']], on='driverId', how='left')
df = pd.merge(df, constructors[[
              'constructorId', 'name', 'nationality']], on='constructorId', how='left')

# %%
df.drop(['number', 'position', 'laps', 'fastestLap', 'statusId',
        'resultId', 'driverId', 'constructorId'], axis=1, inplace=True)

# %%
df.rename(columns={'rank': 'fastest_lap_rank', 'name_x': 'gp_name', 'nationality_x': 'driver_nationality',
          'name_y': 'constructor_name', 'nationality_y': 'constructor_nationality', 'driverRef': 'driver'}, inplace=True)


# %%
df = df[['year', 'gp_name', 'round', 'driver', 'constructor_name', 'grid', 'positionOrder', 'points', 'time',
         'milliseconds', 'fastest_lap_rank', 'fastestLapTime', 'fastestLapSpeed', 'driver_nationality', 'constructor_nationality']]

# %%
df = df[df['year'] != 2022]

# %%
df = df.sort_values(by=['year', 'round', 'positionOrder'],
                    ascending=[False, True, True])

# %%
df.time.replace('\\N', np.nan, inplace=True)
df.milliseconds.replace('\\N', np.nan, inplace=True)
df.fastestLapSpeed.replace('\\N', np.nan, inplace=True)
df.fastestLapTime.replace('\\N', np.nan, inplace=True)
df.fastest_lap_rank.replace('\\N', np.nan, inplace=True)


# %%
df.fastestLapSpeed = df.fastestLapSpeed.astype(float)
df.fastest_lap_rank = df.fastest_lap_rank.astype(float)
df.milliseconds = df.milliseconds.astype(float)


# %%
df.reset_index(drop=True, inplace=True)

# %%
print(df.shape)

# %%
df.info()


# %%
df.head(10)

# %%
sns.set_palette('Set3')
plt.rcParams['figure.figsize'] = (15, 8)

# %%
# all gp winners
gp_winners1950 = df.loc[df['positionOrder'] == 1].groupby('driver')[
    'positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()

# %%
# barplot
plt.figure(figsize=(15, 8))
sns.barplot(x='driver', y='positionOrder', data=gp_winners1950.head(10))
#sns.barplot(data = gp_winners1950, x = 'driver', y = 'positionOrder')
plt.title('Most Race Winners since 1950', fontsize=20,)
plt.xlabel('Drivers')
plt.ylabel('GP Wins')
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# Formula 1 started from 1950 and collectively these are the top10 drivers. To be noted that Sir Lewis Hamilton from mercedes is still racing his record is yet to be broken by himself. He is considered as the most successfull driver in the history

# %%
constructor_winners = df.loc[df['positionOrder'] == 1].groupby('constructor_name')[
    'positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
sns.barplot(x='constructor_name', y='positionOrder',
            data=constructor_winners.head(10))
plt.title('Most Constructor Winners', fontsize=20)
plt.xlabel('Constructors')
plt.ylabel('Constructor Wins')
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# Ferrari are the world famous known super cars and hyper cars , hey have been in the sport from the starting and they have quite a lot of dominationa dn similary Mclaren. They have had very succesfullc ars and drivvrs and have won and made an extensive records already.

# %% [markdown]
# ## 2021 SEASON ANALYSIS  ##

# %% [markdown]
# Now concentrating more on the 2021 season

# %%

df = df[df['year'] == 2021]
# all gp winners
gp_winners = df.loc[df['positionOrder'] == 1].groupby('driver')[
    'positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
# barplot
plt.figure(figsize=(15, 8))
sns.barplot(x='driver', y='positionOrder', data=gp_winners.head(10))
#sns.barplot(data = gp_winners, x = 'driver', y = 'positionOrder', color='blue', alpha = 0.8)
plt.title('Most Wins in 2021', fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('GP Wins')
plt.xticks(rotation=90)
plt.show()


# %% [markdown]
# We can see that Max Vertapen from Redbull Racing is the most race winner. And he is the **Drivers World Champion** of the year 2021 and is guessed to be the winner in 2021

# %%
constructor_winners = df.loc[df['positionOrder'] == 1].groupby('constructor_name')[
    'positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
# barplot
plt.figure(figsize=(15, 8))
sns.barplot(x='constructor_name', y='positionOrder',
            data=constructor_winners.head(10))
#sns.barplot(data = gp_winners, x = 'driver', y = 'positionOrder', color='blue', alpha = 0.8)
plt.title('Most GP Winners', fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('GP Wins')
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# we can clearly see as max won more than lewis hamiton , redbull has won more races

# %%
# Topspeed
fastestLap = df.groupby(['driver', 'constructor_name'])[
    'fastestLapSpeed'].mean().sort_values(ascending=False).to_frame().reset_index()
plt.figure(figsize=(15, 8))
sns.scatterplot(x='driver', y='fastestLapSpeed', data=fastestLap.head(10))
plt.title('Top Speed', fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Fastest Lap Speed')
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# Here comes the top speed, if the driver manages to cLock in a great speed it will be recorded in respect of any track

# %%
fastestLap = df.groupby(['driver', 'constructor_name'])[
    'fastest_lap_rank'].mean().sort_values(ascending=True).to_frame().reset_index()
plt.figure(figsize=(15, 8))
sns.scatterplot(x='driver', y='fastest_lap_rank', data=fastestLap.head(20))
plt.title('Fastest Lap', fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Fastest Lap Rank')
plt.xticks(rotation=90)
plt.show()


# %% [markdown]
# Every race has a fastest Laptime, and we can see Max Verstappen winning more than twice. Fastest time is nothing but he fastest time which a aperson took complete one lap

# %%
# drivers with most points
mostpoints = df.groupby(['driver', 'constructor_name'])['points'].sum(
).sort_values(ascending=False).to_frame().reset_index()
plt.figure(figsize=(15, 8))
sns.barplot(x='driver', y='points', data=mostpoints.head(20))
plt.title('Most Points', fontsize=20)
plt.xlabel('Drivers')
plt.ylabel('Points')
plt.xticks(rotation=90)
plt.show()


# %% [markdown]
# This is the final scoreboard or point table of 2021 drivers championship. We can see that there is nots big gap between lewis hamilton and max verstappen as they awer head on head in the season and other maintian a decent amount of gap to top2.

# %%
mostpoints_teams = df.groupby(['constructor_name'])['points'].sum(
).sort_values(ascending=False).to_frame().reset_index()
plt.figure(figsize=(15, 8))
sns.barplot(x='constructor_name', y='points', data=mostpoints_teams.head(20))
plt.title('Most Points', fontsize=20)
plt.xlabel('Teams')
plt.ylabel('Points')
plt.xticks(rotation=90)
plt.show()


# %% [markdown]
# We can see the scoreboard of 2021 Constructor Championship.
# Mercedes are the constrcutor championship winner and have been consistently winning this from past 8 years.

# %% [markdown]
# ## END OF ANALYSIS <B>
# ## THANK YOU ##
