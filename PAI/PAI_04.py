# 가장 흔한 단어, p151

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

        # Counter 모듈 사용하면 딕셔너리 형태로 저장.
        # most_common(1) 쓰면 가장 많이 나온값 추출[('ball',2)]형태로
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]