from __future__ import annotations
from typing import Callable

from dansql.position import Position
from dansql.token import Token, TokenType, KEYWORDS
from dansql.error import Error, LexerError


class Lexer:

    def __init__(self, source_path: str, source: str) -> None:
        self.source: str = source
        self.current_char: str | None = None
        self.position: Position = Position(-1, -1, 1, self.source)
        self.advance()

        return None

    def advance(self, adv_count: int = 1) -> None:
        self.position.advance(char=self.current_char, count=adv_count)

        if (i := self.position.idx) < len(self.source):
            self.current_char = self.source[i]
            return None

        self.current_char = None
        return None

    def peek_chars_by(self, peek_by: int) -> str:
        if self.position.idx + peek_by < len(self.source):
            return self.source[self.position.idx : self.position.idx + peek_by]
        return ""

    def revert(self) -> None:
        self.position.revert()

        if (i := self.position.idx) > 0:
            self.current_char = self.source[i]
            return None

        self.current_char = None
        return None

    def generate_next_token(self) -> Token | Error:
        if self.current_char in "\n":
            return Token(TokenType.NEWLINE, self.position.copy(), value="\n")

        if self.current_char in "\t ":
            return Token(TokenType.WHITESPACE, self.position.copy(), value=" ")


        if self.current_char == ">":
            return Token(TokenType.RANGLE, self.position.copy(), value=">")

        if self.current_char == "/":
            return Token(TokenType.FWDSLSH, self.position.copy(), value="/")

        if self.current_char == "=":
            return Token(TokenType.EQL, self.position.copy(), value="=")

        if self.current_char in "\"'":
            return self.lex_string()

        if self.current_char in "01234567890.":
            return self.lex_number()

        return self.lex_word()

    class XMLLexer(Lexer):

        def __init__(self, source_path: str, source: str) -> None:
            super().__init__(source_path, source, generate_next_token)

    def lex_string(self) -> Token | Error:
        start_pos: Position = self.position.copy()
        quote: str | None = self.current_char

        self.advance()

        string = ""
        while True:
            if self.current_char is None or self.current_char == quote:
                break
            string += self.current_char
            self.advance()

        if self.current_char != quote:
            return LexerError(
                "Unterminated String Literal",
                self.source,
                start_pos,
                self.position.copy().advance(),
            )

        return Token(
            TokenType.STRING, start_pos, value=string, end_pos=self.position.copy()
        )

    def lex_kwrd_or_ident(self) -> Token:
        word: str = ""
        start_pos: Position = self.position.copy()

        while self.current_char != " ":
            word += self.current_char
            self.advance()

        self.revert()
        return Token(
            TokenType.KWRD if word in KEYWORDS else TokenType.IDENT,
            start_pos,
            value=word,
            end_pos=self.position.copy().advance(),
        )

    def lex_number(self) -> Token | Error:
        start_pos: Position = self.position.copy()
        num_str: str = ""
        dot_count: int = 0

        while self.current_char and self.current_char in "0123456789.":
            if self.current_char == ".":
                dot_count += 1

            num_str += self.current_char
            self.advance()

        self.revert()
        if dot_count > 1:
            return Token(
                TokenType.WORD,
                start_pos,
                value=num_str,
                end_pos=self.position.copy(),
            )

        return Token(
            TokenType.NUMBER,
            start_pos,
            value=(float(num_str) if dot_count else int(num_str)),
            end_pos=self.position.copy(),
        )

    def tokenize(self) -> list[Token] | None:
        tokens = []

        while self.current_char:
            token_or_error: Token | Error = self.generate_next_token(self)

            if isinstance(token_or_error, Error):
                print(token_or_error.generate_error_text())
                return None

            tokens.append(token_or_error)
            self.advance()

        tokens.append(Token(TokenType.EOF, self.position.copy()))

        # pop spaces and new lines from head
        while True:
            if tokens[0].type == TokenType.WHITESPACE:
                tokens.pop(0)
                continue
            break

        return tokens
