s = "A man, a plan, a canal: Panama"
def isPalindrome(s: str) -> bool:
        clean=''.join(ch.lower() for ch in s if ch.isalnum())
        
        print(clean==clean[::-1])
isPalindrome(s)