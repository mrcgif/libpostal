import os
import random
import sys

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.realpath(os.path.join(this_dir, os.pardir, os.pardir)))

from geodata.addresses.config import address_config
from geodata.addresses.numbering import NumericPhrase 
from geodata.encoding import safe_decode


class MetroStationPhrase(NumericPhrase):
    key = 'metro_stations.alphanumeric'
    dictionaries = ['qualifiers']


class MetroStation(object):
    @classmethod
    def phrase(cls, station, language, country=None):
        if station is None:
            return None
        phrase_prob = address_config.get_property('metro_stations.alphanumeric_phrase_probability', language, country=country, default=0.0)
        if random.random() < phrase_prob:
            return MetroStationPhrase.phrase(station, language, country=country)

        return None
