import pandas as pd
import random

# Sample train data
train_data = {
    'Train': ['A express', 'B express', 'C express'],
    'Sleeper Seats': [50, 100, 80],
    'AC Seats': [25, 40, 35],
    'AC Price': [1600, 1750, 1700],
    'Sleeper Price': [650, 750, 800]
}
trains = pd.DataFrame(train_data)

# Function to check seat availability
def check_availability(train, class_type, num_seats):
    if train in trains['Train'].values:
        index = trains[trains['Train'] == train].index[0]

        if class_type == 'Sleeper':
            return trains.at[index, 'Sleeper Seats'] >= num_seats
        elif class_type == 'AC':
            return trains.at[index, 'AC Seats'] >= num_seats
        else:
            print("Invalid class type.")
            return False
    else:
        print("Train not found.")
        return False

# Function to book tickets
def book_tickets(train, class_type, num_seats):
    if check_availability(train, class_type, num_seats):
        index = trains[trains['Train'] == train].index[0]

        if class_type == 'Sleeper':
            trains.at[index, 'Sleeper Seats'] -= num_seats  # Update seat count
            price = trains.at[index, 'Sleeper Price']
        elif class_type == 'AC':
            trains.at[index, 'AC Seats'] -= num_seats  # Update seat count
            price = trains.at[index, 'AC Price']
        else:
            print("Invalid class type.")
            return
        
        # Generate a random 10-character PNR
        pnr_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
        
        print("\n🎟️ Tickets booked successfully!")
        print(f"🔹 PNR Number: {pnr_number}")
        print(f"💰 Total Fare: {price * num_seats} INR\n")
    else:
        print("\n❌ Booking failed. Seats not available.\n")

# Interactive User Booking
def user_interaction():
    while True:
        print("\n🚆 Available Trains (Updated Seat Counts):")
        print(trains[['Train', 'Sleeper Seats', 'AC Seats']])

        train = input("\nEnter train name: ").strip()
        class_type = input("Enter class (Sleeper/AC): ").strip()
        
        try:
            num_seats = int(input("Enter number of seats: "))
            if num_seats <= 0:
                print("❌ Invalid number of seats. Must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        book_tickets(train, class_type, num_seats)

        cont = input("Do you want to book another ticket? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using our service! 🚄")
            break

# Start User Interaction
user_interaction()
