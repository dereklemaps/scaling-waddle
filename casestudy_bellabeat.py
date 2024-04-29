import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt 

daily_activity = pd.read_csv('dailyActivity_merged.csv')

#preview data
daily_activity.info()
daily_activity.head(10)

#check for null values
null_values = daily_activity.isnull().sum()

#count unique IDs
unique_id = len(pd.unique(daily_activity['Id']))
#33 unique IDs mean some users may have created more than 1 account

#convert ActivityDate to datetime
daily_activity['ActivityDate'] = pd.to_datetime(daily_activity['ActivityDate'])
daily_activity['ActivityDate'].dtypes #dtype check

#create DayOfTheWeek to check active days
daily_activity['DayOfTheWeek'] = daily_activity['ActivityDate'].dt.day_name()
daily_activity['DayOfTheWeek'].head() #column check

#create TotalMins to sum all active mins
daily_activity['TotalMins'] = daily_activity['VeryActiveMinutes'] + daily_activity['FairlyActiveMinutes'] + daily_activity['LightlyActiveMinutes'] + daily_activity['SedentaryMinutes']
daily_activity['TotalMins'].head() #column check

#review data
daily_activity.describe()

#creating visualizations
#plot of daily app activity
# plt.hist(daily_activity.DayOfTheWeek, width = 0.75, bins = 7, color = 'orange')
# plt.xlabel('Day of the Week')
# plt.ylabel('Frequency')
# plt.title('App Activity During the Week')
#lower activity Friday to Monday

#plot of distance vs calories burned
# plt.figure(figsize=(8,6))
# plt.scatter(daily_activity.TotalDistance, daily_activity.Calories, c = daily_activity.Calories)
# plt.xlabel('Total Distance Traveled')
# plt.ylabel('Calories Burned')
# plt.title('Calories Burned for Distance Traveled')
# plt.grid(True)
#strong positive correlation between distance traveled vs calories burned

#plot of minutes logged vs calories burned
# plt.figure(figsize=(8,6))
# plt.scatter(daily_activity.TotalMins, daily_activity.Calories, c = daily_activity.Calories)
# plt.xlabel('Total Minutes Logged')
# plt.ylabel('Calories Burned')
# plt.title('Calories Burned for Minutes Logged')
# plt.grid(True)
#weak positive correlation between minutes logged in app vs calories burned
#app activity does not lead to physical activity

#plot of activity type proportion in minutes
VeryActiveMinutes = daily_activity.VeryActiveMinutes.sum()
FairlyActiveMinutes = daily_activity.FairlyActiveMinutes.sum()
LightlyActiveMinutes = daily_activity.LightlyActiveMinutes.sum()
SedentaryMinutes = daily_activity.SedentaryMinutes.sum()
activity_type = ['Very active minutes', 'Fairly active minutes', 'Lightly active minutes', 'Sedentary minutes']
activity_mins = [VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes, SedentaryMinutes]
plt.pie(activity_mins, labels=activity_type, autopct='%1.1f%%')
plt.title('Percentage of Activity Type in Minutes')
plt.show()