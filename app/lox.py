import sys


class Lox:
    def __init__(self) -> None:
        self.has_error: bool = False

    def process_file(self, fname):
        with open(fname) as file:
            content = file.read()
            self.process(content)
            if self.has_error:
                sys.exit(65)

    def process(self, content):
        from app.scanner.scanner import Scanner

        if content:
            scanner = Scanner(content, self)
            for token in scanner.tokenize():
                print(token)
        else:
            print(
                "EOF  null"
            )  # Placeholder, remove this line when implementing the scanner

    def error(self, line, message):
        self.report(line, "", message)

    def report(self, line, loc, message):
        print(f"[line {line}] Error{loc}: {message}", file=sys.stderr)
        self.has_error = True
