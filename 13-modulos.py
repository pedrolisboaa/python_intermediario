"""
Módulos padrões do Python
Os módulos são arquivos .py (que contem código python) e servem para 
expandir as funcionalidades padrão da linguagem
"""

#import sys
#print(sys.platform)

from sys import platform as sistema_operacional
print(sistema_operacional)

import random
print(random.randint(0, 50))
