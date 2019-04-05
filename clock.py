#!/usr/bin/env python
from time import sleep
from sys import argv
import os

class BoundedCounter:

    def __init__(self, upper_limit):
        '''
        @value: value that keeps track of the counter.
        @upper_limit: limit which counter value cannot exceed.
        '''
        self.upper_limit = upper_limit
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if (not value > self.upper_limit) and (not value < 0):
            self._value = value
        else:
            print("invalid value")
            exit(0)

    def next(self):
        '''
        Advance the object counter by one. Reset to 0 if counter
        reaches upper_limit.
        '''
        if self.value < self.upper_limit:
            self.value += 1
        else:
            self.value = 0
            
    def __str__(self):
        '''
        Return 0-padded string of two digits.
        '''
        if self.value < 10:
            return '0' + str(self.value)
        return str(self.value)

class Clock:

    def __init__(self, hours, minutes, seconds):
        '''
        hours: upper_limit = 23
        minutes: upper_limit = 59
        seconds: upper_limit = 59
        '''
        self.hours = BoundedCounter(23)
        self.minutes = BoundedCounter(59)
        self.seconds = BoundedCounter(59)

        self.hours.value = hours
        self.minutes.value = minutes
        self.seconds.value = seconds

    def tick(self):
        '''
        Run each object's counter once previous counter falls back to zero.
        '''
        self.seconds.next()
        if self.seconds.value == 0:
            self.minutes.next()
            if self.minutes.value == 0:
                self.hours.next()

    def __str__(self):
        '''
        Returns a representation of a clock in the format
        hh:mm:ss
        '''
        return f'{self.hours}:{self.minutes}:{self.seconds}'

def main(args):
    '''
    Run a clock object with command line arguments for hours, minutes and seconds.
    '''

    if len(args) < 3:
        print("Usage: provide hours, minutes, seconds, separated by a space.")
        print("('hh' 'mm' 'ss')")
        exit(0)

    hours = int(args[0])
    minutes = int(args[1])
    seconds = int(args[2])
    ticky = Clock(hours, minutes, seconds)

    # Run clock loop until interrupt is sent.
    try:
        while True:
            os.system('clear')
            print(ticky)
            sleep(1)
            ticky.tick()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main(argv[1:])
