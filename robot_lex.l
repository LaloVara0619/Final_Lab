%{
#include "y.tab.h"
%}

%%

"Robot"         { return ROBOT; }
"please"        { return PLEASE; }
"move"          { return MOVE; }
"blocks"        { return BLOCKS; }
"ahead"         { return AHEAD; }
"and"           { return AND; }
"then"          { return THEN; }
"turn"          { return TURN; }
[0-9]+          { yylval.num = atoi(yytext); return NUMBER; }
[ \t\n]         { /* Ignore whitespace */ }
.               { /* Ignore other characters */ }

%%

int yywrap() {
    return 1;
}
