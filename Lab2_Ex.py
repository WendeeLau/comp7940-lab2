import json
import requests
site="https://api.npoint.io/2b57052af2060e84dc86"
# Write the functions convert_number and replace_number here
# Follow the logic below.
# Trying to load JSON into text
r=requests.get(site)
print(r.json())
text=r.json()['users']
print(text)
#print(text[0])
#Debug
#define the function convert_number
def convert_number(t):
    number_list=[]
    for i in t:
        if i.isdigit():
            number_list.append(int(i))
    return number_list
#define the function replace_number
def replace_number(number_list,being_replace,to_replace):
    new_number_list=[]
    for i in number_list:
        if i==being_replace:
            i=to_replace
        new_number_list.append(i)
    return new_number_list
for i in text:
    print("parse"+str(i))
# call the function convert_number
# convert all elements (except the first one) into number and return it as a list
y=convert_number(text[0])
print("y")
print(y)
# call the function replace_number
# replace all number 1 by the number 10 in the function
z=replace_number(y,1,10)
print("z")
print(z)
sum=0
for i in z:
    sum=sum+i
    print("sum="+str(sum)+";i="+str(i))
print("Total="+str(sum))