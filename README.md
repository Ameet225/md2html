# md2html 📝➡🌐

![Python version](https://img.shields.io/badge/python-3.8+-blue)

**md2html** is a simple Python CLI tool that converts Markdown files to HTML.

## Features
- 📍 Converts '.md' files to '.html' files
- 📍 Command-Line interface using 'argparse'
- 📍 Modular and easy to extend

## Installation

First clone the repo and navigate to it:

```bash
git clone https://github.com/Ameet225/md2html.git
cd md2html
```

Install it in editable mode:
```
pip install -e .
```

## Usage
```
md2html -i input.md -o output.html
```
📌 Replace input.md and output.html with your actual filenames.<br>
📌 Make sure input.md is in your current folder, or provide the full/relative path.<br>
📁 The output file will be saved wherever you specify in `-o`.<br>
If no folder is mentioned, it will be created in the current directory.