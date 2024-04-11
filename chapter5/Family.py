class Family:
    last_name = "Shim"
    def __init__(self, first_name):
        self.first_name = first_name
    def __str__(self):
        return f'{self.last_name} {self.first_name}'