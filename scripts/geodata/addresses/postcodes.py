import os
import sys

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.realpath(os.path.join(this_dir, os.pardir, os.pardir)))

from geodata.addresses.numbering import NumberedComponent
from geodata.encoding import safe_decode


class PostCode(NumberedComponent):
    @classmethod
    def phrase(cls, postcode, language, country=None):
        if postcode is None:
            return None
        return cls.numeric_phrase('postcodes.alphanumeric', postcode, language,
                                  dictionaries=['postcodes'], country=country)
