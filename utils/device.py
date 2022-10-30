"""
Authors: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import enum


class Device(enum.Enum):
    cpu = 'cpu'
    cuda = 'cuda'
    mps = 'mps'
