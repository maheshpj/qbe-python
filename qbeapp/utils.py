# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 2014

@author: Mahesh.Jadhav

"""


SELECT = "SELECT"
FROM = "FROM"
WHERE = "WHERE"
GROUP_BY = "GROUP BY"
ORDER_BY = "ORDER BY"
SPACE = " "
COMMA = ", "
DOT = "."
INNER = "INNER"
LEFT_OUTER = "LEFT OUTER"
JOIN = "JOIN"
ON = "ON"
AND = "AND"
OR = "OR"

AGGREGATION = (('', ''), ('avg', 'avg'), ('count', 'count'), ('max', 'max'), 
               ('min', 'min'), ('sum', 'sum'), ('upper', 'upper'), ('lower', 'lower'), 
               ('len', 'len'), ('group by', 'group by'))
OPERATORS = (('=', '='), ('>=', '>='), ('<=', '<='), ('>', '>'), ('<', '<'), 
             ('<>', '<>'), ('like', 'like'), ('between', 'between'), ('in', 'in'))

def quote_str(str):
    return "'" + str + "'"

def parenthesized_str(str):
    return "(" + str + ")"