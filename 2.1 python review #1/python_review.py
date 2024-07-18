#library
import random

#random temp generator
temp = [random.randint(26,40) for i in range(7)]
days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

#shellys good days
good_days_count = 0
good_days = []
even_days = []

for i in range(len(temp)):
	if temp[i]%2 == 0:
		good_days_count += 1
		even_days.append(days_of_the_week[i])

#hot and cold days
max_temp = max(temp)
min_temp = min(temp)
max_temp_day = days_of_the_week[temp.index(max_temp)]
min_temp_day = days_of_the_week[temp.index(min_temp)]

#above avg temp
avg_temp = sum(temp) / len(temp)
above_avg = [temp for temp in temp if temp > avg_temp]

#news report
print("The weather report of the week: ", temp)
print("shelly had", even_days, " good_days")
print("The hotest temp was: ", max_temp, "on", max_temp_day)
print("The coldest temp was: ", min_temp, "on", min_temp_day)
print("Average temp for the week is: ", avg_temp)
print("Days that were above the average temps: ", above_avg)

#bonus task
sorted_temp = sorted(temp) 
print(sorted_temp)
