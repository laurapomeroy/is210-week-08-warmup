#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Systolic blood pressure in common language terms"""


PRESSURE = raw_input('What is your blood pressure reading? ')
PRESSURE = int(PRESSURE)

if PRESSURE <= 89:
    BP_STATUS = 'Low'
elif PRESSURE <= 119:
    BP_STATUS = 'Ideal'
elif PRESSURE <= 139:
    BP_STATUS = 'Warning'
elif PRESSURE <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

STATUS = 'Your status is currently: {}'.format(BP_STATUS)
print STATUS
