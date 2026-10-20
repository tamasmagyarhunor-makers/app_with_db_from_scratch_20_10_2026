class Pokemon():
    def __init__(self, id, name, power_type):
        self.id = id
        self.name = name
        self.power_type = power_type
    
    def __repr__(self):
        return f"Pokemon({self.id}, {self.name}, {self.power_type})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
