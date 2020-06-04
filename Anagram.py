def buildMap(s):
    map = {}
    for ch in s:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] +=1
             
    return map       
     
 
def anagram(s):
    if len(s)%2 == 1:
        return -1
         
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
     
    map_1 = buildMap(s1)
    map_2 = buildMap(s2)
     
    diff_count = 0
    for key in map_2.keys():
        if key not in map_1:
            diff_cnt += map_2[key]
        else:
            diff_cnt += max(0, map_2[key]-map_1[key])
     
    return diff_count