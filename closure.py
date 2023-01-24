class Date:
    length_day = length_month = 2
    length_year = 4

    def __init__(self, day, month, year):
        self.__day = str(day)
        self.__month = str(month)
        self.__year = str(year)

    @property
    def date(self):
        return f"{self.format_data(self.__day)()}/{self.format_data(self.__month)()}/" \
               f"{self.format_data(self.__year)(Date.length_year)}"

    @property
    def usa_date(self):
        return f"{self.format_data(self.__month)()}-{self.format_data(self.__day)()}-" \
               f"{self.format_data(self.__year)(Date.length_year)}"

    @staticmethod
    def format_data(data: str):
        def inner(length=Date.length_day):
            nonlocal data
            while len(data) < length:
                data = "0" + data
            return data

        return inner


d1 = Date(5, 10, 2001)
print(d1.date)
d2 = Date(15, 3, 999)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)
