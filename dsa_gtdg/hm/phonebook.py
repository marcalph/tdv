# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
#  your code here. Read input from STDIN. Print output to STDOUT
pb = {}
n = int(input())
for _ in range(n):
    ins = input()
    pb[ins.split()[0]]=ins.split()[1]

for _ in range(n):
    q = input()
    answer = f"{q}={str(pb.get(q, None))}" if pb.get(q, None) else "Not found"
    print(answer)