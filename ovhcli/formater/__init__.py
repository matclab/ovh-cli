# -*- encoding: utf-8 -*-

import os
import pkgutil
import imp

# HACK: ensure yaml/json lib in cache is the global one:
import yaml
import json

FORMATERDIR = os.path.split(os.path.realpath(__file__))[0]

formaters = dict([(name, importer) for importer, name, _ in pkgutil.iter_modules([FORMATERDIR])])

def get_formater(name):
	return formaters[name].find_module(name).load_module(name)
