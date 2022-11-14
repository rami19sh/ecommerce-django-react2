def valid_parenthesese(str1:str):
    if len(str1)%2==1 or len(str1)==0:
        return False
    if str1.count("{")==str1.count("}") and str1.count("(")==str1.count(")") and str1.count("[")==str1.count("]"):
        return True
    return False



# st1=""
# print(valid_parenthesese(st1))


#41
def first_missing_positive(lst1:list):
    cnt=0
    min1=min(lst1)
    max1=max(lst1)
    res=max1-min1+1
    return res-len(lst1)


lst1=[1,2,0]
print(first_missing_positive(lst1))