from django.db import models
from django.db.models.deletion import CASCADE


class Country(models.Model):
    """
    Модель для представления информации о странах.

    ### Attrs:
    - name (str): Название страны.

    """
    name = models.CharField("Название страны", max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Модель для представления информации о населенных пунктах (городах).

    ### Attrs:
    - name (str): Название населенного пункта (города).
    - region (Country): Страна, к которой относится населенный пункт, связанная с объектом модели Country.

    """
    name = models.CharField("Название", max_length=100, blank=False, null=False)
    region = models.ForeignKey(Country, on_delete=CASCADE, related_name="cities", verbose_name="Страна")

    class Meta:
        verbose_name = "Населённый пункт"
        verbose_name_plural = "Населённые пункты"

    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    """
    Модель для представления информации об адресах.

    ### Attrs:
        - city (City): Населенный пункт (город), связанный с объектом модели City.
        - street (str): Название улицы.
        - building_number (str): Номер дома.
        - building (str, необязательный): Номер корпуса (если есть).
        - postcode (str, необязательный): Почтовый индекс (если есть).

    ### Method:
        - __str__(): Метод, возвращающий строковое представление адреса в виде "город, улица, дом" с возможным указанием корпуса и почтового индекса.

    """
    city = models.ForeignKey(City, on_delete=CASCADE, related_name="addresses", verbose_name="Населённый пункт")
    street = models.CharField("Улица", max_length=200, blank=False, null=False)
    building_number = models.CharField("Дом", max_length=10, blank=False, null=False)
    building = models.CharField("Корпус", max_length=10, blank=True, null=True)
    postcode = models.CharField("Почтовый индекс", max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        address = f'{self.city}, ул. {self.street}, дом {self.building_number}'
        if self.building is not None:
            address += f', корп. {self.building}'
        if self.postcode is not None:
            address += (f' ({self.postcode})')
        return address
