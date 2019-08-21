## Import th libraries
import datetime
import calendar

## Calculate balance
# Create variable that we need
balance = 5000
interest_rate = 13 *.01
monthly_payment = 500

## Calculate the balance we have
# Create today variable
today = datetime.date.today()
print(today)

# Create a variable to calculate total days this month
day_in_current_month = calendar.monthrange(today.year, today.month)[1]
print(day_in_current_month)

# Count how many days till the end of the month
days_till_end_month = day_in_current_month - today.day
print(days_till_end_month)

# Create  a start_date and end_date variables
start_date = today + datetime.timedelta(days=days_till_end_month)
end_date = start_date
print(start_date, end_date)

# Calculate
while balance > 0 :
    interest_charge = interest_rate / 12 * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)

    if balance < 0 :
        balance = 0

    day_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date += datetime.timedelta(days=day_in_current_month)

    print(end_date, balance)

print()

## Calculate weight
# Create variable that we need
current_weight = 240
weigth_goal = 150
avg_lbs_week = 2

# Create  a start_date and end_date variables
start_date = today
end_date = start_date

# Calculate
while current_weight > weigth_goal :
    end_date -= datetime.timedelta(weeks=1)
    current_weight -= avg_lbs_week

print(f"Reached goals in {(start_date - end_date).days // 7} weeks")

print()

## Calculate total subs
# Create variable that we need
current_subs = 50000
subs_goal = 100000
subs_to_go = subs_goal - current_subs
subs_per_day = 400

print(today)

# Using mathematics
import math

# floor() method in Python returns floor of x i.e., the largest integer not greater than x
# ceil() in Python returns ceiling value of x i.e., the smallest integer not less than x.
days_to_go = math.ceil(subs_to_go / subs_per_day)
print(days_to_go)

# Calculate
end_date = today + datetime.timedelta(days=days_to_go)
print(end_date)
