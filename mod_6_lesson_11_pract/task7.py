class GameSettings:
    _instance = None
    _initialized = False # Флаг для однократной инициализации

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.difficulty = "Normal"
        self.sound_volume = 75
        self._initialized = True

    def set_difficulty(self, level):
        self.difficulty = level

    def set_sound_volume(self, volume):
        self.sound_volume = volume

    def display_settings(self):
        print(f"Сложность: {self.difficulty}, Громкость: {self.sound_volume}")


# Пример использования
settings1 = GameSettings()
settings1.display_settings()

settings2 = GameSettings()
settings2.set_difficulty('Hard')
settings2.set_sound_volume(90)

# settings1 и settings2 должны быть одним и тем же объектом
settings1.display_settings()
print(f"settings1 is settings2: {settings1 is settings2}")
