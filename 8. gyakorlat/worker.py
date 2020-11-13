
class Worker:

    def __init__(self, id, name, address, phone_number, email):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, ph):
        self.__phone_number = ph

    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"{self.get_id()},{self.get_name()},{self.get_address()},{self.get_phone_number()},{self.get_email()}"

    def __lt__(self, other):
        return self.get_id() < other.get_id()

    def __le__(self, other):
        return self.get_id() <= other.get_id()

    def __ge__(self, other):
        return self.get_id() >= other.get_id()

    def __gt__(self, other):
        return self.get_id() > other.get_id()

    def __eq__(self, other):
        return self.get_id() == other.get_id()
