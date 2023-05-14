# question - https://leetcode.com/problems/merge-sorted-array



######### solution 1 #######
# j = 0
# for i in range(m, m+n):
#     nums1[i]= nums2[j]
#     j+=1
# nums1.sort()

######## solution 2 ########
i = m-1
j = n-1
k = m+n -1
while j>=0:
    if i>=0 and nums1[i]>nums2[j]:
        nums1[k] = nums1[i]
        i-=1
    else:
        nums1[k] = nums2[j]
        j-=1
    k-=1


print(nums1)


#PS: For some reason, on the run, the sol1 seems to be too slow and memory consuming, if leetcode's metrics are to be believed.
# is it because we are using the 'sort()' method? ......probably🤔
