
# Recursive Descent Parser

class Parser:
    def __init__(self, exp):
        self.exp = exp.replace(" ", "")
        self.i = 0

    # E -> T E'
    def E(self):
        if not self.T():
            return False

        while self.i < len(self.exp) and self.exp[self.i] in "+-":
            self.i += 1
            if not self.T():
                return False

        return True

    # T -> F T'
    def T(self):
        if not self.F():
            return False

        while self.i < len(self.exp) and self.exp[self.i] in "*/":
            self.i += 1
            if not self.F():
                return False

        return True

    # F -> (E) | id
    def F(self):
        if self.i >= len(self.exp):
            return False

        if self.exp[self.i] == '(':
            self.i += 1

            if not self.E():
                return False

            if self.i < len(self.exp) and self.exp[self.i] == ')':
                self.i += 1
                return True

            return False

        if self.exp[self.i].isalpha():
            self.i += 1
            return True

        return False

    # Check the complete expression
    def parse(self):
        return self.E() and self.i == len(self.exp)


# Main program
exp = input("Enter an expression: ")

p = Parser(exp)

if p.parse():
    print("String Accepted")
else:
    print("String Rejected")
