import pandas as pd
import matplotlib.pyplot as plt

# Data for rooms and guests
rooms = pd.DataFrame({
    'Room No': [101, 102, 103, 104, 105],
    'Room Type': ['Single', 'Double', 'Suite', 'Single', 'Double'],
    'Status': ['Available', 'Occupied', 'Available', 'Available', 'Occupied']
})

guests = pd.DataFrame({
    'Guest ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Emma', 'Oliver', 'Ava', 'William'],
    'Room No': [101, 102, 103, 104, 105],
    'Check-in Date': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15', '2024-01-20'],
    'Check-out Date': ['2024-01-05', '2024-01-10', '2024-01-15', '2024-01-20', '2024-01-25']
})

# Main program
while True:
    print("\nHotel Management System")
    print("1. Display Rooms")
    print("2. Display Guests")
    print("3. Book Room")
    print("4. Check Out")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(rooms)
    elif choice == 2:
        print(guests)
    elif choice == 3:
        room_no = int(input("Enter room number: "))
        if rooms.loc[rooms['Room No'] == room_no, 'Status'].values[0] == 'Available':
            guest_id = int(input("Enter guest ID: "))
            name = input("Enter guest name: ")
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")

            rooms.loc[rooms['Room No'] == room_no, 'Status'] = 'Occupied'
            guests.loc[len(guests)] = [guest_id, name, room_no, check_in, check_out]
            print(f"Room {room_no} booked successfully.")
        else:
            print(f"Room {room_no} is not available.")
    elif choice == 4:
        guest_id = int(input("Enter guest ID to check out: "))
        guest = guests.loc[guests['Guest ID'] == guest_id]
        if not guest.empty:
            room_no = guest['Room No'].values[0]
            rooms.loc[rooms['Room No'] == room_no, 'Status'] = 'Available'
            guests = guests[guests['Guest ID'] != guest_id]
            print(f"Guest {guest_id} checked out successfully.")
        else:
            print("Guest not found.")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

# Display rooms as bar graph
# Plot room availability (Available vs Occupied)
room_status_count = rooms['Status'].value_counts()
room_status_count.plot(kind='bar', color=['green', 'red'])

plt.xlabel('Room Status')
plt.ylabel('Count')
plt.title('Room Availability Status')
plt.xticks(rotation=0)
plt.show()

# Optionally, you can also visualize Room Type counts
room_type_count = rooms['Room Type'].value_counts()
room_type_count.plot(kind='bar', color='skyblue')

plt.xlabel('Room Type')
plt.ylabel('Count')
plt.title('Count of Each Room Type')
plt.xticks(rotation=0)
plt.show()
