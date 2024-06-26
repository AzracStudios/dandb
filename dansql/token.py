from __future__ import annotations

from dansql.position import Position

KEYWORDS = [
  "select",
  "write",
  "create",
  "fetchall",
  "fetchone",
  "update",
  "delete",
  "to",
  "from",
  "database",
  "table",
  "commit"
]

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
  ARITH_OP = "ARITH_OP"

  LBRACE = "LBRACE"
  RBRACE = "RBRACE"
  
  LSQBRAC = "LSQBRAC"
  RSQBRAC = "RSQBRAC"

  SEMICOL= "SEMICOL"
  COL = "COL"
  
  WHITESPACE = "WHITESPACE"
  NEWLINE = "NEWLINE"
  EOF = "EOF" 