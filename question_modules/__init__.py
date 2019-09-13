# -*- coding: utf-8 -*-
# import os
# from importlib.machinery import SourceFileLoader

# lut = {}

# dirname = os.path.dirname(__file__)

# for filename in os.listdir(dirname):
#     if filename == '__init__.py' or filename[-3:] != '.py':
#         continue

#     module = SourceFileLoader("question_modules." + filename[:-3], os.path.join(dirname, filename)).load_module()

#     lut[module.NAME] = module
