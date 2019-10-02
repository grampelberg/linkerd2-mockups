#!/usr/bin/env python3

import argparse

import yaml

from prettytable import PrettyTable, PLAIN_COLUMNS

def output(header, rows):
    tbl = PrettyTable()
    tbl.border = False
    tbl.field_names = [x.upper() for x in header]

    for row in rows:
        try:
            tbl.add_row(row)
        except:
            print('error-{}'.format(row))
            break

    return tbl

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data', metavar='PATH', help='path to the data files.')

    args = parser.parse_args()

    data = yaml.load(open(args.data, 'r'))

    print(output(data.get('header'), data.get('rows')))
