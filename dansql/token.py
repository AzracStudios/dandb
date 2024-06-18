from __future__ import annotations

from dansql.position import Position


class Token:

  def __init__(
      self,
      tok_type: str,
      start_pos: Position,
      value: str | int | float | None = None,
      end_pos: Position | None = None,
  ) -> None:
    self.type = tok_type
    self.value = value
    self.start_pos = start_pos
    self.end_pos = self.start_pos.copy().advance() if not end_pos else end_pos
    return None

  def __repr__(self) -> str:
    return f"[{self.type}{f':{self.value}' if self.value else ''}]"


class TokenType:
  KWRD = "KWRD"
  IDENT = "IDENT"

  STRING = "STRING"
  INT = "INT"
  FLOAT = "FLOAT"

  COMPARE_OP = "COMPARE_OPERATOR"
  ASSIGN_OP = "ASSIGN_OPERATOR"

  LBRACE = "LBRACE"
  RBRACE = "RBRACE"
  
  LBRACK = "LBRAC"
  RBRACK = "RBRACK"

  SEMICOL= "SEMICOL"
  COL = "COL"
  
  NEWLINE = "NEWLINE"
  EOF = "EOF"
  