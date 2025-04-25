class TV:
    def __init__(self):
        self._volume = 50

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = max(0, min(value, 100))


if __name__ == '__main__':
    tv = TV()
    tv.volume = 120
    print(tv.volume)
