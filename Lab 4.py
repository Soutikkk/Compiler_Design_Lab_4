
# Recursive Descent Parser for Arithmetic Expressions

class Parser:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")
        self.position = 0

    # Return the current character
    def current_char(self):
        if self.position < len(self.expression):
            return self.expression[self.position]
        return None

    # Match and consume the expected character
    def match(self, char):
        if self.current_char() == char:
            self.position += 1
            return True
        return False

    # E -> T E'
    def E(self):
        return self.T() and self.E_prime()

    # E' -> + T E' | - T E' | epsilon
    def E_prime(self):
        while self.current_char() in ('+', '-'):
            self.position += 1

            if not self.T():
                return False

        return True

    # T -> F T'
    def T(self):
        return self.F() and self.T_prime()

    # T' -> * F T' | / F T' | epsilon
    def T_prime(self):
        while self.current_char() in ('*', '/'):
            self.position += 1

            if not self.F():
                return False

        return True

    # F -> ( E ) | id
    def F(self):
        # Check for parenthesized expression
        if self.match('('):
            if not self.E():
                return False
            return self.match(')')

        # Check for an identifier
        char = self.current_char()

        if char is not None and char.isalpha():
            self.position += 1
            return True

        return False

    # Start parsing and verify the entire expression
    def parse(self):
        return self.E() and self.position == len(self.expression)


# Main program
expression = input("Enter an arithmetic expression: ")

parser = Parser(expression)

if parser.parse():
    print("String Accepted")
    print("Valid Arithmetic Expression")
else:
    print("String Rejected")
    print("Invalid Arithmetic Expression")
