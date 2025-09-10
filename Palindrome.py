def Palindrome(array):
    left, right = 0, len(array)-1
    while left < right:
        if array[left] != array[right]:
            return False
        left +=1
        right -=1
    return True 

print(Palindrome(array=["racecar"]))


