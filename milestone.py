def s(dna):
    Dict = {}
    countA = countC = countG = countT = 0
    for i in dna:
        if i == 'A': #if the element is A 
            countA = countA + 1 #increase count of A
            Dict['A'] = countA #store the count of A into Dict
        elif i == 'C':  #if the element is C
            countC = countC + 1 #increase count of C
            Dict['C'] = countC #store the count of C into Dict 
        elif i == 'G':  #if the element is G
            countG = countG + 1 #increase count of G
            Dict['G'] = countG #store the count of G into Dict
        elif i == 'T':  #if the element is T
            countT = countT + 1 #increase count of T
            Dict['T'] = countT #store the count of T into Dict
    return Dict
    
    
