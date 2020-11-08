import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def get_Bullvalue(value):
    if (value == "True"):
     for number in range(2,101,2):
            print(number)
    else:
        if (value == "False"):
         for number in range(1,100,2):
                print(number)
