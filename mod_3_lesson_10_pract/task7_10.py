def is_palindrome(strk):
    if not isinstance(strk,str):
        raise TypeError("not str")
    return strk == strk[::-1]
print(is_palindrome(""))
