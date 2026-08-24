# Recursive Descent Parser for Arithmetic Expressions

A simple **Recursive Descent Parser** implemented in Python to validate arithmetic expressions using a context-free grammar.

## 📌 About the Project

This project demonstrates how a recursive descent parser can be used to determine whether an arithmetic expression follows a predefined grammar.

The parser supports:

* Identifiers (`a`, `x`, `num`)
* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Parentheses (`(` `)`)

### Grammar Used

```text
E  → T E'
E' → + T E' | - T E' | ε

T  → F T'
T' → * F T' | / F T' | ε

F  → ( E ) | id
```

Where:

* `E` = Expression
* `T` = Term
* `F` = Factor
* `id` = Identifier
* `ε` = Empty string

## ⚙️ How It Works

The parser follows the grammar recursively:

```text
Expression
    ↓
    E
    ↓
    T → F → Identifier / (Expression)
    ↓
    E'
    ↓
  + / -
```

The parser processes the input from left to right and keeps track of the current character using a position pointer.

If the complete input matches the grammar, the expression is **accepted**. Otherwise, it is **rejected**.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Run the Python program

```bash
python parser.py
```

### 3. Enter an expression

Example:

```text
Enter an arithmetic expression: a+b*c
String Accepted
Valid Arithmetic Expression
```

## 🧪 Examples

### Valid Expressions

```text
a+b
a+b*c
(a+b)*c
a/(b-c)
x+y*(z-2)
```

### Invalid Expressions

```text
a+
+a
a*/b
(a+b
a+b)
a**b
```

## 🧩 Main Components

| Method           | Purpose                                                |
| ---------------- | ------------------------------------------------------ |
| `current_char()` | Returns the current character                          |
| `match()`        | Checks and consumes an expected character              |
| `E()`            | Parses an expression                                   |
| `E_prime()`      | Handles `+` and `-` operations                         |
| `T()`            | Parses a term                                          |
| `T_prime()`      | Handles `*` and `/` operations                         |
| `F()`            | Parses identifiers and parenthesized expressions       |
| `parse()`        | Starts the parsing process and checks the entire input |

## 🛠️ Technologies Used

* **Python 3**
* **Context-Free Grammar (CFG)**
* **Recursive Descent Parsing**
* **Compiler Design Concepts**

## 🎯 Learning Objectives

This project helps understand:

* Recursive descent parsing
* Context-free grammars
* Grammar production rules
* Expression parsing
* Top-down parsing techniques
* Basic compiler design concepts

## 📁 Project Structure

```text
Recursive-Descent-Parser/
│
├── LAB4.py
└── README.md
```

## 🚀 Future Improvements

Possible improvements include:

* Support for numeric constants such as `10`, `25`
* Support for decimal numbers
* Unary operators such as `-a`
* Better error messages showing the position of the error
* Support for exponentiation (`^`)
* Building a parse tree

## 📄 License

This project is created for **educational and learning purposes**.
