from address import Address

from mailing import Mailing

address1 = Address("660021", "Красноярск", "Мира", "128", "16")
address2 = Address("630005", "Новосибирск", "Ломоносова", "4", "1")

to_address = address1.where_to_go()
from_address = address2.where_sent_from()

mailing = Mailing(to_address, from_address, 300, 112112)
result = mailing.get_result()
print(result)
