class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        print(f"{self.phone_number} called {other_phone.phone_number}")
        self.call_history.append(f"{self.phone_number} called {other_phone.phone_number}")

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone):
        dict = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": "message"
        }
        self.messages.append(dict)

    def show_outgoing_messages(self):
        print(self.messages)


itay = Phone("0508220")
shani = Phone("0502249")

itay.call(shani)
itay.send_message(shani)
itay.show_outgoing_messages()
