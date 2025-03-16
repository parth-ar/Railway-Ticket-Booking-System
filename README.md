# Railway-Ticket-Booking-System
A basic railway ticket booking system.
Introduction:
We are basically using lists to store train names, available seats in different classes and ticket prices.
Using operators to check for seat availability, ticket booking, fare calculation and generating PNR numbers.
Working:
Creating a pandas DataFrame to store train data named trains, this DataFrame stores trains, sleeper seats, AC seats and their respective prices.
Availability function: Take train name, class type and number of seats as input. Check if the specified train and class have enough available seats.
Booking function: We use check_availability to confirm seat availability. If available, it reduces the available seats and generates a random PNR number which can be later printed along with other details. 
