import os
import sys

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.realpath(os.path.join(this_dir, os.pardir, os.pardir)))

from geodata.configs.utils import RESOURCES_DIR

UNICODE_DATA_DIR = os.path.join(RESOURCES_DIR, 'unicode')

CLDR_DIR = os.path.join(UNICODE_DATA_DIR, 'cldr')
