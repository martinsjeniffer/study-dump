"""
    Given two strings ransomNote and magazine, 
        return true if ransomNote can be constructed by using the letters from magazine and 
        false otherwise.

    Each letter in magazine can only be used once in ransomNote.

"""

"""
    SOLUTIONS OBSERVATIONS

    magazine   "aaab" -> { a: 3, b: 1 }
    ransomnote "aabb" -> { a: 2, b: 2 }
    second str must be sub-set of first str, and not overload.

    using a dictionary for the solution:
    complexity
        time -> O(n + m)
        space -> O(m)

"""

import collections

# def canConstruct(ransomNote, magazine):
#     magazine_dict = collections.defaultdict(int)

#     for char in magazine:
#         magazine_dict[char] = 1 if char not in magazine_dict else magazine_dict[char] + 1
#         print(magazine_dict)

#     print('-----')

#     for r_char in ransomNote:
#         if r_char not in magazine_dict or magazine_dict[r_char] == 0:
#             return False
#         else:
#             magazine_dict[r_char] -= 1
#         print(magazine_dict)


#     return True


def canConstruct(ransomNote, magazine):
    magazine_counter = collections.Counter(magazine)

    for r_char in ransomNote:
        if r_char not in magazine_counter or magazine_counter[r_char] == 0:
            return False
        else:
            magazine_counter[r_char] -= 1
        print(magazine_counter)

    return True


if __name__== "__main__":
    ransomNote = "aabbb"
    magazine = "aaabb"
    canConstruct(ransomNote, magazine)

