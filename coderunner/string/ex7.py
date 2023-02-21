#parcialmente correto
s = input()   


if s == s[::-1]:
    print("ON")
else:
   
    for i in range(len(s)):
        new_s = s[:i] + chr(ord('a') + (ord(s[i]) - ord('a') + 1) % 26) + s[i+1:]
        if new_s == new_s[::-1]:
            print("ON")
            break
    else:
        print("OFF")
