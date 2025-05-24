from abc import ABC, abstractmethod


# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"1. Student - Name: {self.name}, Marks: {self.marks}")


# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"2. Counter - Number of objects created: {cls.count}")


# 3. Public Variables and Methods
class Car:
    def _init_(self, brand):
        self.brand = brand

    def start(self):
        print(f"3. Car - {self.brand} is starting.")


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def display_bank_name(cls):
        print(f"4. Bank - Bank name: {cls.bank_name}")


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("6. Logger - Logger created.")

    def __del__(self):
        print("6. Logger - Logger destroyed.")


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super()._init_(name)
        self.subject = subject


# 9. Abstract Classes and Methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"10. Dog - {self.name} says Woof!")


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"11. Book - Total books: {cls.total_books}")


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# 13. Composition
class Engine:
    def start(self):
        print("13. Engine - Engine starting.")


class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


# 14. Aggregation
class DeptEmployee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, employee):
        self.employee = employee


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("15. A's show")


class B(A):
    def show(self):
        print("15. B's show")


class C(A):
    def show(self):
        print("15. C's show")


class D(B, C):
    pass


# 16. Function Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("16. Function is being called")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def say_hello():
    print("16. Hello!")


# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "17. Hello from Decorator!"
    return cls


@add_greeting
class PersonDecorated:
    pass


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# 19. callable() and _call_()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val


# Run examples
if __name__ == "__main__":
    # 1
    s = Student("Alice", 85)
    s.display()

    # 2
    c1 = Counter()
    c2 = Counter()
    Counter.display_count()

    # 3
    car = Car("Toyota")
    print(car.brand)
    car.start()

    # 4
    b1 = Bank()
    Bank.display_bank_name()
    Bank.change_bank_name("New Bank")
    Bank.display_bank_name()

    # 5
    print("5. MathUtils - Add: ", MathUtils.add(5, 3))

    # 6
    logger = Logger()
    del logger

    # 7
    emp = Employee("John", 50000, "123-45-6789")
    print(f"7. Employee - Public: {emp.name}")
    print(f"7. Employee - Protected: {emp._salary}")
    try:
        print(emp.__ssn)
    except AttributeError:
        print("7. Employee - Private: Cannot access __ssn directly")

    # 8
    t = Teacher("Mr. Smith", "Math")
    print(f"8. Teacher - Name: {t.name}, Subject: {t.subject}")

    # 9
    rect = Rectangle(5, 3)
    print(f"9. Rectangle - Area: {rect.area()}")

    # 10
    d = Dog("Buddy", "Golden Retriever")
    d.bark()

    # 11
    Book.increment_book_count()
    Book.increment_book_count()
    Book.display_total_books()

    # 12
    print(f"12. Celsius to Fahrenheit (25°C): {TemperatureConverter.celsius_to_fahrenheit(25)}")

    # 13
    engine = Engine()
    car_with_engine = CarWithEngine(engine)
    car_with_engine.start()

    # 14
    emp2 = DeptEmployee("Alice")
    dept = Department(emp2)
    print(f"14. Department's employee name: {dept.employee.name}")

    # 15
    d_obj = D()
    d_obj.show()
    print(f"15. MRO:", [cls._name_ for cls in D._mro_])

    # 16
    say_hello()

    # 17
    p_dec = PersonDecorated()
    print(p_dec.greet())

    # 18
    product = Product(100)
    print(f"18. Product price: {product.price}")
    product.price = 150
    print(f"18. Updated price: {product.price}")
    del product.price

    # 19
    multiplier = Multiplier(3)
    print(f"19. callable(multiplier): {callable(multiplier)}")
    print(f"19. multiplier(5): {multiplier(5)}")

    # 20
    try:
        check_age(16)
    except InvalidAgeError as e:
        print(f"20. InvalidAgeError caught: {e}")

    # 21
    print("21. Countdown:")
    for number in Countdown(5):
        print(number)