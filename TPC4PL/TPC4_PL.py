#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      dario
#
# Created:     07/03/2024
# Copyright:   (c) dario 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Exemplo do manual
# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
# Exemplo do manual
# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'Select',
   'From',
   'Where',
   'Numero',
   'MayorQue',
   'Delimitador',
   'Atributos',
   'Signos',
)

# Regular expression rules for simple tokens

# A regular expression rule with some action code
def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A regular expression rule with some action code
#(?i) mayus y minus
#\b para que pille la palabra sola
def t_Select(t):
    r'(?i)\bSelect\b'
    return t

# A regular expression rule with some action code
def t_Form(t):
    r'(?i)\bForm\b'
    return t

# A regular expression rule with some action code
def t_Where(t):
    r'(?i)\bWhere\b'
    return t

# A regular expression rule with some action code
def t_Signos(t):
    r',|;'
    return t

# A regular expression rule with some action code
def t_Atributos(t):
    r'[A-Z][a-z]+'
    return t

# A regular expression rule with some action code
def t_MayorQue(t):
    r'>='
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
Select id,nome,salario From empregados Where salario >= 820
'''

# Give the lexer some input
lexer.input(data)

for tok in lexer:
    print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)