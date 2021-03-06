#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 10},
    {ID: 'ALI', MIN: 0, MAX: 5},
    {ID: 'IMD', MIN: 0, MAX: 10},
    {ID: 'FTX', MIN: 0, MAX: 5},
    {ID: 'PGI', MIN: 0, MAX: 10},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'TRU', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'RCS', MIN: 0, MAX: 10, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 5},
    ]},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 10},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'CCI', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'CAV', MIN: 0, MAX: 10},
        {ID: 'MEA', MIN: 0, MAX: 10},
    ]},
    {ID: 'EFI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CED', MIN: 0, MAX: 99},
        {ID: 'COM', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 999999, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 10},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'MEA', MIN: 0, MAX: 10},
        {ID: 'HAN', MIN: 0, MAX: 5},
        {ID: 'DOC', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'PGI', MIN: 0, MAX: 10},
        {ID: 'IMD', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'TRU', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
        {ID: 'RCS', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 5},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
            {ID: 'STS', MIN: 0, MAX: 5},
        ]},
        {ID: 'PRI', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'CUX', MIN: 0, MAX: 1},
            {ID: 'RNG', MIN: 0, MAX: 1},
        ]},
        {ID: 'CCI', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CAV', MIN: 0, MAX: 10},
            {ID: 'MEA', MIN: 0, MAX: 10},
        ]},
        {ID: 'ALI', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PCD', MIN: 0, MAX: 5},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 5},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'CTA', MIN: 0, MAX: 5, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 10, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 5},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'HAN', MIN: 0, MAX: 5},
            {ID: 'PCI', MIN: 0, MAX: 5},
            {ID: 'COD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9},
                {ID: 'QTY', MIN: 0, MAX: 9},
                {ID: 'PCD', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'HYN', MIN: 0, MAX: 999999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 10},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 5},
            ]},
            {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CAV', MIN: 0, MAX: 10},
                {ID: 'MEA', MIN: 0, MAX: 10},
            ]},
            {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'PIA', MIN: 0, MAX: 10},
                {ID: 'QTY', MIN: 0, MAX: 5},
                {ID: 'CCI', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'CAV', MIN: 0, MAX: 99},
                    {ID: 'MEA', MIN: 0, MAX: 10},
                ]},
            ]},
        ]},
        {ID: 'EFI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'CED', MIN: 0, MAX: 99},
            {ID: 'COM', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
