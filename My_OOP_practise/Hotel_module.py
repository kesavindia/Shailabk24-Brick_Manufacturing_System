class Hotel:
    hotel_name = "Ashoka"
    city = "Madurai"
    email = "john@gmail.com"

    @classmethod
    def printmail(cls):
        print(cls.email)

class Customer(Hotel):
    def __init__(self, name, phone, roomRent, id_proof, email):
        self.name = name
        self.phone = phone
        self.roomRent = roomRent
        self.id_proof = id_proof
        self.email = email
        self.checked_in = False

    def __str__(self):
        return f"{self.name} ({self.email})"

    def presence(self):
        if not self.checked_in:
            self.checked_in = True
            print(f"{self.name} has checked into the room.")
        else:
            print(f"{self.name} is already checked into the room.")

Kesavan = Customer("Kesavan", 7019502821, 3000, "Aadhar", "kesa@gmail.com")
Kumaran = Customer("Kumaran", 7019502822, 3000, "Aadhar", "kesav1@gmail.com")
Ragavan = Customer("Ragavan", 7019502823, 3000, "Aadhar", "kesav2@gmail.com")
Madavan = Customer("Madavan", 7019502824, 3000, "Aadhar", "kesav3@gmail.com")
Yadavan = Customer("Yadavan", 7019502825, 3000, "Aadhar", "kesa5@gmail.com")
Govindan = Customer("Govindan", 7019502826, 3000, "Aadhar", "kesav@gmail.com")

print(Govindan.email)
print(Hotel.city)

Kesavan.presence()
