def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(s) == 0 or len(p) == 0:
        return 0
    # initialise
    s = {}
    indexs_array = []
    substring_map = {}
    i = 0

    # get the substring map
    for char in p:
        if char in substring_map.keys():
            substring_map[char] += 1
        else:
            substring_map[i] = 1

    temp_substring_map = substring_map

    # check substrings occurence
    while i != len(s) - 1:
        if s[i] in substring_map.keys():
            j = i
            while s[j] in temp_substring_map.keys() and temp_substring_map[s[j]] > 0:
                j += 1
                temp_substring_map[s[j]] -= 1
            if j == len(p):
                index_array.append(i)
        i += 1
    print(index_array)
