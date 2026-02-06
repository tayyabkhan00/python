class Phone:
    def call(self):
        print("Calling...")

class Camera:
    def take_photo(self):
        print("Photo taken")

# Multiple Inheritance
class SmartPhone(Phone, Camera):
    def browse(self):
        print("Browsing internet")

# Create object
sp = SmartPhone()

sp.call()        # from Phone
sp.take_photo()  # from Camera
sp.browse()      # from SmartPhone
