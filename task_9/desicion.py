class Temperature:
    def __init__(self, celsium: float):
        self._celsium = celsium

    @property
    def celsium(self):
        return self._celsium

    @celsium.setter
    def celsium(self, value):
        if value < -273.15:
            raise ValueError('Температура не может быть ниже - 273,15 С')
        self._celsium = value


if __name__ == '__main__':
    temp = Temperature(50)
    print(temp.celsium)
    temp.celsium = -300
