next_uid = 1

class User:
    def __init__(self, name):
        global next_uid
        self.name = name
        self.__id = next_uid
        next_uid += 1

u = User("Mary")
print(f'name={u.name}, id={u._User__id}')
u = User("Princess")
print(f'name={u.name}, id={u._User__id}')

