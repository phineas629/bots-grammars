from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'SL',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGN', MIN: 1, MAX: 1},
    {ID: 'SLI', MIN: 1, MAX: 3},
    {ID: 'DB', MIN: 1, MAX: 10},
    {ID: 'DEF', MIN: 0, MAX: 1},
    {ID: 'DTP', MIN: 0, MAX: 5},
    {ID: 'ENT', MIN: 1, MAX: 6, LEVEL: [
        {ID: 'NTE', MIN: 0, MAX: 5},
        {ID: 'ENR', MIN: 0, MAX: 1},
        {ID: 'FNA', MIN: 0, MAX: 1},
        {ID: 'AMT', MIN: 0, MAX: 15},
        {ID: 'MEA', MIN: 0, MAX: 2},
        {ID: 'SCT', MIN: 0, MAX: 8},
        {ID: 'DTP', MIN: 0, MAX: 1},
        {ID: 'Y6', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 2, LEVEL: [
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 10},
            {ID: 'PER', MIN: 0, MAX: 2},
        ]},
        {ID: 'PLI', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'N1', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
        ]},
        {ID: 'IN1', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'IN2', MIN: 0, MAX: 5},
            {ID: 'DMG', MIN: 0, MAX: 1},
            {ID: 'DMA', MIN: 0, MAX: 1},
            {ID: 'LX', MIN: 0, MAX: 4, LEVEL: [
                {ID: 'N1', MIN: 0, MAX: 1},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 1},
                {ID: 'DTP', MIN: 0, MAX: 1},
                {ID: 'PER', MIN: 0, MAX: 2},
            ]},
        ]},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]