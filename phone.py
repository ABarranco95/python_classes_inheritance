class Phone():
    """ This is a phone class that can be used for inheritance purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f'Calling number: {other_number}')

    def text(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f'Opening {app_name}')



class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print(f'Phone unlocked')

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery >= 100:
            self.battery = 100
            print(f'Phone is now fully charged')

    def view_phone_number(self):
        print(f'Phone number: {self.phone_number}')



frank_phone = Android('888-767-1923', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(150)
frank_phone.view_battery_life()
frank_phone.call('310-743-3243')


class Iphone(phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 100

    def __str__(self):
        return f'This iphone belongs to number {self.phone_number}'

    def set_passcode(self, passcode):
        self.passcode = passcode
        return f'You have successfully added a passcode to your phone.'