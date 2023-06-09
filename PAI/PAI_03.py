# 로그파일 재정렬, p148

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters, digits = [],[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 람다 표현식으로 정렬
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        return letters + digits



