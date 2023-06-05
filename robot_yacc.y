%{
#include <stdio.h>

int yylex();
void yyerror(const char* s);

// Define tokens
#define ROBOT 257
#define PLEASE 258
#define MOVE 259
#define BLOCKS 260
#define AHEAD 261
#define AND 262
#define THEN 263
#define TURN 264
#define NUMBER 265

%}

%token ROBOT PLEASE MOVE BLOCKS AHEAD AND THEN TURN NUMBER

%%

program : ROBOT PLEASE instruction_list
        {
            printf("Program executed successfully!\n");
        }
        ;

instruction_list : instruction
                 | instruction_list AND instruction
                 | instruction_list THEN instruction
                 ;

instruction : MOVE NUMBER BLOCKS AHEAD
            {
                printf("Move %d blocks ahead\n", $2);
            }
            | TURN NUMBER
            {
                printf("Turn %d degrees\n", $2);
            }
            ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "%s\n", s);
}

int main() {
    yyparse();
    return 0;
}
