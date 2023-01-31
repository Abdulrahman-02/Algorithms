def isValideSubsequence(array,sequence):
    num = 0
    seq = 0
    while num < len(array) and seq < len(sequence):
        if(sequence[seq] == array[num]):
            seq += 1
        num += 1
    return seq == len(sequence)
