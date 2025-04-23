import Pyro5.api

def main():
    uri = input("Enter the URI of the remote hotel booking object: ")
    hotel = Pyro5.api.Proxy(uri)

    while True:
        print("\n--- Hotel Booking Menu ---")
        print("1. Book Room")
        print("2. Cancel Booking")
        print("3. List Bookings")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            room = input("Enter room number: ")
            guest = input("Enter guest name: ")
            print(hotel.book_room(room, guest))
        elif choice == "2":
            room = input("Enter room number: ")
            print(hotel.cancel_booking(room))
        elif choice == "3":
            print(hotel.list_bookings())
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
