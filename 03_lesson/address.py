class Address:

    def __init__(self, postal_code, city, street, house, apartment):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def where_to_go(self):
        return f"{self.postal_code}, г.{self.city}, ул.{self.street}, д.{self.house} - кв.{self.apartment}"

    def where_sent_from(self):
        return f"{self.postal_code}, г.{self.city}, ул.{self.street}, д.{self.house} - кв.{self.apartment}"
