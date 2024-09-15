a = input()
char_list = list(a)

def is_palindrome(list_):
    end = len(char_list)
    for i in range(0, end // 2):
        if char_list[i] != char_list[end-i-1]:
            return False
    return True
    
if is_palindrome(char_list):
    print("Yes")
else: print("No")