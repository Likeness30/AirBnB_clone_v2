#!/usr/bin/python3
import re
def parser(argument, [delimeter]):
    result = re.split(delimeter, argument)
    return result
