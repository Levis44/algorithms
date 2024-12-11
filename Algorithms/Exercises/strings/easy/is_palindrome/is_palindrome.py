def isPalindrome(string):
    if(len(string) == 0):
        return True

    pointer = len(string) - 1
    for letter in string:
        if letter == string[pointer]:
            pointer -= 1
        else:
            return False

    return True
        
