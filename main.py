# Пользовательское исключение
class GroupLimitError(Exception):  # Исключение, которое выбрасывается, если группа переполнена
    def __init__(self, message="Group size limit exceeded"):
        super().__init__(message)


# Модифицированный класс Group
class Group:
    def __init__(self, number, max_size=10):  # Конструктор задает номер группы и максимальный размер
        self.number = number
        self.max_size = max_size
        self.group = set()  # Используем множество для хранения студентов

    def add_student(self, student):  # Добавление студента в группу
        if len(self.group) >= self.max_size:  # Проверяем, не превышен ли лимит
            raise GroupLimitError(f"Cannot add more than {self.max_size} students to the group.")
        self.group.add(student)  # Если лимит не превышен, добавляем студента в множество

    def delete_student(self, last_name):  # Удаление студента из группы
        for student in self.group:
            if student.last_name == last_name:  # Находим студента по фамилии
                self.group.remove(student)  # Удаляем его из группы
                return  # Прекращаем после удаления, так как студент найден

    def find_student(self, last_name):  # Поиск студента по фамилии
        for student in self.group:
            if student.last_name == last_name:
                return student  # Возвращаем найденного студента
        return None  # Если студент не найден, возвращаем None

    def __str__(self):  # Возвращаем строковое представление группы
        all_students = '\n'.join(str(student) for student in self.group)  # Собираем всех студентов в строку
        return f"Number: {self.number}\nStudents:\n{all_students}"



class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


# Класс Student модифицирован для поддержки множества (hashable)
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):  # Возвращаем строковое представление студента
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):  # Определяем равенство студентов
        if not isinstance(other, Student):  # Проверяем, что другой объект — это Student
            return NotImplemented
        return (self.first_name, self.last_name, self.record_book) == (
            other.first_name,
            other.last_name,
            other.record_book,
        )

    def __hash__(self):  # Определяем хэш, чтобы студент стал hashable
        return hash((self.first_name, self.last_name, self.record_book))


# Тестирование
try:
    # Создаем студентов
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Female', 20, 'Anna', 'Smith', 'AN148')
    st4 = Student('Male', 22, 'Tom', 'Hanks', 'AN150')
    st5 = Student('Female', 19, 'Emily', 'Blunt', 'AN155')
    st6 = Student('Male', 21, 'Chris', 'Evans', 'AN160')
    st7 = Student('Female', 23, 'Scarlett', 'Johansson', 'AN165')
    st8 = Student('Male', 24, 'Robert', 'Downey', 'AN170')
    st9 = Student('Female', 26, 'Natalie', 'Portman', 'AN175')
    st10 = Student('Male', 27, 'Mark', 'Ruffalo', 'AN180')
    st11 = Student('Female', 28, 'Gal', 'Gadot', 'AN185')

    # Создаем группу
    gr = Group('PD1')
    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

    # Добавляем студентов
    for student in students:
        gr.add_student(student)
        print(f"Added {student.first_name} {student.last_name} to the group.")

except GroupLimitError as e:  # Обрабатываем переполнение группы
    print(f"Error: {e}")

# Выводим содержимое группы
print(gr)