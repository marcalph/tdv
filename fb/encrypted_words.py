import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def helper(stringlist):
  if len(stringlist)==0:
    return []
  
  if len(stringlist)==1:
    print(stringlist[0])
    return stringlist
  
  mid = (len(stringlist)-1)//2
  print(stringlist[mid])
  return [stringlist[mid]]+helper(stringlist[:mid])+helper(stringlist[mid+1:])
  
  