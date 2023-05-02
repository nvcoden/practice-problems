# Leetcode problem - https://leetcode.com/problems/distance-between-bus-stops/description/


distance =[7,10,1,12,11,14,5,0]
start = 7
destination = 2

#################### SOLUTION ####################

f = b = start   # 0<=start<n
print(f)
n = len(distance)
distF = distB = 0
# stops = list(i for i in range(n))
# print(stops)
# print(f, b)
for i in range(n):
    distF += distance[f]
    distB += distance[(b-1)]
    print(distF, distB)
    f=(f+1)%n
    b=(b-1)%n
    print("f+1=", f)
    print("(b-1)%n=", b)
    # print("stop[f] = ", stops[f])
    # print("stop[b] = ", stops[b])
    if f == destination:
        print("in here")
        # if distF < distB:
        print(distF, type(distF))
        print("FINAL ANSWER", distF)
        exit()
    if b == destination:
        print("I am not in here???")
        # if distB < distF:
        print("FINAL ANSWER",distB)
        exit()

############## REFLECTIONS ##############


# Now that i think about best solution posted in the 'solutions' section, i reealize that my solution is the most stupid way to answer this question. 😔
# Hopefully I can think smarter like this in as I do more.
# The best answer - https://leetcode.com/problems/distance-between-bus-stops/solutions/377532/python-3-easy-to-understand/