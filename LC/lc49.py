# print(''.join(sorted(strs[0])))
class Solution:
    def groupAnagrams(self, strs):
        hash_map={}
        for word in strs:
            if(''.join(sorted(word)) not in hash_map):
                hash_map[''.join(sorted(word))]=[word]
            else:
                hash_map[''.join(sorted(word))].append(word)
        answer=[]
        for word in hash_map:
            answer.append(hash_map[word])
        return answer
s=Solution()
strs=["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))