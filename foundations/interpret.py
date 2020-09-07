def interpret(value, commands, args):
  ops = zip(commands, args)
  for op in ops:
    if op[0]=="+": value+=op[1]
    elif op[0]=="-": value-=op[1]
    elif op[0]=="*": value*=op[1]
    else:
      return -1
  return value



if __name__=="__main__":
    print("interpret(1, ['+'], [1]) should be 2 and is ", interpret(1, ['+'], [1]))
    print("interpret(4, ['-'], [2]) should be 2 and is ", interpret(4, ['-'], [2]))
    print("interpret(1, ['+', '*'], [1, 3]) should be 6 and is ", interpret(1, ['+', '*'], [1, 3]))