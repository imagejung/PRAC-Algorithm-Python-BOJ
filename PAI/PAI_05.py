# 그룹 애너그램, p153

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 존재하지 않는 키값으로 삽입하려하면, 그값이 키값이 됨
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
