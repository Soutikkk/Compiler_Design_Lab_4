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

    # Match the expected character
    def match(self, char):
        if self.current_char() == char:
            self.position += 1
            return True
        return False

    # E -> T E'
    def E(self):
        if not self.T():
            return False

        return self.E_prime()

    # E' -> + T E' | - T E' | epsilon
    def E_prime(self):
        while self.current_char() in ['+', '-']:
            self.position += 1

            if not self.T():
                return False

        return True

    # T -> F T'
    def T(self):
        if not self.F():
            return False

        return self.T_prime()

    # T' -> * F T' | / F T' | epsilon
    def T_prime(self):
        while self.current_char() in ['*', '/']:
            self.position += 1

            if not self.F():
                return False

        return True

    # F -> ( E ) | id
    def F(self):
        # Case 1: ( E )
        if self.match('('):
            if not self.E():
                return False

            return self.match(')')

        # Case 2: identifier
        if self.current_char() is not None and self.current_char().isalpha():
            self.position += 1
            return True

        return False

    # Start parsing
    def parse(self):
        if self.E() and self.position == len(self.expression):
            return True

        return False


# Main program
expression = input("Enter an arithmetic expression: ")

parser = Parser(expression)

if parser.parse():
    print("String Accepted")
    print("Valid Arithmetic Expression")
else:
    print("String Rejected")
    print("Invalid Arithmetic Expression")