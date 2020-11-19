def compare(l1,l2):
    num=sum(a==b for a,b in zip(l1,l2))
    return num==len(l1)==len(l2)

def diff(l1,l2):

    print([x for x in l1 if x not in set(l2)])

l1=[0,0,0]
l2=[0,0,0]
print("Enter elements of the 1st list :\n")
l1.append(int(input([0])))
l1.append(int(input([1])))
l1.append(int(input([2])))
print("Enter elements of the 2nd lits :\n")
l2.append(int(input([0])))
l2.append(int(input([1])))
l2.append((input([2])))

res=compare(l1,l2)
if res==False:
    print("\nDifference between the two lists after comparing : ")
    diff(l1,l2)
else:
    print("\nThere is no difference between the lists.")
