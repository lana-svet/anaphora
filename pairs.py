#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import itertools

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, description='Make pairs "group id - pronoun id".')
parser.add_argument('infile1', nargs='?', type = argparse.FileType('r'), help = 'file with a list of groups')
parser.add_argument('infile2', nargs='?', type = argparse.FileType('r'), help = 'file with a list of pronouns')
args = parser.parse_args()


groups = []
pron = []


def take_num(fd, mas):
    for line in fd:
        line = line.strip().split('\t')
        mas.append(line[0])  

take_num(args.infile1, groups)
take_num(args.infile2, pron)         


result = itertools.product(groups, pron)
for i in result:
    sys.stdout.write('{0}__{1}'.format(i[0], i[1]) + '\n')

