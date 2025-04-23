import Pyro5.api

@Pyro5.api.expose
class HotelBookingSystem:
    def __init__(self):
        self.bookings = {}  # room_number -> guest_name

    def book_room(self, room_number, guest_name):
        if room_number in self.bookings:
            return f"Room {room_number} is already booked by {self.bookings[room_number]}"
        self.bookings[room_number] = guest_name
        return f"Room {room_number} successfully booked for {guest_name}"

    def cancel_booking(self, room_number):
        if room_number in self.bookings:
            guest = self.bookings.pop(room_number)
            return f"Booking for {guest} in room {room_number} cancelled."
        return f"No booking found for room {room_number}."

    def list_bookings(self):
        if not self.bookings:
            return "No current bookings."
        return "\n".join(f"Room {r}: {g}" for r, g in self.bookings.items())

def main():
    daemon = Pyro5.server.Daemon()
    uri = daemon.register(HotelBookingSystem)
    print("Hotel Booking Server is ready.")
    print("Object URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
