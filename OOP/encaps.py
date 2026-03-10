class speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 50
s = speed()
print(s.__new_speed)
print(s.speed)