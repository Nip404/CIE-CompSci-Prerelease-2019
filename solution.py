#1
buses = []
days = 20
daynames = ["Mon","Tue","Wed","Thu","Fri"]
busnames = ["busA","busB","busC","busD","busE","busF"]

for b in range(6):
    bus = []
    
    for day in range(days):
        while True:
            try:
                print("Prompting for",busnames[b],"on",daynames[day%5]+str((day//5) + 1))
                minutes = int(input("Enter minutes late here: "))
                break
            except:
                print("Please enter valid integer.")
                
        bus.append(minutes)
    buses.append(bus)

#2
for index,bus in enumerate(buses):
    lates_only = list(filter(lambda x: x < 0,bus))
    
    print(busnames[index],"had",len(lates_only),"late arrivals.")
    print(busnames[index],"averaged",sum(bus)/len(bus),"minutes late.")

    if len(lates_only):
        print(busnames[index],"averaged",sum(lates_only)/len(lates_only),"minutes only on late days.")
    else:
        print("There were no lates on",busnames[index]+"'s route.")

    if len(lates_only) == max(buses,key=len):
        print(busnames[index],"had the most days late.")

#3
while True:
    day = input("Enter day: ")

    if not len(day) == 4 or not day[:3] in daynames or not day[-1].isdigit() or not 1 <= int(day[-1]) <= 4:
        print("Please enter a valid day")
        continue

    daypos = daynames.index(day[:3])
    weekpos = (int(day[-1])-1)*5
    index = daypos+weekpos

    total = 0
    for busindex,bus in enumerate(buses):
        if bus[index] < 0:
            total += 1
            print(busnames[busindex],"was late on",day,"by",-bus[index],"minutes.")

    print(total,"buses were late on",day+".")    
