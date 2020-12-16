"""First part of Sample Google Interview Question
Find the total number of nodes from each value to the root node (1) in this tree
       1
     /   \\
    2      3
   / \\    / \\
  4   5   6   7
 /\\
8  9                       """

#before we right code let's think about how the algorithim works
# let's just go from the node 9 first
number = int(input("enter a positve integer: "))
nodes=0
while (2**(nodes+1) <= number):
    nodes+=1
print(nodes)

#now that we can calculate the number of nodes from a value, we can find the total nodes by using another while statement
total_nodes =0
while (number>0):
  nodes=0
  while (2**(nodes+1) <= number):
    nodes+=1
  number-=1
  total_nodes += nodes
print(total_nodes)