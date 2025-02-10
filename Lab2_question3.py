#Write a Python function that can reverse a string

def reverse_string(s):
    reversed_str=""
    for i in s:
        reversed_str=i+reversed_str
    return reversed_str

print(reverse_string("Cloud Computing"))



