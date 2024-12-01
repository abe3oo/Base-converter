
---

# Base Converter

## Overview

The **Base Converter** is a Python program that converts numbers between different bases, supporting bases from **2 to 16**. Whether you're working with binary, hexadecimal, or anything in between, this tool simplifies the process with an interactive command-line interface.

---

## Features

- **Flexible Base Conversion**: Convert numbers between bases from **2 to 16**.
- **Supports Hexadecimal**: Includes proper handling for hexadecimal digits (A-F).
- **Interactive and User-Friendly**: The program provides clear prompts and colored output for better readability.
- **Error Handling**: Ensures incorrect inputs are caught and reported.

---

## How It Works

1. **Input a Number**: Enter the number you want to convert.
2. **Specify the Source Base**: Provide the base of the input number (e.g., 2, 10, 16).
3. **Specify the Target Base**: Enter the base to which you want the number converted.
4. **View the Result**: The program calculates and displays the converted number.

---

## Prerequisites

To run this program, ensure the following:
- Python 3.x is installed on your system.
- Basic knowledge of number systems (binary, decimal, hexadecimal, etc.) is helpful.

---

## Usage

1. Clone or download this repository.
2. Run the program using Python:
   ```bash
   python base_converter.py
   ```
3. Follow the prompts:
   - Input your number.
   - Enter the source and target bases.
   - View the result.

### Example

```plaintext
_-_-_Base converter_-_-_ (to close the app please type exit)
enter your number: 1011
From base: 2
to base: 16
Result ==> B
```

---

## Code Explanation

### Key Functions

1. **`convert_list_to_string(lst1)`**  
   Converts a list of digits into a single string for easy output.

2. **`number_to_10(a, number)`**  
   Converts a number from any base (2–16) to base 10.

3. **`ten_to_enything(a, number)`**  
   Converts a base-10 number to any target base (2–16).

### Main Loop

- Continuously prompts the user for input until they type `exit`.
- Performs base conversions and handles errors gracefully, such as invalid inputs or incorrect bases.

### Error Handling

- Ensures bases are entered as integers.
- Validates the number's compatibility with the source base.

---

## Color-Coded Outputs

The program uses ANSI escape codes to enhance readability:
- **Bold Text**: For key information.
- **Colors**: Different colors for messages like errors or instructions.

---

## Notes

- Supports bases **2 through 16**. For bases greater than 10, the program uses standard hexadecimal notation (A-F).
- To stop the program, type `exit` when prompted for a number.

---

## License

This project is released under the MIT License. Feel free to use and modify it as needed.

---