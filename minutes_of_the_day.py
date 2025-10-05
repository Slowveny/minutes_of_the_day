def time_passed(hours, minutes):
    global start_of_day, end_of_day
    start_of_day = hours * 60 + minutes
    end_of_day = 1440 - start_of_day

hours = int(input('What hour is it now (0-23)? '))
while hours < 0 or hours > 23:
    print('Invalid hour!')
    hours = int(input('What hour is it now (0-23)? '))

minutes = int(input('What minutes is it now (0-59)? '))
while minutes < 0 or minutes > 59:
    print('Invalid minutes!')
    minutes = int(input('What minutes is it now (0-59)? '))

time_passed(hours, minutes)
print(f'{start_of_day} minutes have passed since the start of the day.')
print(f'{end_of_day} minutes are left until the end of the day.')
