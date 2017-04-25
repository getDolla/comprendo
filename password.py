def validate_password(s):
    upper = [ u for u in s if ord(u) in range(65, 91) ]
    lower = [ l for l in s if ord(l) in range(97, 123) ]
    nums = [ n for n in s if ord(n) in range(48, 58) ]
    return (len(upper) > 0) and (len(lower) > 0) and (len(nums) > 0)

'''
print validate_password("abcDEFZz")#false
print validate_password("Aa0")#true
print validate_password("zZ9")#true
print validate_password("ABC")#false
print validate_password("abc")#false
print validate_password("123")#false
'''

def password_strength(s): #1-10 range
    upper = [ u for u in s if ord(u) in range(65, 91) ]
    lower = [ l for l in s if ord(l) in range(97, 123) ]
    nums = [ n for n in s if ord(n) in range(48, 58) ]
    nonalpha = [ na for na in s if ord(na) in range(33, 48) ]

    length = len(upper) + len(lower) + len(nums) + len(nonalpha)
    score = length * 4 + len(upper) + len(lower)
    score = score + len(nums) if len(nums) == length else score + len(nums) * 2
    score = score + len(nonalpha) if len(nonalpha) == length else score + len(nonalpha) * 3
    
    score = int(round(score/10.6))
    score = 10 if score > 10 else score
    return score

'''
print password_strength("abcdefg")#3
print password_strength("1234567")#3
print password_strength("a1b2d34v56g7H")#7
'''
