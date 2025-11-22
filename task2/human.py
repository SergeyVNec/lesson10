class Human:
    def __init__(self, name: str):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "This is a static message."
