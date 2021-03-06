from bots.botsconfig import *
from records003040 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'FT',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGF', MIN: 1, MAX: 1},
    {ID: 'K3', MIN: 1, MAX: 99999},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
