class Pogi:

    def __init__(self, first, last, sex):
        self.first = first
        self.last = last
        self.sex = sex

    def display_info(self):
        if self.sex == 'M':
            print(f'Hi, {self.first} {self.last}! Is your phone number 69? Hihe')
        else:
            print(f'Hi, {self.first} {self.last}! Is your phone number beach?')



person1 = Pogi('Earl', 'Paquibol', 'M')
person1.display_info()
