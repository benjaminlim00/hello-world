def is_anagram(s1,s2):
    a = list(s1)
    b = list(s2)
    print(sorted(a))
    print(sorted(b))
    return sorted(a) == sorted(b)

print(is_anagram('abc', 'acb'))