def isValidSubsequence(array, sequence):
    sequence_pointer = 0
    for num in array:
        if (sequence_pointer == (len(sequence))):
            return True
            
        if (num == sequence[sequence_pointer]):
            sequence_pointer += 1

    if (sequence_pointer == (len(sequence))):
        return True
    else:
        return False
        
