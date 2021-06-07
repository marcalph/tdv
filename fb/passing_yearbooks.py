""" There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back. 
"""

#
def findSignatureCounts(arr):
  # Write your code here
  res = [1]*len(arr)
  count = 0
  for i in range(len(arr)):
    k=i
    while arr[k]!=i+1:
      res[i]+=1
      k=arr[k]-1
  return res

"""
Consider that each student is a member of a single yearbook passing cycle.
For example, for input [3, 2, 4, 1], there are two yearbook passing cycles: {3, 4, 1} and {2}.
Therefore, the number of signatures for each member of a passing cycle is equal to the size of the cycle.
In the example, students {3, 4, 1} each get 3 signatures (1 for his/her self, and 1 for the other 2 students), and student {2} gets 1 signature, his/her own signature.
The yearbook passing cycle for any group of students can be determined starting with a particular student, and traversing through the input until the next student to receive the book is the first student of the cycle. (I thought of the cycle like a circular linked list.)

An O(N) time algo can achieved if it considers a student only one time. That is, as the root of a passing cycle, or as a member of a passing cycle that is visited before the traversal returns to the root member.

Algo

Follow the passing cycle of the first student until it returns back to the first student.
Along the way, mark each student (the root and traversed nodes) as visited.
Save the count of the members in the cycle with the root node.
For each node traversed (nodes other than the root node), save a reference to the root node.
Repeat the above for any students that have yet to be visited.
For each root node, return the size of its cycle.
For each traversed node, return the size of the cycle of its root node.
"""
def findSignatureCounts(arr):
    visited_students = set()
    signatures = [0] * len(arr)
    root_indexes = [-1] * len(arr)

    for i in range(len(arr)):
        # avoid traversing a node more than once
        student = arr[i]
        if student in visited_students:
            continue
        visited_students.add(student)

        # consider the current student to be the root of a cycle, and traverse back to itself
        signatures[i] = 1
        next_i = student - 1
        while next_i != i:
            signatures[i] += 1
            root_indexes[next_i] = i
            visited_students.add(arr[next_i])
            next_i = arr[next_i] - 1

    # return the signature counts of the root nodes, and the referenced root node counts of traversed nodes
    for i in range(len(arr)):
        if root_indexes[i] != -1:
            signatures[i] = signatures[root_indexes[i]]
    return signatures  