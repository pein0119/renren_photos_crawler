# -*- coding: utf-8 -*-

import ConfigParser
import io

config = ConfigParser.RawConfigParser()
config.read('config.ini')

# print config.get('cookie', 'cookie')
rid_list = config.options('person')
print rid_list
