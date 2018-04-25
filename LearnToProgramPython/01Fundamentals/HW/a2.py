def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    lendna = len(dna)
    return lendna


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num = 0
    for char in dna:
        if char == nucleotide:
            num = num + 1
    return(num)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return(dna1.find(dna2)>0)

def is_valid_sequence(dna):
    ''' (str) -> bool
    
    Return True if DNA sqeuence dan is valid, i.e. it contains no characters other than 'A', 'T', 'C' and 'G'
    
    >>> is_valid_sequence('ACTGATTG')
    True
    >>> is_valid_sequence('AACCTtaG')
    False
    >>> is_valid_sequence('ACTGUF')
    False
    '''
    res = None
    for char in dna:
        res = char in 'ATCG'
        if not res:
            break
    return res
    
def insert_sequence(dna1, dna2, loc):
    ''' (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second sequence dna2 into the first dna1 at given index (loc).
        
    >>> insert_sequence('ATGC', 'AACG', 2)
    'ATAACGGC'
    '''
        
    return dna1[0:loc]+dna2+dna1[loc:]

def get_complement(neo):
    ''' (str) -> str
        
    Return the cucleotide neo's complement.
        
    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    '''
    if (neo == 'A'):
        return 'T'
    elif (neo == 'T'):
        return 'A'
    elif (neo == 'C'):
        return 'G'
    elif (neo == 'G'):
        return 'C' 
        
def get_complementary_sequence(dna): 
    ''' (str) -> str 
    
    Return DNA sequence that is complementary to the given DNA sequence dna
    
    >>> get_complementary_sequence('ATCGG')
    'TAGCC'
    '''
    com = ''
    for char in dna:
        com = com + get_complement(char)
    return com    