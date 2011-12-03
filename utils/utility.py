#!/usr/bin/python

import codecs
import json

import itertools
import operator

import re
import sys

def from_file(name, encoding = 'utf-8'):
    with open(name, 'rb') as handle:
        iterable = codecs.getreader(encoding)(handle)
        for item in iterable:
            yield item.rstrip('\r\n')

def read(fn, iterable):
    for line_number, line in enumerate(iterable):
        try:
            yield fn(line)
        except Exception as e:
            exc_type = sys.exc_info()[0].__name__
            exc_trace = sys.exc_info()[2]
            raise RuntimeError, 'Exception on item #{0}:\n\t{1}\n{2}: {3}'.format(
                1 + line_number, line,
                exc_type, e
            ), exc_trace

def write(stream, iterable):
    for item in iterable:
        stream.write(item)
        stream.write('\n')

def select(key, iterable):
    for item in iterable:
        yield item[key]

def mean(iterable):
    value_accumulator = 0.0
    count_accumulator = 0

    for item in iterable:
        value_accumulator += item
        count_accumulator += 1

    return value_accumulator / float(count_accumulator)
