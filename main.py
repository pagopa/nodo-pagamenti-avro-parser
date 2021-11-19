import json
import os
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='Parse an .avro file', prog='main.py')
parser.add_argument('file', metavar='FILE', type=str, help='.avro file path to parse')
parser.add_argument('--iuv', metavar='IUV', type=str, nargs='?', help='filter by iuv')
parser.add_argument('--dominio', metavar='ID DOMINIO', type=str, nargs='?', help='filter by ID Dominio')
parser.add_argument('--pretty', action='store_true', help='prettyprint the json output')
args = parser.parse_args()

file = args.file
iuv = args.iuv
idDominio = args.dominio
pretty = args.pretty

os.system(f'java -jar avro-tools-1.11.0.jar tojson {file} > tmp.json')

with open('tmp.json') as f:
    lines = f.readlines()
    for line in lines:
        elem = json.loads(line)
        data = json.loads(elem['Body']['bytes'])
        if (iuv is None or data['iuv'] == iuv) and (idDominio is None or data['idDominio'] == idDominio):
            if pretty:
                pprint(data)
            else:
                print(data)
os.system('rm tmp.json')
