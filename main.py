# TODO: Добавить проверку на пустой ввод
from faker import Faker

faker_instance = Faker()
print("Случайное имя:", faker_instance.name())
print("Случайный адрес:", faker_instance.address())
