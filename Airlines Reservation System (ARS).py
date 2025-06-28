# Title, Interface
def interface():
    title = "--WELCOME TO NIKA CENTRAL RESERVATION SYSTEM!--"
    required_length = len(title) + 30
    title_modified = title.center(required_length)
    print(title_modified)


# Registration for customer
def register_customer():
    file = "customer.txt"
    print("< Registration >")
    while True:
        username = str(input("Username: "))
        password = str(input("Password: "))
        confirm_password = str(input("Confirm your password: "))
        # Confirm password is not same will repeat
        if confirm_password == password:
            print("[Your data has been saved.]\n")
            break
        else:
            print("[Your password are not same. Try it again.]\n")

    # Ask user for information
    print("---Contact Information---")
    while True:
        try:
            ph_no = int(input("Enter your contact number: +"))
            while len(str(ph_no)) > 12:
                print("[Your contact number shouldn't be more than 12]")
                ph_no = (input("\nRe-enter your contact number: "))
            break
        except ValueError:
            print("[Invalid input. Please enter integer number.]")

    email = input("Enter your email: ")
    print("\n< Address >")
    street = input("Enter street: ").upper()
    state = input("Enter state: ").upper()
    while True:
        try:
            postal_no = int(input("Enter postal number: "))
            while len(str(postal_no)) != 5:
                print("[The length of postal number should be 5]\n")
                postal_no = (input("Re-enter the postal number: "))
            break
        except ValueError:
            print("[Invalid input. Please enter integer number.]\n")
    city = input("Enter city: ").upper()
    address = f"{street}/ {state}/ {postal_no}/ {city}."
    print(f"Address: {address}")

    print("\n---Personal information---")
    gender = str(input("Enter your gender (Male/Female):")).capitalize()
    while gender.capitalize() != "Male" and gender.capitalize() != "Female":
        print("[Something wrong. Check again.]")
        gender = str(input("\nEnter your gender again:"))

    print("\n< Birthday >")
    while True:
        try:
            year = int(input("Enter year(YYYY): "))
            while year < 1900 or year > 2023:
                print("[Invalid value.Check again.]")
                year = int(input("\nEnter year again(YYYY): "))
            month = int(input("Enter month(MM): "))
            while month <= 0 or month > 12:
                print("[Invalid value. Month should be within (01-12)]")
                month = int(input("\nEnter month again(MM): "))
            day = int(input("Enter day(DD): "))
            while (day < 1 or
                   day > 31 or
                   year % 4 != 0 and month == 2 and day > 28 or
                   year % 4 == 0 and month == 2 and day > 29 or
                   month == 4 and day > 30 or
                   month == 6 and day > 30 or
                   month == 9 and day > 30 or
                   month == 11 and day > 30):
                print("[Invalid date]")
                day = int(input("\nEnter day again(DD): "))

            birthday = f"{day}/{month}/{year}"
            print(birthday)
            break
        except ValueError:
            print("[Invalid input. Please enter integer number.]\n")
    with open(file, "a") as register_customer_file:
        register_customer_file.write(f"{username},{password},{ph_no},{email},{address},{gender},{birthday}\n")


def admin_acc(username, password):
    with open('admin.txt', 'w') as f:
        f.write(f"{username},{password}\n")

admin_acc('nika', '12345')
#only one username and password for all admin to login


# Log in for customer
def customer_login():
    attempt = 0
    while attempt < 3:
        print("\n< Log in >\n[Enter 'e' to exit]")
        username = input("Username: ")
        if username == 'e' or username == 'E':
            break
        password = input("Password: ")
        if password == 'e' or password == 'E':
            break
        with open("customer.txt", "r") as file:
            for line in file:
                if f"{username}, {password}" in line:
                    print(f"[Log in successfully! Welcome {username.capitalize()}.]\n")
                    while True:
                        option_flight = input("Choose the following option for flight ticket: "
                                              "\na. View Available Flights"
                                              "\nb. Booking Flight"
                                              "\nc. View Own Bookings"
                                              "\nd. Update Own Booking"
                                              "\ne. Cancel Own Booking"
                                              "\nf. Order Food"
                                              "\ng. Generate Boarding Pass"
                                              "\nh. Profile"
                                              "\ni. Exit"
                                              "\n>>> ")
                        if option_flight.lower() == "a":
                            print("\n----------/ View Flight /-----------")
                            display_updated_flights()
                            continue
                        elif option_flight.lower() == "b":
                            print("\n-----------/ Book Flight /----------")
                            booking_info(username)
                            continue
                        elif option_flight.lower() == "c":
                            print("\n-----------/ View Own Booking /----------")
                            view_own_bookings(username)
                            continue
                        elif option_flight.lower() == "d":
                            print("\n----------/ Update Own Booking /----------")
                            update_own_booking(username)
                            continue
                        elif option_flight.lower() == "e":
                            print("\n----------/ Cancel Own Booking /----------")
                            cancel_own_booking(username)
                            continue
                        elif option_flight.lower() == "f":
                            print("\n----------/ Order Food /----------")
                            in_flight_menu = initialize_in_flight_menu()
                            orders = {}
                            order_food(in_flight_menu, orders)
                            continue
                        elif option_flight.lower() == "g":
                            print("\n-----------/ Self Check in /----------")
                            self_check_in(username)
                            continue
                        elif option_flight.lower() == "h":
                            print("\n-----------/ Profile /----------")
                            profile(username)
                            continue
                        elif option_flight.lower() == "i":
                            break
                        else:
                            print("[Invalid value, please check again.]\n")
                            continue
                    break
            else:
                print("[User not found. Please try again.]\n")
                attempt += 1
    else:
        print("[Too many login attempts.]\n")
        exit()


# Log in for admin
def admin_login():
    exit_value = 0  # variable so if user inputs 'e' program will go back
    print("\n< Log in >\n[Enter 'e' to exit]")
    with open('admin.txt', 'r') as f:
        count = 3
        while count > 0:
            username = str(input("Username: "))
            if username == 'e' or username == 'E':
                exit_value = 1
                return exit_value
            password = str(input("Password: "))
            if password == 'e' or password == 'E':
                exit_value = 1
                return exit_value
            for line in f:
                admin_username, admin_password = line.strip().split(',')
            if admin_username == username and admin_password == password:
                print(f"Log in successfully. Welcome! {username.capitalize()}.")
                return exit_value
            elif admin_username == username:
                print("Password is wrong")
            else:
                print(f"Account <{username}> is invalid. ")
            count = count - 1

        else:
            print("Too many login attempts.")
            exit()


# Class representing information about a flight
class Flight:
    def __init__(self, airline, airline_id, flight_number, total_economy, total_business,
                 origin, destination, departure_date, departure_time,
                 arrival_date, arrival_time, in_flight_service):
        self.airline = airline
        self.airline_id = airline_id
        self.flight_number = flight_number
        self.total_economy = total_economy
        self.total_business = total_business
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.in_flight_service = in_flight_service
        # initialize a Flight object with provided information

    def display_info(self):
        print(f"Airline: {self.airline}")
        print(f"Airline ID: {self.airline_id}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Total Economy Seats: {self.total_economy}")
        print(f"Total Business Seats: {self.total_business}")
        print(f"Origin state: {self.origin}")
        print(f"Destination state: {self.destination}")
        print(f"Departure Date: {self.departure_date}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Date: {self.arrival_date}")
        print(f"Arrival Time: {self.arrival_time}")
        print(f"In-flight service: {self.in_flight_service}")
        # display information about the flight


def save_flights_to_file(flights, filename):
    with open(filename, 'w') as file:
        for flight in flights:
            file.write(f"{flight.airline},{flight.airline_id},{flight.flight_number},{flight.total_economy},"
                       f"{flight.total_business},{flight.origin},{flight.destination},{flight.departure_date},"
                       f"{flight.departure_time},{flight.arrival_date},{flight.arrival_time},"
                       f"{flight.in_flight_service}\n")
# save a list of flights into a file


def load_flights_from_file(filename):
    flights = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            flight = Flight(*values)
            flights.append(flight)
    return flights


# View all flight
def display_current_flights():
    print("\nCurrent available flights:")
    for current_flight in load_flights_from_file("flights.txt"):
        current_flight.display_info()
        print()


def display_updated_flights():
    print("\nCurrent available flights:")
    for updated_flight in load_flights_from_file("flights.txt"):
        updated_flight.display_info()
        print()
# Display new list of flights after updated


# Upload new flight details
def get_new_flight():
    new_airline = input("Enter the airline name:")
    new_airline_id = input("Enter the airline ID:")
    new_flight_number = input("Enter the flight number:")
    new_total_economy = input("Enter the total economy seats:")
    new_total_business = input("Enter the total business seats:")
    new_origin = input("Enter the origin state code only:")
    new_destination = input("Enter the destination state code only:")
    new_departure_date = input("Enter the departure date:")
    new_departure_time = input("Enter the departure time:")
    new_arrival_date = input("Enter the arrival date:")
    new_arrival_time = input("Enter the arrival time:")
    new_in_flight_service = input("In-flight service provided: ")
    return (new_airline, new_airline_id, new_flight_number, new_total_economy, new_total_business, new_origin,
            new_destination, new_departure_date, new_departure_time, new_arrival_date, new_arrival_time,
            new_in_flight_service)
# Origin and destination state input must be flight code only i.e. Kuala Lumpur = KUL

def add_new_flight():
    flights = load_flights_from_file("flights.txt")
    (new_airline, new_airline_id, new_flight_number, new_total_economy, new_total_business, new_origin, new_destination,
     new_departure_date, new_departure_time, new_arrival_date, new_arrival_time,
     new_in_flight_service) = get_new_flight()

    new_flight = Flight(airline=new_airline, airline_id=new_airline_id, flight_number=new_flight_number,
                        total_economy=new_total_economy, total_business=new_total_business, origin=new_origin,
                        destination=new_destination, departure_date=new_departure_date,
                        departure_time=new_departure_time, arrival_date=new_arrival_date, arrival_time=new_arrival_time,
                        in_flight_service=new_in_flight_service)

    flights.extend([new_flight])

    save_flights_to_file(flights, "flights.txt")
    print("[Upload Successfully]")


# Modify or update in-flight service information
def edit_flight(flights, flight_number_to_edit, attribute_index, new_values):
    for flight in flights:
        if flight.flight_number == flight_number_to_edit:
            attributes = ['total_economy', 'total_business', 'origin', 'destination', 'departure_date',
                          'departure_time', 'arrival_date', 'arrival_time', 'in_flight_service']
            setattr(flight, attributes[attribute_index], new_values)


def new_edit_flight():
    flights = load_flights_from_file("flights.txt")
    display_current_flights()

    flight_to_edit = input("Enter an existing flight number to edit: ")
    print(
        "(0)Total economy class seats\n(1)Total business class seats\n(2)Origin state\n(3)Destination state\n"
        "(4)Departure date\n(5)Departure time\n(6)Arrival date\n(7)Arrival time\n(8)In-flight service")
    attribute_index = int(input("Enter which category to be edited(0-8): "))

    edit_value = input("Modify it into:")

    edit_flight(flights, flight_to_edit, attribute_index, edit_value)

    save_flights_to_file(flights, "flights.txt")
    display_updated_flights()


# Delete in-flight service information
def delete_in_flight_service():
    flights = load_flights_from_file("flights.txt")
    display_current_flights()

    flight_number = input("Enter an existing flight number to edit: ")
    service_to_delete = input("What service do you want to delete?: ")
    for flight in flights:
        if flight.flight_number == flight_number:
            if flight.in_flight_service == service_to_delete:
                flight.in_flight_service = "no meal provided"
            else:
                print(f"No '{service_to_delete}' in-flight service is found.")

    save_flights_to_file(flights, "flights.txt")
    display_updated_flights()


# Initialize in-flight menu
def initialize_in_flight_menu():
    in_flight_menu = {
        '1': {'item': 'Sandwich', 'price': 10},
        '2': {'item': 'Salad', 'price': 8},
        '3': {'item': 'Pasta', 'price': 12},
        '4': {'item': 'Burger', 'price': 11},
        '5': {'item': 'Pizza', 'price': 13},
        '6': {'item': 'Sushi', 'price': 15},
        '7': {'item': 'Chicken Rice', 'price': 9},
        '8': {'item': 'Steak', 'price': 18},
        '9': {'item': 'Fruit Platter', 'price': 7},
        '10': {'item': 'Ice Cream', 'price': 5},
    }
    return in_flight_menu


# Display In-flight Menu
def view_in_flight_menu(menu):
    print("-----In-flight Menu-----")
    for item_id, item_info in menu.items():
        print(f"{item_id}. {item_info['item']} - RM{item_info['price']: .2f}")


# Modify In-flight Menu
def edit_in_flight_menu(menu):
    while True:
        print("\nMenu Editing Options:")
        print("1. Add New Item")
        print("2. Delete Item")
        print("3. Done Editing")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            new_item = input("Enter the name of the new menu item: ")
            new_price = float(input(f"Enter the price for {new_item}: "))
            new_id = str(len(menu) + 1)
            menu[new_id] = {'item': new_item, 'price': new_price}
            print(f"Added '{new_item}' to the in-flight menu with a price of {new_price}.")
        elif choice == '2':
            item_to_delete = input("Enter the ID of the item to delete: ")
            if item_to_delete in menu:
                del menu[item_to_delete]
                print(f"Item with ID {item_to_delete} deleted from the in-flight menu.")
            else:
                print(f"No item found with ID {item_to_delete}.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Main code for in-flight menu
def main_in_flight_menu():
    # Initialize or load in-flight menu
    in_flight_menu = initialize_in_flight_menu()

    while True:
        print("\nOptions:")
        print("1. View In-flight Menu"
              "\n2. Edit In-flight Menu"
              "\n3. Delete In-flight Service"
              "\n3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            view_in_flight_menu(in_flight_menu)
        elif choice == '2':
            edit_in_flight_menu(in_flight_menu)
        elif choice == '3':
            delete_in_flight_service()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


# Function to handle food ordering
def order_food(menu, orders):
    # Display the available in-flight menu
    view_in_flight_menu(menu)

    # Loop to take food orders
    while True:
        # Get user input for food ID or 'e' to exit
        order_id = input("Enter the ID of food to order ('e' to exit): ")

        # Check if user wants to exit
        if order_id.lower() == "e":
            break

        # Check if the entered food ID is in the menu
        if order_id in menu:
            # Get user input for the quantity of the selected food
            quantity = int(input("Enter the quantity: "))

            # Check if the food item is already in the order
            if order_id in orders:
                # Increment the quantity if the item is already in the order
                orders[order_id]['quantity'] += quantity
            else:
                # Add the food item to the order if it's not already present
                orders[order_id] = {'item': menu[order_id]['item'],
                                    'price': menu[order_id]['price'],
                                    'quantity': quantity}

                # Display confirmation message for the placed order
                print(f"Order placed: {quantity}x {menu[order_id]['item']}")
        else:
            # Display an error message for an invalid food ID
            print(f"No item found with ID {order_id}")

    # Display the current order details
    print("\nCurrent Orders:")
    total_order_price = 0  # Initialize total order price

    # Loop through the orders and calculate total order price
    for order_id, order_info in orders.items():
        total_price = order_info['price'] * order_info['quantity']
        total_order_price += total_price

        # Display details for each ordered item
        print(f"{order_info['item']} - Quantity: {order_info['quantity']}, Total Price: RM{total_price: .2f}")

    # Display the total order price
    print(f"\nTotal Order Price: RM{total_order_price: .2f}")


# Search specific in-flight menu for specific customer
def display_flights_from_service():
    flights = load_flights_from_file("flights.txt")
    service = input("\nWhich in-flight service do you want?\n'meal provided' or 'no meal provided' : ")
    matching_flights = [flight for flight in flights if flight.in_flight_service == service]
    if matching_flights:
        print(f"\nFlights with {service}: ")
        for matching_flight in matching_flights:
            matching_flight.display_info()
            print()
    else:
        print(f"\nNo flights found with {service}.")


# View the AirlineID, AirlineName and the total number of flights for each Airline
def summarize_flights_by_airline(flights):
    airline_summary = {}

    for flight in flights:
        airline_key = (flight.airline, flight.airline_id)
        if airline_key in airline_summary:
            airline_summary[airline_key] += 1
        else:
            airline_summary[airline_key] = 1

    return airline_summary


def display_airline_summary(airline_summary):
    print("\n")
    print("Airline Name:     | Airline ID:  | Total flights:")
    print("-------------------------------------------------")
    for (airline_name, airline_id), total_flights in airline_summary.items():
        print(f"{airline_name:<16} | {airline_id:<10} |      {total_flights}")
    print("-------------------------------------------------")


def get_airline_summary():
    flights = load_flights_from_file("flights.txt")
    airline_summary = summarize_flights_by_airline(flights)
    
    display_airline_summary(airline_summary)


# Search the Airline with the most frequencies of flights
def most_frequent_airline(flights):
    airline_counts = {}

    for flight in flights:
        airline_key = flight.airline
        if airline_key in airline_counts:
            airline_counts[airline_key] += 1
        else:
            airline_counts[airline_key] = 1

    most_frequent_airline = None
    max_count = 0

    for airline, count in airline_counts.items():
        if count > max_count:
            most_frequent_airline = airline
            max_count = count

    return most_frequent_airline, max_count


def get_most_frequent_airline():
    flights = load_flights_from_file("flights.txt")
    most_frequent, count = most_frequent_airline(flights)
    if most_frequent is not None:
        print(f"The Airline with the most frequent flights is '{most_frequent}' with total of {count} flights.")
    else:
        print("No flights found.")


# Cancel flight schedule
def cancel_schedule_by_id():
    file_path = 'flights.txt'

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    found = False
    print("\n----- Cancel Schedule -----")
    flight_id = input("Enter the Flight ID you want to cancel: ")

    for line in lines:
        flight_data = line.strip().split(',')
        if len(flight_data) >= 10 and flight_data[2] == flight_id:
            found = True
            flight_info = (
                f"Airline: {flight_data[0]}\n"
                f"Airline ID: {flight_data[1]}\n"
                f"Flight ID: {flight_data[2]}\n"
                f"Total economy class seats: {flight_data[3]}\n"
                f"Total business class seats: {flight_data[4]}\n"
                f"Destination state: {flight_data[5]}\n"
                f"Date of departure: {flight_data[6]}\n"
                f"Time of departure: {flight_data[7]}\n"
                f"Date of arrival: {flight_data[8]}\n"
                f"Time of arrival: {flight_data[9]}"
            )
            print("\n< Flight Schedule >")
            print(flight_info + "\n" + "-" * 28 + "\n")
            confirm_cancel = input("Are you sure you want to cancel this schedule (yes/no)? ").lower()
            if confirm_cancel == "yes":
                print(f"[Flight schedule with ID {flight_id} canceled successfully.]\n")
            break  # Stop searching after finding a match

    if not found:
        print(f"[Flight schedule with ID {flight_id} not found.]\n")


# Delete flight details by searching any of flight details such as Airline ID, flight ID...
def delete_flight_details():
    file_path = 'flights.txt'
    lines = []

    # Read all lines from the file and store them in a list
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    found = False
    print("\n----- Delete Flight Details -----")
    search_data = input("Enter any flight detail you want to delete: ")

    for i, line in enumerate(lines):
        flight_data = line.strip().split(',')
        if search_data in line:
            found = True
            flight_info = (f"Airline: {flight_data[0]}\n"
                           f"Airline ID: {flight_data[1]}\n"
                           f"Flight ID: {flight_data[2]}\n"
                           f"Total economy class seats: {flight_data[3]}\n"
                           f"Total business class seats: {flight_data[4]}\n")
            print("\n< Flight Details >")
            print(flight_info + "\n" + "-" * 28 + "\n")
            confirm_cancel = input("Are you sure you want to cancel this flight schedule (yes/no)? ").lower()
            if confirm_cancel == "yes":
                del lines[i]  # Remove the line from the list
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print(f"[Flight details '{search_data}' delete successfully.]\n")
            break  # Stop searching after finding a match

    if not found:
        print(f"[Flight details '{search_data}' not found.]\n")


# Display all current booking
def display_current_booking(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        print("-----All available booking-----")
        for line in lines:
            user_data = line.strip().split(",")
            if len(user_data) == 5:
                user_info = {
                    "Booking ID": user_data[0],
                    "Username": user_data[4],
                    "Departure Country": user_data[1],
                    "Arrival Country": user_data[2],
                    "Booking Date": user_data[3]
                }
                for key, value in user_info.items():
                    print(f"{key}: {value}")
                print("-" * 35)


# Search booking by input any of the booking details such as destination code
def search_booking(file_path):
    while True:
        search_item = input("Search[Enter 'e' to exit]: ")
        if search_item.lower() == "e":
            break
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                booking_data = line.strip().split(',')
                if search_item in line:
                    print(f"Booking ID: {booking_data[0]}\n"
                          f"Username: {booking_data[4]}\n"
                          f"Origin State: {booking_data[1]}\n"
                          f"Destination State: {booking_data[2]}\n"
                          f"Departure Date: {booking_data[3]}")
                print("-" * 30)
                continue


# Read all booking from file
def read_booking_file(file_path='booking.txt'):
    bookings = []
    with open(file_path, 'r') as file:
        for line in file:
            booking_data = line.strip().split(',')
            bookings.append({
                'booking_id': booking_data[0],
                'origin_state': booking_data[1],
                'destination_state': booking_data[2],
                'departure_date': booking_data[3],
                'username': booking_data[4]
            })
    return bookings


# Generate flight ticket by input booking ID
def generate_ticket(bookings):
    search_id = input("Enter the booking ID to generate the ticket: ")
    found_booking = None

    for booking in bookings:
        if booking['booking_id'] == search_id:
            found_booking = booking
            break
    if found_booking:
        print("-" * 42)
        print("\t\tNIKA RESERVATION SYSTEM\t\t")
        print(f"Booking ID        | {found_booking['booking_id']} ")
        print(f"Username          | {found_booking['username']}")
        print(f"Origin State      | {found_booking['origin_state']}")
        print(f"Destination State | {found_booking['destination_state']}")
        print(f"Departure Date    | {found_booking['departure_date']}")
        print("-" * 42)
    else:
        print(f"Booking ID {search_id} not found.")


# Generate bills by input booking id
def generate_bill(bookings):
    search_id = input("Enter the booking ID to generate the bill: ")
    found_booking = None

    for booking in bookings:
        if booking['booking_id'] == search_id:
            found_booking = booking
            break

    if found_booking:
        basic_price = int(input("Enter the basic price: "))
        tax_rate = 6
        tax_amount = basic_price * (tax_rate / 100)
        total_amount = basic_price + tax_amount

        print("-" * 42)
        print("\t\tNIKA RESERVATION SYSTEM\t\t")
        bills = (f"Booking ID        | {found_booking['booking_id']}\n"
                 f"Username          | {found_booking['username']}\n"
                 f"Origin State      | {found_booking['origin_state']}\n"
                 f"Destination State | {found_booking['destination_state']}\n"
                 f"Departure Date    | {found_booking['departure_date']}\n"
                 f"Tax amount(6%)    | RM{tax_amount: .2f}\n"
                 f"Total Price       | RM{total_amount: .2f}")
        print(bills)
        print("-" * 35)
    else:
        print(f"Booking ID {search_id} not found.")


# Main coding for generate tickets and bills
def main_ticket_bill():
    bookings = read_booking_file()
    while True:
        print("1. Generate tickets\n"
              "2. Generate bills\n"
              "3. Exit")
        choice = input(">>> ")

        if choice == '1':
            generate_ticket(bookings)

        elif choice == '2':
            generate_bill(bookings)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter 1, 2")


# Display all of the cancelled booking
def view_cancelled_bookings():
    booking_file = 'Cancelled_Booking.txt'

    try:
        with open(booking_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"[Error: File '{booking_file}' not found.]")
        return
    except Exception as e:
        print(f"[Error: An unexpected error occurred - {e}]")
        return

    print("\n----- Canceled Bookings -----")
    for line in lines:
        booking_details = line.strip().split(',')
        if len(booking_details) >= 4:
            print(f"Booking ID: {booking_details[0]}\n"
                  f"Username: {booking_details[4]}\n"
                  f"Origin State: {booking_details[1]}\n"
                  f"Destination State: {booking_details[2]}\n"
                  f"Departure Date: {booking_details[3]}")
            print(f"-" * 35)
        else:
            print(f"Error: Invalid format in line - {line}")


# Total number of cancelled booking
def no_cancelled_booking():
    file_path = 'Cancelled_Booking.txt'
    line_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
            return line_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return 0


# Total number of customers' account
def no_customer_acc():
    file_path = 'customer.txt'
    line_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
            return line_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return 0


# Total number of bills that have been generated
def count_bill_pairs(file_path='bills.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        pair_count = 0
        for i in range(0, len(lines) - 1, 8):
            if i + 7 < len(lines):
                pair_count += 1

        return pair_count

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return 0


# Generate report
def generate_report():
    print("\t\t[ NIKA RESERVATION SYSTEM ]\t\t")
    print("-" * 43)
    print("\t\t\t -----REPORT-----\t\t")
    print(f"Number of customer cancel booking | {no_cancelled_booking(): >7}")
    print(f"Number of customer register       | {no_customer_acc(): >7}")
    print(f"Number of bills generated         | {count_bill_pairs(): >7}")
    print("-" * 43)


# Admin Interface
def admin_interface():
    while True:
        print("\n1. Booking Information\n"
              "2. Flight Information\n"
              "3. Bills & Ticket\n"
              "4. In-flight Menu\n"
              "5. Generate Report\n"
              "6. Exit\n")
        sel = int(input("Choose the following option: "))
        if sel == 1:
            while True:
                print("1.View\n2.Search\n3.Exit")
                choice = int(input(">>> "))
                if choice == 1:
                    print("\n----------/ View /----------")
                    view_selection = input("1. Current Booking"
                                           "\n2. Cancelled Booking"
                                           "\nChoose a selection[Enter 'e' to exit]: ")
                    if view_selection == '1':
                        print("----------/ Current Booking /----------")
                        display_current_booking('booking.txt')

                    elif view_selection == '2':
                        print("----------/ Cancelled Booking /----------")
                        view_cancelled_bookings()

                    elif view_selection.lower() == 'e':
                        break
                    else:
                        print("[Invalid Input]")

                elif choice == 2:
                    print("----------/ Search Booking /----------")
                    search_booking('booking.txt')
                elif choice == 3:
                    break

        elif sel == 2:
            while True:
                print("(1)Upload"
                      "\n(2)View"
                      "\n(3)Update/Modify"
                      "\n(4)Delete/Cancel"
                      "\n(5)Search"
                      "\n(6)Exit\n")
                choose_action = int(input("What do you want to do?\nPlease select one of the option: "))
                if choose_action == 1:
                    print("\n-----Upload new flight details-----")
                    add_new_flight()

                elif choose_action == 2:
                    print("\n(1)View all flights."
                          "\n(2)View the AirlineID, AirlineName and the total number of flights for each Airline.")
                    choose_view = input("What do you want to view?[Enter 'e' to exit]: ")
                    if choose_view == '1':
                        display_updated_flights()
                    elif choose_view == '2':
                        get_airline_summary()
                    elif choose_view.lower() == 'e':
                        continue

                elif choose_action == 3:
                    new_edit_flight()

                elif choose_action == 4:
                    print("\n-----Delete/Cancel-----")
                    delete_cancel = input("1. Delete Flight Details"
                                          "\n2. Cancel Flight Schedule"
                                          "\n>>> ")
                    if delete_cancel == '1':
                        delete_flight_details()

                    elif delete_cancel == '2':
                        cancel_schedule_by_id()

                elif choose_action == 5:
                    print("\n(1)Specific in-flight Service\n(2)The Airline with the most frequencies of flights")
                    choose_search = int(input("What do you want to search?: "))
                    if choose_search == 1:
                        display_flights_from_service()
                    elif choose_search == 2:
                        get_most_frequent_airline()
                elif choose_action == 6:
                    break
                else:
                    print("[Invalid value]")
                    continue

        elif sel == 3:
            print("----------/ Tickets & Bills /----------")
            main_ticket_bill()

        elif sel == 4:
            main_in_flight_menu()

        elif sel == 5:
            generate_report()

        elif sel == 6:
            break


# Booking system
# Generate Random booking ID
def booking_id():
    file = "booking.txt"
    import random
    start_range = 1000
    end_range = 10000
    num_list = list(range(start_range, end_range))
    random.shuffle(num_list)
    id_list = str(num_list[0])
    print(f"Your booking ID is {id_list}.\n")
    with open(file, "a") as file:
        file.write(f"{id_list},")


# Booking info allow customer to input
def booking_info(username):
    while True:
        print("< Departure location >"
              "\n[Enter 'E' to exit.]")

        origin_state = input("Enter Origin State Code Only: ").upper()
        if origin_state == 'E':
            break
        destination_state = input("Enter Destination State Code Only: ").upper()
        print("< Booking Date >")
        month = input("Enter departure month(MM): ")
        while True:
            if len(month) == 2:
                print(f"Booking Month: {month}")
                break
            else:
                print("[Invalid Input]\n")
                month = input("Enter departure month(MM): ")

        day = input("Enter departure day(DD): ")
        while True:
            if len(day) == 2:
                print(f"Booking Day: {day}")
                break
            else:
                print("[Invalid day]\n")
                day = input("Enter departure day(DD): ")

        year = input("Enter departure year(YYYY): ")
        while True:
            if len(year) == 4:
                if year == "2023" or year == "2024":
                    print(f"Departure Year: {year}")
                    break
            else:
                print("[Invalid year]\n")
                year = input("Enter departure year(YYYY): ")

        user_booking = f"{origin_state},{destination_state},{month} {day} {year}"
        with open("flights.txt", "r") as flight_file:
            flight_data = flight_file.readlines()
        for line in flight_data:
            flight_values = line.strip().split(',')
            departure_month = flight_values[7].split(' ')[0]
            departure_day = flight_values[7].split(' ')[1]
            departure_year = flight_values[7].split(' ')[2]
            if (origin_state == flight_values[5] and
                    destination_state == flight_values[6] and
                    month == departure_month and
                    day == departure_day and
                    year == departure_year):
                print("[Booking saved successfully!]\n")
                booking_id()
                with open("booking.txt", "a") as booking_file:
                    booking_file.write(user_booking + "," + username + "\n")
                return

        print("\n[Booking is not available]\n")


# Function to view bookings associated with a specific username
def view_own_bookings(username):
    # Path to the booking file
    booking_file = 'Booking.txt'

    try:
        # Attempt to open the booking file for reading
        with open(booking_file, 'r') as file:
            invalid_format_printed = False  # Reset the flag before processing each line

            # Iterate through each line in the booking file
            for line in file:
                # Extract booking details from the line
                booking_details = line.strip().split(',')

                # Skip empty or insufficient entries
                if len(booking_details) != 5 or not all(booking_details):
                    # Display an error message for invalid booking format
                    if not invalid_format_printed:
                        print("Invalid booking format in the file. Skipping entries with insufficient elements.")
                        invalid_format_printed = True
                    continue

                # Check if the booking belongs to the specified username
                if booking_details[4] == username:
                    # Display details of the booking
                    print(f"Booking ID: {booking_details[0]}\n"
                          f"Origin State: {booking_details[1]}\n"
                          f"Destination State: {booking_details[2]}\n"
                          f"Departure Date: {booking_details[3]}\n" + "-" * 28)

    except FileNotFoundError:
        # Display a message when no bookings are found
        print("[You have no bookings.]\n")


# Function to update an existing booking associated with a specific username
def update_own_booking(username):
    # Path to the booking file
    booking_file = 'booking.txt'

    try:
        # Attempt to open the booking file for reading
        with open(booking_file, 'r') as file:
            # Code to execute if the file exists
            booking_id = input("\nEnter Booking ID to update: ")
            lines = file.readlines()

        # Initialize a flag to track if the booking ID is found
        found = False

        # Iterate through each line in the booking file
        for i, line in enumerate(lines):
            # Extract booking details from the line
            booking_details = line.strip().split(',')

            # Check if booking_details has at least 4 elements and the booking ID matches
            if len(booking_details) >= 5 and booking_details[0] == booking_id:
                # Check if the booking belongs to the specified username
                if booking_details[4] == username:
                    found = True
                    # Display the current booking details
                    print("\n--------/ Current Booking Details /--------")
                    print(f"Booking ID: {booking_details[0]}"
                          f"\nOrigin State: {booking_details[1]}"
                          f"\nDestination State: {booking_details[2]}"
                          f"\nDeparture Date: {booking_details[3]}\n")

                    # Get new booking information from the user
                    new_booking_date = input("Enter new booking date (MM DD YYYY): ")
                    new_departure_state = input("Enter new origin state code: ").upper()
                    new_arrival_state = input("Enter new destination state code: ").upper()

                    # Update the booking information
                    lines[i] = f"{booking_id},{new_departure_state},{new_arrival_state},{new_booking_date},{username}\n"

                    # Check flight availability
                    with open("flights.txt", "r") as flight_file:
                        flight_data = flight_file.readlines()
                    flight_found = False

                    # Iterate through each line in the flight file
                    for flight_line in flight_data:
                        flight_values = flight_line.strip().split(',')

                        # Check if the new flight details match any available flight
                        if (new_departure_state == flight_values[5] and
                                new_arrival_state == flight_values[6] and
                                new_booking_date == flight_values[7]):
                            flight_found = True
                            break

                    if flight_found:
                        # Write the updated booking information back to the file
                        with open(booking_file, 'w') as file:
                            file.writelines(lines)
                        print("[Booking updated successfully.]")
                        break
                    else:
                        print("[Your booking is not available.]")
                else:
                    print("[Your booking is not found.]")

        # Display a message if the booking ID is not found
        if not found:
            print("[Booking ID not found.]\n")

    except FileNotFoundError:
        # Display a message when no bookings are found
        print("[You have no bookings to update.]\n")



# Function to cancel a booking associated with a specific username
def cancel_own_booking(username):
    # Path to the booking file
    booking_file = 'booking.txt'

    try:
        # Attempt to open the file to check if it exists
        with open(booking_file, 'r'):
            pass
    except FileNotFoundError:
        # Display a message when no bookings are found
        print("You have no bookings to cancel.\n")
        return

    # Get Booking ID from user
    booking_id = input("\nEnter Booking ID to cancel: ")

    with open(booking_file, 'r') as file:
        # Read all lines from the booking file
        lines = file.readlines()

    # Initialize a flag to track if the booking ID is found
    found = False

    # Initialize variable to store cancelled booking details
    cancelled_booking = None

    # Iterate through each line in the booking file
    for i, line in enumerate(lines):
        # Extract booking details from the line
        booking_details = line.strip().split(',')

        # Check if the booking ID and username match
        if booking_details[0] == booking_id and booking_details[4] == username:
            found = True
            print("-----Booking Details to Cancel-----")
            print(f"Booking ID: {booking_details[0]}\n"
                  f"Origin State: {booking_details[1]}\n"
                  f"Destination State: {booking_details[2]}\n"
                  f"Departure Date: {booking_details[3]}\n")

            # Ask for confirmation to cancel the booking
            confirmation = input("Are you sure you want to cancel this booking? (yes/no): ").lower()

            # Remove the cancelled booking from the list
            if confirmation == 'yes':
                # Store the cancelled booking
                cancelled_booking = line.strip() + ',Cancelled\n'
            elif confirmation == 'no':
                print("Booking cancellation canceled.\n")
            else:
                print("Invalid input. Cancellation canceled.\n")
            break

    # Display a message if the booking ID is not found
    if not found:
        print("Booking ID not found.\n")
        return

    # Write the non-cancelled bookings back to "booking.txt"
    with open(booking_file, 'w') as file:
        for i, line in enumerate(lines):
            if i != found - 1:  # Skip the line with the cancelled booking
                file.write(line)

    # Write the cancelled booking to "Cancelled_Booking.txt"
    if cancelled_booking:
        with open("Cancelled_Booking.txt", 'a') as cancelled_file:
            cancelled_file.write(cancelled_booking)

    # Display a message if the booking was successfully canceled
    if cancelled_booking:
        print("[Booking canceled successfully.]\n")


# Function to retrieve the customer name associated with a specific username
def get_customer_name(username):
    # Path to the customer file
    file_path = 'customer.txt'

    try:
        # Attempt to open the customer file for reading
        with open(file_path, 'r') as file:
            # Iterate through each line in the customer file
            for line in file:
                # Extract customer data from the line
                data = line.strip().split(',')

                # Check if the data is complete and contains the username
                if len(data) > 6 and any(entry.startswith(username) for entry in data):
                    # Return the customer name (assuming it's the second element)
                    return data[0]
    except FileNotFoundError:
        # Display a message when the file is not found
        print("File not found.")
        return None

    # Return None if the username or data is not found
    return None


# Function to generate a seat number based on row and column indices
def generate_seat_number(row, column):
    # Define the column letters for seat numbering
    column_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Extract the column letter based on the provided column index
    column_letter = column_letters[column] if column < len(column_letters) else ''

    # Combine the column letter and row index to form the seat number
    seat_number = f"{column_letter}{row}"

    # Return the generated seat number
    return seat_number


# Function to perform self-check-in and generate a boarding pass
def self_check_in(username):
    # Define the file paths for booking and boarding pass
    booking_file = 'booking.txt'
    boarding_pass_file = 'BoardingPass.txt'

    try:
        # Attempt to open the booking file for reading
        with open(booking_file, 'r') as file:
            # Read all lines from the booking file
            lines = file.readlines()
    except FileNotFoundError:
        # Display a message when no booking file is found
        print("\nNo booking found. Please make a booking first.")
        return

    valid_booking_details = None

    # Iterate through lines in reverse to find the latest valid booking details
    for line in reversed(lines):
        booking_details = line.strip().split(',')
        if len(booking_details) == 5:
            valid_booking_details = booking_details
            break

    if valid_booking_details is None:
        # Display a message for invalid booking details
        print("\nInvalid booking details.")
        return

    # Retrieve the passenger name using the get_customer_name function
    passenger_name = get_customer_name(username)

    if passenger_name is None:
        # Display a message when customer details are not found
        print("\nCustomer details not found.")
        return

    # Use the generate_seat_number function with appropriate parameters to create a seat number
    seat_number = generate_seat_number(3, 2)

    # Prepare boarding pass information
    boarding_pass_info = (f"Passenger Name: {username}\nFlight Number: {valid_booking_details[0]}"
                          f"\nSeat Number: {seat_number}\nOrigin State: {valid_booking_details[1]}"
                          f"\nDestination State: {valid_booking_details[2]}\nDeparture Date: {valid_booking_details[3]}")

    try:
        # Attempt to open the boarding pass file for appending
        with open(boarding_pass_file, 'a') as file:
            # Write boarding pass information to the file
            file.write("< Boarding Pass >\n")
            file.write(boarding_pass_info + '\n')
    except FileNotFoundError:
        # Display an error message when unable to create a boarding pass
        print("\nError creating boarding pass. Please check your booking details.")
        return

    # Display a success message for self-check-in
    print("Self-check-in successful! Boarding pass generated.")


# Function to display user profile information based on the provided username
def view_profile(username):
    # Define the file path for the customer information
    file_path = "customer.txt"

    # Attempt to open the customer file for reading
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Extract user details from the line
            user = line.strip().split(',')

            # Check if the user has at least 7 elements and the username matches
            if len(user) >= 7 and user[0] == username:
                # Prepare user information string
                user_info = (f"Username: {user[0]}\n"
                             f"Contact Number: {user[2]}\n"
                             f"Email ID: {user[3]}\n"
                             f"Address: {user[4]}\n"
                             f"Gender: {user[5]}\n"
                             f"Date of Birthday: {user[6]}\n")

                # Display the profile information
                print("\n-----View Profile-----")
                print(user_info)


# Function to update the profile information associated with a specific username
def update_profile(username):
    # Path to the customer file
    file_path = 'customer.txt'

    try:
        # Attempt to open the customer file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    found = False
    for i, line in enumerate(lines):
        data = line.strip().split(',')

        # Check if the line has at least 1 element and matches the specified username
        if len(data) >= 1 and data[0] == username:
            found = True
            print("Profile found!\n")

            # Display current profile
            print("--------/ Current Profile /--------")
            print(f"Username: {data[0]}\n"
                  f"Contact Number: {data[2]}\n"
                  f"Email ID: {data[3]}\n"
                  f"Address: {data[4]}\n"
                  f"Gender: {data[5]}\n"
                  f"Date of Birthday: {data[6]}\n")

            # Update profile
            print("--------/ Update Profile /--------")
            field_to_update = input("1. Username\n"
                                    "2. Contact Number\n"
                                    "3. Email ID\n"
                                    "4. Address\n"
                                    "5. Gender\n"
                                    "6. Date of Birthday\n"
                                    "Enter the number you want to update: ").strip()

            # Get the new value for the specified field
            new_value = input(f"Enter the new value for {field_to_update}: ")

            # Update the specified field
            if field_to_update == '1':
                data[0] = new_value
            elif field_to_update == '2':
                data[2] = new_value
            elif field_to_update == '3':
                data[3] = new_value
            elif field_to_update == '4':
                data[4] = new_value
            elif field_to_update == '5':
                data[5] = new_value
            elif field_to_update == '6':
                data[6] = new_value
            else:
                print("[Invalid input]")

            # Update data in the lines list
            lines[i] = ','.join(data) + '\n'

            try:
                # Write the updated data back to the customer file
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print("Profile updated successfully.")
            except Exception as e:
                print(f"Error updating file: {e}")
            break

    if not found:
        print("Profile not found.")


# Function to delete the profile associated with a specific username
def delete_profile(username):
    # Path to the customer file
    file_path = 'customer.txt'

    try:
        # Attempt to open the customer file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    found = False
    updated_lines = []  # To store lines that will be kept

    for i, line in enumerate(lines):
        data = line.strip().split(',')

        # Check if the line has at least 1 element and matches the specified username
        if len(data) >= 1 and data[0] == username:
            found = True
            print("Profile found!")
            print("\nProfile Information to Delete:")
            print(f"Name: {data[0]}")
            confirmation = input("Are you sure you want to delete this account? (yes/no): ").lower()
            if confirmation == 'yes':
                # Do not add the line to updated_lines, effectively skipping it
                print("Profile deleted successfully.")
                break  # Exit the loop immediately after deleting the profile
            elif confirmation == 'no':
                print("Profile failed to delete. Go back to Login.")
                return  # Exit the function immediately after failing to delete the profile
            else:
                print("Invalid input. Deletion canceled.")
        else:
            # Add the line to updated_lines as it should be kept
            updated_lines.append(line)

    if found:
        try:
            # Write the updated data back to the customer file
            with open(file_path, 'w') as file:
                file.writelines(updated_lines)
        except Exception as e:
            print(f"Error updating file: {e}")

    if not found:
        print("Profile not found.")


# Reset password
def change_password(username):
    file_path = 'customer.txt'
    lines = []

    # Read all lines from the file and store them in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    found = False
    for i, line in enumerate(lines):
        user = line.strip().split(',')
        if len(user) >= 7 and user[0] == username:
            found = True

            while True:
                old_password = input("Please enter your old password: ")
                if old_password == user[1]:
                    new_password = input("Please enter your new password: ")
                    confirm_new_password = input("Please confirm your password: ")
                    if new_password == confirm_new_password:
                        # Update the password in the list
                        user[1] = new_password
                        lines[i] = ','.join(user) + '\n'

                        # Write the updated list back to the file
                        with open(file_path, 'w') as file:
                            file.writelines(lines)

                        print("Password changed successfully.")
                        break
                    else:
                        print("Password does not match. Please try again.")
                else:
                    print("Incorrect old password. Please try again.")
            break

    if not found:
        print("User not found.")


def profile(username):
    while True:
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Delete Profile")
        print("4. Reset Password")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            view_profile(username)
        elif choice == '2':
            update_profile(username)
        elif choice == '3':
            delete_profile(username)
        elif choice == '4':
            change_password(username)
        elif choice == '5':
            customer_login()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Coding
while True:
    interface()
    print("\n(1)I am Customer."
          "\n(2)I am Administrator.")
    choose_user = input("\nWho are you?\nPlease select '1' or '2': ")
    # Customer register/login Interface
    if choose_user == '1':
        print("[You will proceed to customer interface.]")
        while True:
            enter_system = input("\na. Register (New User)\nb. Login\nc. Exit \nChoose above option: ")
            if enter_system.lower() == "a":
                register_customer()
                customer_login()
                break

            elif enter_system.lower() == "b":
                customer_login()
                break

            elif enter_system.lower() == "c":
                break

            else:
                print("[Invalid value, please check again.]")
                continue

    # Admin login Interface
    elif choose_user == '2':
        print("[You will proceed to administrator interface.]\n")
        while True:
            print("1. Login\n2. Exit")
            cho = input(">>> ")
            if cho == '1':
                exit_value = admin_login()
                if exit_value == 0:
                    admin_interface()
                    break
                if exit_value == 1:  # if user enters 'e' it will restart main file
                    break
            elif cho == '2':
                break
            else:
                print("[Invalid choice. Please select '1' or '2' only.]")
                continue
    else:
        print("[Invalid value. Please check back.]")
