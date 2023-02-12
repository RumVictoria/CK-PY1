import doctest


class Art:
    """ Базовый класс "Набор картин". """

    def __init__(self, subject: str, canvas_width: (int, float), canvas_height: (int, float)):
        """
        Создание и подготовка к работе объекта класса "Набор картин"

        :param subject: Тематика картины
        :param canvas_width: Ширина холста, см
        :param canvas_height: Высота холста, см

        Примеры:
        >>> art1 = Art("Кот", 50, 80)
        """
        self._subject = subject
        self._canvas_width = canvas_width
        self._canvas_height = canvas_height

    @property
    def subject(self):
        """
        Метод определяет свойства атрибута "Тематика картины"
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Метод проверяет условия возможных значений атрибута "Тематика картины"
        """
        if not isinstance(subject, str):
            raise TypeError("Тематика картины должны быть описана строкой")
        self._subject = subject

    @property
    def canvas_width(self):
        """
        Метод определяет свойства атрибута "Ширина холста"
        """
        return self._canvas_width

    @canvas_width.setter
    def canvas_width(self, canvas_width):
        """
        Метод проверяет условия возможных значений атрибута "Ширина холста"
        """
        if not isinstance(canvas_width, (int, float)):
            raise TypeError("Ширина холста должна быть описана числом")
        if not 0 < canvas_width:
            raise ValueError("Ширина холста должна быть положительным числом")
        self._canvas_width = canvas_width

    @property
    def canvas_height(self):
        """
        Метод определяет свойства атрибута "Высота холста"
        """
        return self._canvas_height

    @canvas_height.setter
    def canvas_height(self, canvas_height):
        """
        Метод проверяет условия возможных значений атрибута "Высота холста"
        """
        if not isinstance(canvas_height, (int, float)):
            raise TypeError("Высота холста должна быть описана числом")
        if not 0 < canvas_height:
            raise ValueError("Высота холста должна быть положительным числом")
        self._canvas_height = canvas_height

    def __str__(self) -> str:
        """
        Метод возвращает информацию об объекте в виде строки

        Примеры:
        >>> art1 = Art("Кот", 50, 80)
        >>> art1.__str__()
        'Тематика: Кот. Габариты холста (шхв): 50 х 80 см'
        """
        return f"Тематика: {self.subject}. Габариты холста (шхв): {self.canvas_width} х {self.canvas_height} см"

    def __repr__(self):
        """
        Метод возвращает информацию об объекте в виде строки Python

        Примеры:
        >>> art1 = Art("Кот", 50, 80)
        >>> art1.__repr__()
        "Art(subject='Кот', canvas_width=50, canvas_height=80)"
        """
        return f"{self.__class__.__name__}(subject={self.subject!r}, canvas_width={self.canvas_width!r}, " \
               f"canvas_height={self.canvas_height!r})"

    @staticmethod
    def ready(current_volume: int, full_volume: int):
        """
        Метод показывает процент готовности картины

        Примеры:
        >>> art1 = Art("Кот", 50, 80)
        >>> art1.ready(8, 16)
        'Процент готовности: 50.0%'
        """
        return f"Процент готовности: {current_volume / full_volume * 100}%"

    def area(self):
        """
        Метод показывает площадь рабочей области картины

        Примеры:
        >>> art1 = Art("Кот", 50, 80)
        >>> art1.area()
        'Площадь рабочей области: 4000 см2'
        """
        return f"Площадь рабочей области: {self.canvas_width * self.canvas_height} см2"


class Coloring(Art):
    """ Дочерний класс "Картина по цветам". """

    def __init__(self, subject: str, canvas_width: (int, float), canvas_height: (int, float), paint_number: int):
        """
        Создание и подготовка к работе объекта подкласса "Картина по цветам"

        :param subject: Тематика картины (унаследованный)
        :param canvas_width: Ширина холста, см (унаследованный)
        :param canvas_height: Высота холста, см (унаследованный)
        :param paint_number: Количество цветов, шт

        Примеры:
        >>> coloring1 = Coloring("Птица", 20, 40, 15)
        """
        super().__init__(subject, canvas_width, canvas_height)
        self._paint_number = paint_number

    @property
    def paint_number(self):
        """
        Метод определяет свойства атрибута "Количество цветов"
        """
        return self._paint_number

    @paint_number.setter
    def paint_number(self, paint_number):
        """
        Метод проверяет условия возможных значений атрибута "Количество цветов"
        """
        if not isinstance(paint_number, int):
            raise TypeError("Количество цветов должно быть целым числом")
        if not 0 < paint_number:
            raise ValueError("Количество цветов должно быть положительным числом")
        self._paint_number = paint_number

    def __str__(self):
        """
        Перегрузка метода базового класса по причине добавления нового атрибута

        Примеры:
        >>> coloring1 = Coloring("Птица", 20, 40, 15)
        >>> coloring1.__str__()
        'Тематика: Птица. Габариты холста (шхв) 20 х 40. Количество цветов: 15.'
        """
        return f"Тематика: {self.subject}. Габариты холста (шхв) {self.canvas_width} х {self.canvas_height}. " \
               f"Количество цветов: {self.paint_number}."

    def __repr__(self):
        """
        Метод возвращает информацию об объекте в виде строки Python

        Примеры:
        >>> coloring1 = Coloring("Птица", 20, 40, 15)
        >>> coloring1.__repr__()
        "Coloring(subject='Птица', canvas_width=20, canvas_height=40, paint_number=15)"
        """
        return f"{self.__class__.__name__}(subject={self.subject!r}, canvas_width={self.canvas_width!r}, " \
               f"canvas_height={self.canvas_height!r}, paint_number={self.paint_number!r})"


class Mosaic(Art):
    """ Дочерний класс "Алмазная мозаика". """

    def __init__(self, subject: str, canvas_width: (int, float), canvas_height: (int, float), border: int):
        """
        Создание и подготовка к работе объекта подкласса "Алмазная мозаика"

        :param subject: Тематика картины (унаследованный)
        :param canvas_width: Ширина холста, см (унаследованный)
        :param canvas_height: Высота холста, см (унаследованный)
        :param border: Ширина ограничительных полей холста, см

        Примеры:
        >>> mosaic1 = Mosaic("Цветок", 35, 60, 3)
        """
        super().__init__(subject, canvas_width, canvas_height)
        self._border = border

    def __repr__(self):
        """
        Метод возвращает информацию об объекте в виде строки Python

        Примеры:
        >>> mosaic1 = Mosaic("Цветок", 35, 60, 3)
        >>> mosaic1.__repr__()
        "Mosaic(subject='Цветок', canvas_width=35, canvas_height=60, border=3)"
        """
        return f"{self.__class__.__name__}(subject={self.subject!r}, canvas_width={self.canvas_width!r}, " \
               f"canvas_height={self.canvas_height!r}, border={self._border!r})"

    def area(self):
        """
        Перегрузка метода базового класса "Площадь рабочей области" с учетом полей на холсте

        Примеры:
        >>> mosaic1 = Mosaic("Цветок", 35, 60, 3)
        >>> mosaic1.area()
        'Площадь рабочей области: 1566 см2'
        """
        return f"Площадь рабочей области: {(self._canvas_width - 2 * self._border) * (self._canvas_height - 2 * self._border)} см2"


if __name__ == "__main__":
    doctest.testmod()
    pass
