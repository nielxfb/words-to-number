# words-to-number

A Python utility to convert a list of words representing a number into its numerical value.

## Description

This project provides a function `wordsToNumber` that takes a list of words representing a number and converts it into its numerical value. It handles various multipliers such as "hundred", "thousand", "million", etc.

## Usage

### Function: `wordsToNumber`

#### Arguments

- `words` (list of str): A list of words representing the number.

#### Returns

- `int`: The numerical value of the words.

#### Example

```python
from main import wordsToNumber

print(wordsToNumber(["two", "million", "three", "hundred", "forty", "five", "thousand", "six", "hundred", "seventy", "eight"]))
# Output: 2345678

print(wordsToNumber(["three", "thousand", "two", "hundred", "ten"]))
# Output: 3210
```

## Running the Script
You can run the script directly to convert a number in words entered by the user:
```python
python main.py
```

## Installation
Clone the repository:
```bash
git clone https://github.com/nielxfb/words-to-number.git
cd words-to-number
```

## Testing
Unit tests are provided to ensure the function works correctly. To run the tests, use the following command:
```bash
python -m unittest discover
```
