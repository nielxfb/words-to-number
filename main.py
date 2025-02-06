numberWordsDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}

multipliers = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
    "billion": 1000000000,
    "trillion": 1000000000000
}

def wordsToNumber(words):
    """
    Convert a list of words representing a number into its numerical value.

    Args:
        words (list of str): A list of words representing the number.

    Returns:
        int: The numerical value of the words.

    Example:
        >>> wordsToNumber(["two", "million", "three", "hundred", "forty", "five", "thousand", "six", "hundred", "seventy", "eight"])
        2345678
        >>> wordsToNumber(["three", "thousand", "two", "hundred", "ten"])
        3210
    """
    number = 0
    current = 0
    for word in words:
        if word in numberWordsDict:
            current += numberWordsDict[word]
            print (current)
        elif word in multipliers:
            if multipliers[word] >= 1000:
                current *= multipliers[word]
                number += current
                current = 0
            else:
                current *= multipliers[word]

    return number + current

if __name__ == "__main__":
    words = input("Enter a number in words: ")
    words = words.lower().split()
    print(f"Your number is: {wordsToNumber(words)}")
