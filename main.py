import json
from utils.functions import process
from utils.statistics import get_stat_dict
from time import sleep

pict_list = ['MY FIRST SKRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
  sleep(.4)
  print(i)


with open('parallelepipeds.json', 'r') as f:
  parallelepipeds = json.load(f)


characteristics_json = {}
for fig, atr_dict in parallelepipeds.items():
    a = float(atr_dict['a'])
    b = float(atr_dict['b'])
    c = float(atr_dict['c'])
    characteristics_json[fig] = process(a, b, c)

statistics = get_stat_dict(characteristics_json)

#-----load files----
with open('outputs/characteristics.json', 'w') as json_file:
    json.dump(characteristics_json, json_file, indent=4)

with open('outputs/statistics.json', 'w') as f:
    json.dump(statistics, f, indent=4)


num_keys = len(parallelepipeds)
print(f'Total number of figures: {num_keys}.')

end_= """
Created FILES:
    --'outputs/characteristics.json'
    --'outputs/statistics.json'

###___END SCRIPT___###
"""
print(end_)