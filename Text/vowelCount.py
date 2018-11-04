"""
=======================================================================


"""

""" 
This script helps you to count the number of vowels in a given string (even a file)
"""

def vowelsCount(entryStr):
    """
    This scans the string and outputs the vowel count stats from the given string

    :param entryStr:
    :return:
    """
    vowel = ['a','e','i','o','u']
    aCount, eCount, iCount, oCount, uCount = 0, 0, 0, 0, 0

    for char in entryStr:
        if char in vowel:
            aCount += 1 if char == 'a' else 0
            eCount += 1 if char == 'e' else 0
            iCount += 1 if char == 'i' else 0
            oCount += 1 if char == 'o' else 0
            uCount += 1 if char == 'u' else 0
    return (f'======================================\n'
            f'Below are the vowel finding stats: \nVowel a - {aCount}\nVowel e - {eCount}\nVowel i - {iCount}\nVowel o - {oCount}\nVowel u - {uCount}\n'
            f'======================================')

def validateText():
    """
    Asks the user for input and only return a valid string
    that contains both alpha and alphanumeric characters.
    """
    while True:
        validateStr = input('Enter a valid sentence that contains alphabets and alphanumeric characters: ')
        try:
            entryStr = validateStr.lower()
            if entryStr.isdecimal() or entryStr.isdigit() or entryStr.isnumeric() or entryStr.isspace():
                print('Please enter a valid sentence')
            else:
                return entryStr
        except:
            print('Invalid characters, please enter valid characters')


def mainScript():
    text = validateText()
    print(vowelsCount(text))


if __name__ == "__main__":
    mainScript()
