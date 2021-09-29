
# Python3 implementation of the above approach
 
# Function that returns true if s1
# and s2 are anagrams of each other
def isAnagram(s1, s2) :
    s1 = list(s1);
    s2 = list(s2);
    s1 = s1.sort();
    s2 = s2.sort();
     
    if (s1 == s2) :
        return 1;
         
    return 0;
 
# Function to return the minimum swaps required
def CountSteps(s1, s2, size) :
    s1 = list(s1);
    s2 = list(s2);
     
    i = 0;
    j = 0;
    result = 0;
     
    # Iterate over the first string and convert
    # every element equal to the second string
    while (i < size) :
        j = i;
         
        # Find index element of first string which
        # is equal to the ith element of second string
        while (s1[j] != s2[i]) :
            j += 1;
             
        # Swap adjacent elements in first string so
        # that element at ith position becomes equal
        while (i < j) :
             
            # Swap elements using temporary variable
            temp = s1[j];
            s1[j] = s1[j - 1];
            s1[j - 1] = temp;
            j -= 1;
            result += 1;
             
        i += 1;
         
    return result;


