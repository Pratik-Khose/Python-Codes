# This is the 09FindingFrequencyOfElements.py file

def finding(a):
    mp = dict()

    for i in range(len(a)):
        if a[i] in mp.keys():
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1

    # for x in mp:
    #     print(x, ':', mp[x])

    return mp


ab = [ 1,9,7,8,6,4,3,2,5,1,6,8,4,9,1,3,1,5]

numbers = finding(ab)
print(numbers)