
#this is a hotel managment program

rooms = -10

print("Hotel Management System")

print("Check available rooms by pressing 1")
print("For booking a room press 2")
print("To check out a room press 3")
print("Exit 4")

customer_choice = int(input("INput integer: "))

if customer_choice == 1:
    if rooms > 0:
        rooms-=1
        print("ROOM is available")
    else:
        print('No room available.')
elif customer_choice == 2:
    print("room booked")



