def palindrome(word):
  
    def check_rec(word,i,j):
        if i>=len(word):
            return True
        elif word[i] != word[j]:
            return False
        else:
            return check_rec(word,i+1,j-1)
    return check_rec(word,0,-1)