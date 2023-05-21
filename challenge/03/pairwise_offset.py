def pairwise_offset(sequence, fillvalue = "*", offset = 0):
    fillers = fillvalue * offset
    
    if type(sequence) is list:
        fillers = list(fillers)

    seq1 = fillers + sequence
    seq2 = sequence + fillers

    result = [(b, a) for (a, b) in zip(seq1, seq2)]
    return result
