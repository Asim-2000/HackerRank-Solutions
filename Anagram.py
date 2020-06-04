#Building a dictionary ot map to store the frequency count of characters in the substring 
def buildMap(s):
    map = {}
    for ch in s:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] +=1
             
    return map       
     
 
def anagram(s):
    #return -1 if the number is odd
    if len(s)%2 == 1:
        return -1

    #Taking the middle index     
    mid = len(s)//2
    #first substring from index 0 to mid_index-1
    s1 = s[:mid]
    #second substring from mid_index to last
    s2 = s[mid:]
    #building map for s1
    map_1 = buildMap(s1)
    #building map for s2
    map_2 = buildMap(s2)
    
    #counting the different letters
    diff_count = 0
    for key in map_2.keys():
        if key not in map_1:
            diff_count += map_2[key]
        else:
            diff_count += max(0, map_2[key]-map_1[key])
     
    return diff_count