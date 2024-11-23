

class Videocard:
    def __init__(self, id, name, price, memory, core, frequency, memory_type):
        self.id = id
        self.name = name
        self.price = price
        self.memory = memory
        self.core = core
        self.frequency = frequency
        self.memory_type = memory_type

    def __str__(self):
        return (f"id: {self.id}\n"
                f"Название: {self.name}\n" 
                f"Цена: {self.price}\n" 
                f"Память: {self.memory}\n" 
                f"Количество ядер: {self.core}\n" 
                f"Частота: {self.frequency}\n" 
                f"Тип памяти: {self.memory_type}\n")

    def get_headers(self):
        return ["ID", "Название", "Цена", "Память", "Количество ядер", "Частота", "Тип памяти"]

    def get_data(self):
        return [self.id, self.name, self.price, self.memory, self.core, self.frequency, self.memory_type]