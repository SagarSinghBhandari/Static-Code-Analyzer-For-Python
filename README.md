# 🧠 Static Code Analyzer

A Python-based Static Code Analyzer that performs **Lexical**, **Syntax**, and **Semantic** analysis of source code and computes **code metrics** including Halstead complexity using Radon. The project also features an interactive user interface built with Streamlit to visualize code properties and structural components like AST, identifiers, and reserved keywords.

## 🚀 Features

- ✅ **Lexical Analysis**  
  Tokenizes source code into meaningful tokens (keywords, identifiers, literals, operators).

- ✅ **Syntax Analysis**  
  Parses the code to build an abstract syntax tree (AST) using Python's built-in `ast` module.

- ✅ **Semantic Analysis**  
  Identifies semantic issues like use of undefined variables.

- ✅ **Code Metrics**  
  Computes:
  - Maintainability Index
  - Cyclomatic Complexity
  - Halstead Metrics (Length, Volume, Effort, Time, Estimated Bugs)

- ✅ **Visualization Tabs**
  - Metrics Summary
  - Reserved Keywords
  - Identifiers
  - Abstract Syntax Tree (AST)

## 🛠 Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: Python (`ast`, `radon`, `re`, `collections`)
- **Visualization**: Plotly Express, Wordcloud
- **Testing**: Manual Test Cases

## 📂 Project Structure

```bash
.
├── lexical.py            # Lexical Analyzer
├── parser_module.py      # AST-based Syntax Analyzer
├── semantic.py           # Semantic Checker
├── utility.py            # Halstead & Radon Metrics
├── main.py               # Streamlit UI
├── parser.py             # Dependency list
├── parse.py              # Dependency list
└── README.md             # Project documentation
