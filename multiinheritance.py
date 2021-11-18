class Human:

    is_mammal = True

    def __init__(self, name, birth_date, height, sex='m', race='White'):
        self.name = name
        self.birth_date = birth_date
        self.height = height
        self.sex = sex
        self.race = race

    def work(self):
        print('I do not work')


class Employee:

    def __init__(self, salary=0, working_hours=8, vacation=30):
        self.salary = salary
        self.working_hours = working_hours
        self.vacation = vacation

    def work(self):
        print("I am working")


class Manager(Human, Employee):

    def __init__(self, name, birth_date, height, sex, race,
                 salary, vacation, working_hours=8):
        Human.__init__(self, name, birth_date, height, sex, race)
        Employee.__init__(self, salary, working_hours, vacation)

    def __str__(self):
        return f'{self.__class__.__name__} name = {self.name}, birthdate = {self.birth_date}' \
               f' height = {self.height}, sex = {self.sex}, race = {self.race},' \
               f'salary = {self.salary}, working_hours = {self.working_hours},' \
               f'vacation = {self.vacation}'


# manager = Manager('Иван Дмитров', '17-04-1994', 173, 'm', 'White',
#                   5000, 30, working_hours=None)
# print(manager)
# manager.work()
#
# # MRO -> Method Resolution Order
# print(Manager.mro())
