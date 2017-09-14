global comparisons

def select(ls,i):
    global comparisons
    '''select the ith order stat of the list ls'''
    subs = [ls[i:i+5] for i in range(0,len(ls),5)] #partition in n/5 groups of length at most 5 each

    median_ls = [sorted(sub)[len(sub)/2] for sub in subs]



    if len(median_ls) <= 5:
        pivot = sorted(median_ls)[len(median_ls)/2]
    else:
        pivot = select(median_ls, len(median_ls)/2) #pivot is the median of medians

    #pivot = median(median_ls)
    #partition array around the pivot
    low = [j for j in ls if j < pivot]
    high = [j for j in ls if j > pivot]

    k = len(low)
    if i < k:
        comparisons+=1
        return  select(low,i)
    elif i > k:
        comparisons += 1
        return select(high,i-k-1)
    else:
        comparisons += 1
        return pivot

#x=[4,2,5,4,6,11,13]

#print(select(x,3))



comparisons=0
print(comparisons)