class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hash_map={}
        for i in range(0,len(words)):
            if(words[i] not in hash_map):
                hash_map[words[i]]=1
            else:
                hash_map[words[i]]+=1
        # print(hash_map)
        sorted_items = sorted(hash_map.items(), key=lambda item: item[1])
        sorted_items=sorted_items[::-1]
        answer=[]
        for i in range(0,k):
            answer.append(sorted_items[i][0])
        return answer
s=Solution()
print(s.topKFrequent(["i","love","leetcode","i","love","coding"],2))