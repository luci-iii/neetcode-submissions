class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = {}

        for word in strs:
            order = ''.join(sorted(word))

            if order in groups:
                groups[order].append(word) 
            
            else:
                groups[order] = [word]      

        return list (groups.values())

    