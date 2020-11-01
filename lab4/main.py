from scanner import Scanner
from pif import PIF
from symbol_table import SymbolTable

pif = PIF()
symbol_table = SymbolTable()
scanner = Scanner(pif, symbol_table, "p1.txt")
scanner.scan()
