import random

# Списки имен и окончаний
beginnings = ["Ба", "Бе", "Бо", "Бу", "Ва", "Ве", "Во", "Ву", "Га", "Ге", "Го", "Гу"]
endings = ["рд", "льф", "гги", "ван", "нек", "ша", "тас", "рик", "шон", "сто"]

# Генерируем случайное имя для собаки
beginning = random.choice(beginnings)
ending = random.choice(endings)
name = beginning + ending

print("Имя для собаки:", name)
