from Token import TokenType
from Lexing import Lexing

def main() -> None :
    sorce_code = 'for(int i===0; i<10; i+=1) { }'
    go_to_lexer = Lexing(sorce_code)
    find_token = go_to_lexer.NextToken()

    while find_token.tokenType != TokenType.EOF :
        print(find_token)
        find_token = go_to_lexer.NextToken()

if __name__ == '__main__' :
    main()