# Code Formatter

## Overview

Welcome to my Code Formatter tool! This Python program is designed to take a text file containing unformatted code, with no indentations and possibly all code on a single line, and transform it into properly formatted code with appropriate indentations and spaces. Whether you're dealing with messy code or need to enhance readability, this tool's got you covered.

## Features

- **Automatic Formatting**: The formatter automatically analyzes the structure of the code and applies the necessary indentations and spaces to ensure readability and maintainability.

- **Customizable Settings**: While the formatter comes with default settings for code formatting, you can customize indentation width, spacing, and other formatting options to match your preferred coding style.

- **Support for Various Languages**: The formatter supports multiple programming languages, allowing you to format code written in Python, JavaScript, Java, C++, and more. Just copy and paste your code into a text file and you are good to go.

## Implementation Details

This tool leverages the power of a stack data structure in Python to analyze the code structure and apply appropriate formatting. By utilizing a stack, the program efficiently handles nested code blocks and ensures accurate indentation.

## Usage

1. **Input File**: Prepare a text file containing the unformatted code that you wish to format.

2. **Run the Formatter**: Execute the `formatter.py` script. This should run the program and make edits to the input text file. You can view the edited text file in the input.txt file

   Example:

   python3  formatter.py
