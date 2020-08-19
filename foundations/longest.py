#!/usr/bin/env python3
# coding: utf-8
########################################
# authors                              #
# marcalph https://github.com/marcalph #
########################################
"""
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"
"""

s = "abppplee"
d = {"able", "ale", "apple", "bale", "kangaroo"}
d = sorted(d, key=len, reverse=True)

def find_longest_substr(d=d, s=s):
    for candidate in d:
        if len(candidate) > len(s):
            continue
        else:
            for i in range(len(candidate)):
                if candidate[i] in s[i:]:
                    if i == len(candidate)-1:
                        return candidate
                    i = s.index(candidate[i])
                else:
                    break


res = find_longest_substr()
print(res)