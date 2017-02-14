def palindrome(word):
  
    def check_rec(word,i,j):
        if i>=len(word):
            return True
        elif word[i] != word[j]:
            return False
        else:
            return check_rec(word,i+1,j-1)
    return check_rec(word,0,-1)

    # OR

    def ispalindrome(word):
        return word == word[::-1]

    # OR

    def ispalindrome(word):
        if len(word) < 2: return True
        if word[0] != word[-1]: return False
        return ispalindrome(word[1:-1])

