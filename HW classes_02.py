class Human:
    __id_set = set()  # Множество для хранения занятых ID

    def __init__(self, full_name, id=None):
        self.full_name = full_name
        if id is None:
            self.__id = self.__generate_unique_id()
        else:
            if id in self.__id_set:
                raise Exception("Переданный ID уже существует!")
            self.__id = id
            self.__id_set.add(id)

    def __generate_unique_id(self):
        new_id = 1
        while new_id in self.__id_set:
            new_id += 1
        self.__id_set.add(new_id)
        return new_id

    def __lt__(self, other):
        return self.full_name < other.full_name

    def __hash__(self):
        return hash(self.full_name)

    def __repr__(self):
        return f"Human({self.full_name}, {self.__id})"

    def __str__(self):
        return f"Full Name: {self.full_name}, ID: {self.__id}"

    @staticmethod
    def read_csv(filename):
        # Чтение информации из CSV файла и создание объектов Human
        pass

    @staticmethod
    def write_csv(filename, humans):
        # Запись информации об объектах Human в CSV файл
        pass

# Пример использования класса Human
human1 = Human("Иванов Иван Иванович")
human2 = Human("Петров Петр Петрович")

print(human1)
print(human2)
print(human1 < human2)
