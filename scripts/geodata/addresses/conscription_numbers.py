import os
import random
import sys

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.realpath(os.path.join(this_dir, os.pardir, os.pardir)))

from geodata.addresses.config import address_config
from geodata.addresses.numbering import NumberedComponent
from geodata.encoding import safe_decode


class ConscriptionNumber(NumberedComponent):
    @classmethod
    def phrase(cls, number, language, country=None):
        if number is None:
            return number

        key = 'conscription_numbers.alphanumeric'
        dictionaries = ['house_numbers']
        default = safe_decode(number)

        return cls.numeric_phrase(key, safe_decode(number), language,
                                  dictionaries=dictionaries, country=country)
