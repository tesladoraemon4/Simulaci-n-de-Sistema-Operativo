# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlHardware.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
def contains(item,lis):
	for ite in lis:
		if ite == item:
			return True
		return False


def getIndex(item,lista):
	cont = 0
	for x in lista:
		if x == item:
			return cont
		cont += 1
