import os
import random
import sys

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.realpath(os.path.join(this_dir, os.pardir, os.pardir)))

from geodata.addresses.config import address_config
from geodata.addresses.numbering import NumberedComponent
from geodata.encoding import safe_decode


class HouseNumber(NumberedComponent):
    @classmethod
    def phrase(cls, number, language, country=None):
        if number is not None:
            prob_key = 'house_numbers.alphanumeric_phrase_probability'
            key = 'house_numbers.alphanumeric'
            dictionaries = ['house_numbers', 'number']
            default = safe_decode(number)
        else:
            prob_key = 'house_numbers.no_number_probability'
            key = 'house_numbers.no_number'
            dictionaries = ['no_number']
            default = None

        phrase_prob = address_config.get_property(prob_key, language, country=country, default=0.0)
        if random.random() < phrase_prob:
            return cls.numeric_phrase(key, safe_decode(number), language,
                                      dictionaries=dictionaries, country=country)
        return default
