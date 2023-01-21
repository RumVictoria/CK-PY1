from typing import Union
import doctest


class FatCat:
    def __init__(self, weight: Union[int, float], eaten_food: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Толстый кот"

        :param weight: Вес котика, кг
        :param eaten_food: Количество съеденной еды, кг

        Примеры:
        >>> fat_cat1 = FatCat(4, 0.1)
        """
        self.weight = None
        self.init_weight(weight)
        self.eaten_food = None
        self.init_eaten_food(eaten_food)

    def init_weight(self, weight: Union[int, float]):
        """
        Метод проверяет условия возможных значений атрибута "Вес котика"
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес котика должен быть типа int или float")
        if not weight > 0:
            raise ValueError("Вес котика должен быть положительным числом")
        self.weight = weight

    def init_eaten_food(self, eaten_food: Union[int, float]):
        """
        Метод проверяет условия возможных значений атрибута "Количество съеденной еды"
        """
        if not isinstance(eaten_food, (int, float)):
            raise TypeError("Количество съеденной еды должно быть типа int или float")
        if not eaten_food >= 0:
            raise ValueError("Количество съеденной еды должно быть положительным числом")
        self.eaten_food = eaten_food

    def is_satisfied(self) -> bool:
        """
        Метод, который проверяет доволен ли котик

        :return : Доволен ли котик

        Примеры:
        >>> fat_cat1 = FatCat(4, 0)
        >>> fat_cat1.is_satisfied()
        """
        ...

    def pet_the_cat(self) -> None:
        """
        Метод, который гладит котика

        Примеры:
        >>> fat_cat1 = FatCat(4, 0)
        >>> fat_cat1.pet_the_cat()
        """
        ...


class Candle:
    def __init__(self, wick: bool, flavor: str, flame: bool):
        """
        Создание и подготовка к работе объекта "Свеча"

        :param wick: Наличие фитиля
        :param flavor: Наименование аромата
        :param flame: Показатель горения свечи

        Примеры:
        >>> candle1 = Candle(True, "Cotton candy", False)
        """
        if not isinstance(wick, bool):
            raise TypeError("Наличие фитиля должно быть описано значениями True или False")
        self.wick = wick

        if not isinstance(flavor, str):
            raise TypeError("Наименование аромата должно быть типа str")
        self.flavor = flavor

        if not isinstance(flame, bool):
            raise TypeError("Показатель горения свечи должен быть типа bool")
        self.flame = flame

    def light_the_candle(self) -> None:
        """
        Зажечь свечу

        :raise ValueError: Если фитиль отсутствует, то вызываем ошибку
        :raise ValueError: Если свеча зажжена, то вызываем ошибку

        Примеры:
        >>> candle1 = Candle(True, "Cotton candy", False)
        >>> candle1.light_the_candle()
        """
        if not self.wick:
            raise ValueError("Чтобы зажечь свечу, нужен фитиль")
        if self.flame:
            raise ValueError("Свеча уже горит")
        ...

    def put_out_the_candle(self) -> None:
        """
        Потушить свечу

        :raise ValueError: Если свеча не горит, то вызываем ошибку

        Примеры:
        >>> candle1 = Candle(True, "Cotton candy", True)
        >>> candle1.put_out_the_candle()
        """
        if not self.flame:
            raise ValueError("Свечу можно потушить только в том случае, если она горит")
        ...


class Moodle:
    def __init__(self, max_online: int, online: int, institute: str):
        """
        Создание и подготовка к работе объекта "Мудл"

        :param max_online: Максмально поддерживаемое количество пользователей на сайте
        :param online: Текущее количество пользователей на сайте
        :param institute: Название институа, для которого предназначен сайт

        Примеры:
        >>> moodle1 = Moodle(300, 150, "ИСИ")
        """
        self.max_online = None
        self.init_max_online(max_online)
        self.online = None
        self.init_online(online)

        if not isinstance(institute, str):
            raise TypeError("Название института должно быть типа str")
        self.institute = institute

    def init_max_online(self, max_online: int):
        """
        Метод проверяет условия значений атрибута "Максмально поддерживаемое количество пользователей на сайте"
        """
        if not isinstance(max_online, int):
            raise TypeError("Максмально поддерживаемое количество пользователей на сайте должно быть типа int")
        if not max_online > 0:
            raise ValueError("Максмально поддерживаемое количество пользователей на сайте должно быть положительное")
        self.max_online = max_online

    def init_online(self, online: int):
        """
        Метод проверяет условия возможных значений атрибута "Текущее количество пользователей на сайте"
        """
        if not isinstance(online, int):
            raise TypeError("Текущее количество пользователей на сайте должно быть типа int")
        if online < 0:
            raise ValueError("Текущее количество пользователей на сайте не должно быть отрицательным числом")
        self.online = online

    def destroy(self) -> bool:
        """
        Метод, который проверяет упал ли сайт

        :return : Упал ли сайт

        Примеры:
        >>> moodle1 = Moodle(300, 400, "ИЭ")
        >>> moodle1.destroy()
        """
        ...

    def control_users(self, users: int):
        """
        Метод увеличивает/уменьшает количество пользователей, которым доступен сайт

        :param users: Количество добавленных/удаленных пользователей, которым доступен сайт

        :return : Текущее количество пользователей, которым доступен сайт

        Примеры:
        >>> moodle1 = Moodle(300, 400, "ИЭ")
        >>> moodle1.control_users(100)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
