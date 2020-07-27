"""
Smallest Window containing substr_starting (hard) #
Given a string and a pattern, find the smallest substr_starting in the given string which has all the characters of the given pattern.
Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substr_starting having all characters of the pattern is "abdec"
Example 2:
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substr_starting having all characters of the pattern is "abc".
Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substr_starting in the given string has all characters of the pattern.
"""

# O(N+M) time | O(M) space

import math

def solve(pattern,arr):
    windowStart,matched,substr_start=0,0,0
    charFrequency={}
    minlength=math.inf

    for ch in pattern:
        if ch not in charFrequency:
            charFrequency[ch]=0
        charFrequency[ch] +=1

    for windowEnd in range(len(arr)):
        rightChar= arr[windowEnd]

        if rightChar in charFrequency:
            charFrequency[rightChar]-=1
            if charFrequency[rightChar] >=0:
                matched +=1

        while matched == len(pattern):
            if minlength >=windowEnd-windowStart+1:
                minlength =windowEnd-windowStart+1
                substr_start=windowStart

            leftChar=arr[windowStart]
            windowStart +=1
            if leftChar in charFrequency:
                if charFrequency[leftChar] ==0:
                    matched -=1
                charFrequency[leftChar] +=1

    if minlength>len(arr):
        return ""
    
    return arr[substr_start:substr_start+minlength]
