from src.core import Parser, Either, Error, Success


class Char(Parser[str]):
    def __init__(self, character: str) -> None:
        self.character = character

    def parse(self, input: str) -> Either[Success[str]]:
        if not len(input):
            return Error("Unexpected end of input")
        if input[0] != self.character:
            return Error(f"Expected '{self.character}', got '{input[0]}'")
        return Success(self.character, input[1:])
