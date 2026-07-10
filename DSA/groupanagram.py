class Solution:
    def sortstring(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for s in strs:
            key=self.sortstring(s)
            if key in dict:
                dict[key].append(s)
            else:
                dict[key]=[s]

        return list(dict.values())        
