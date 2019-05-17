# Task 1
buses = [] # bus master list - contains all 6 bus data
days = 20
daynames = ["Mon","Tue","Wed","Thu","Fri"]
busnames = ["busA","busB","busC","busD","busE","busF"]

for b in range(6):
    bus = [] # creates a new bus 6 times
    
    for day in range(days): # For each bus, input 20 days worth of results
        while True: # continues input until input is valid
            try:
                print("Prompting for",busnames[b],"on",daynames[day%5]+str((day//5) + 1)) # Calculates week number
                minutes = int(input("Enter minutes late here: ")) # tries to convert into integer; if failed, goes to except and restarts loop
                break
            except:
                print("Please enter valid integer.")
                
        bus.append(minutes) # once validated, appends to bus
    buses.append(bus) # after 20 loops, finishes entering for each bus and appends it to the bus master list

# Task 2
for index,bus in enumerate(buses): # In each loop, creates a temporary variable which tracks the position and item
    lates_only = [i for i in bus if i < 0] # finds the late entries by filtering for results less than 0
    
    print(busnames[index],"had",len(lates_only),"late arrivals.")
    print(busnames[index],"averaged",sum(bus)/len(bus),"minutes late.")

    if len(lates_only): # if there were any lates on this bus; to avoid division by 0
        print(busnames[index],"averaged",sum(lates_only)/len(lates_only),"minutes only on late days.")
    else: # if there weren't any lates, program would do 0/0, causing a ZeroDivisionError
        print("There were no lates on",busnames[index]+"'s route.")

    if len(lates_only) == max([[i for i in bus if i < 0] for bus in buses],key=len): # if 1st place was tied, it prints all buses who match the most lates
        print(busnames[index],"had the most days late.")

#3
while True:
    day = input("Enter day: ")

    # validation check
     # 1. Checks if input length is 4 (i.e 'Monday1' is invalid)
     # 2. Checks if first 3 chars is a valid day (i.e. 'Mon' is fine but 'abc' is not)
     # 3. Checks if the last char is a number
     # 4. Checks is the last char is a number within the acceptable range (1-4)
    if not len(day) == 4 or not day[:3] in daynames or not day[-1].isdigit() or not 1 <= int(day[-1]) <= 4:
        print("Please enter a valid day.")
        continue # restarts at the top of the loop

    # to convert the day into an index in a list (e.g. Mon1 -> 0, Tue2 -> 6) - see README for more info
    index = daynames.index(day[:3]) + (int(day[-1])-1)*5

    total = 0 # total amount of late buses
    for busindex,bus in enumerate(buses): # keeps track of index and item each loop
        if bus[index] < 0:
            total += 1
            print(busnames[busindex],"was late on",day,"by",-bus[index],"minutes.") # use '-bus[index]' because late minutes are in the negative

    print(total,"buses were late on",day+".")    
