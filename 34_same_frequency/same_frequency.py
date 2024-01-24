def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    counts = {}
    counts2 = {}

    for char in str(num1):
        counts[char] = str(num1).count(char)

    for char in str(num2):
        counts2[char] = str(num2).count(char)

    return counts == counts2