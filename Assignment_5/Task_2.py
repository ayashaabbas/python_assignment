# Task 2: Demonstrate List Slicing 
#Create a list of numbers from 1 to 10.

orignl_lst=[1,2,3,4,5,6,7,8,9,10]
print("The original list: ", orignl_lst)
# Extract the first five elements from the list.
ext_lst= orignl_lst[:5]
print("Extracted First five elements: ", ext_lst)
#3.   Reverses these extracted elements.
def reverse_lst(a):
    j= len(a)-1
    for i in range(len(a)//2):
        a[i] , a[j-i]= a[j-i], a[i]
    return a

rever_lst=reverse_lst(ext_lst)
#4.   Prints both the extracted list and the reversed list

print("Reversed Extracted list: ", rever_lst)