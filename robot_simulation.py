import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = (
    'ROBOT',
    'PLEASE',
    'MOVE',
    'BLOCKS',
    'AHEAD',
    'AND',
    'THEN',
    'TURN',
    'NUMBER',
)

# Define lexer rules
t_ROBOT = r'Robot'
t_PLEASE = r'please'
t_MOVE = r'move'
t_BLOCKS = r'blocks'
t_AHEAD = r'ahead'
t_AND = r'and'
t_THEN = r'then'
t_TURN = r'turn'
t_ignore = ' \t\n'

# Define lexer error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define parser rules
def p_program(p):
    '''program : ROBOT PLEASE instruction_list'''
    print("Program executed successfully!")

def p_instruction_list(p):
    '''instruction_list : instruction
                        | instruction_list AND instruction
                        | instruction_list THEN instruction'''
    pass

def p_instruction(p):
    '''instruction : MOVE NUMBER BLOCKS AHEAD
                   | TURN NUMBER'''
    if p[1] == 'MOVE':
        print(f"Move {p[2]} blocks ahead")
    elif p[1] == 'TURN':
        print(f"Turn {p[2]} degrees")

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")

# Build lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the program with example instructions
instructions = [
    "Robot please move 2 blocks ahead",
    "Robot please move 3 blocks ahead and then turn 90 degrees",
    "Robot please move 2 blocks ahead and then turn 270 degrees",
]

for instruction in instructions:
    lexer.input(instruction)
    parser.parse(lexer=lexer)
    print()
