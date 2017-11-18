# -*- coding: utf-8 -*-
#
# parameters.py
#
# This file is part of PrintNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# Fibonacci is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PrintNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrintNumbers.  If not, see <http://www.gnu.org/licenses/>.

#
# Class to process and store program parameters.
#

CONST_VERSION = 'V1.0'
CONST_VERSION_STRING = '+ + PrintNumbers ' + CONST_VERSION + ' (Software Development in Science 2017) + +'
CONST_DEF_NUMBER_OF_TERMS = 10
CONST_MAX_NUMBER_OF_TERMS = 20
CONST_FUNC_CODE_FIBONACCI = 0
CONST_FUNC_CODE_FACTORIAL = 1

class Parameters(object):

    def __init__(self, cmdLineArgs):
        self.numberOfTerms = CONST_DEF_NUMBER_OF_TERMS
        self.functionIndex = CONST_FUNC_CODE_FIBONACCI
        self.__setParameters(cmdLineArgs)

    def __setParameters(self, cmdLineArgs):
        self.numberOfTerms = (int(cmdLineArgs['<numberOfTerms>']))
        if cmdLineArgs['--fibonacci']:
            self.functionIndex = CONST_FUNC_CODE_FIBONACCI
        elif cmdLineArgs['--factorial']:
            self.functionIndex = CONST_FUNC_CODE_FACTORIAL

    @property
    def numberOfTerms(self):
        return(self.__numberOfTerms)

    @numberOfTerms.setter
    def numberOfTerms(self, n):
        if n <= 0 or n > CONST_MAX_NUMBER_OF_TERMS:
            print("Error: The number of terms needs to be in the following range: 0 < n <=", CONST_MAX_NUMBER_OF_TERMS)
            print("       The default value will be used.")
            print("")
            n = CONST_DEF_NUMBER_OF_TERMS
        self.__numberOfTerms = n

    @property
    def functionIndex(self):
        return(self.__functionIndex)

    @functionIndex.setter
    def functionIndex(self, value):
        self.__functionIndex = value

    def PrintParameters(self):
        print('')
        print(CONST_VERSION_STRING)
        print('')
        print('Following Parameters are in use:')
        print('--------------------------------')
        print('Function Code  : ', self.functionIndex)
        print('<numberOfTerms>: ' + str(self.numberOfTerms))
        print('')
