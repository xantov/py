hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
total_mins = mins + dura

add_hour   = total_mins//60
new_hour   = (hour + add_hour)%24
add_day    = add_hour//24

new_mins   = total_mins%60
 
new_hour   = new_hour if new_hour > 9 else '0'+str(new_hour)
new_mins   = new_mins if new_mins > 9 else '0'+str(new_mins)

print('The event will be ended at +{} day(s), {}:{}'.format(add_day,new_hour,new_mins))
