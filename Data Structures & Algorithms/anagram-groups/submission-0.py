class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        var = defaultdict(list)

        for i in strs:
            sorted_i = "".join(sorted(i))
            var[sorted_i].append(i)

        return list(var.values())
        