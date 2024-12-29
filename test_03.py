def longestCommonSubstring(s1: str, s2: str) -> str:
    res = 0
    local_array = []
    ans = ""

    for i in range(len(s1)):
        for j in range(len(s2)):
            current = 0
            while i + current < len(s1) and j + current < len(s2) and s1[i + current] == s2[j + current]:
                ans += s1[i + current]
                current += 1
            else:
                if ans != "":
                    local_array.append(ans)
                    ans = ""

            res = max(res, current)

    local_array.sort(key=len, reverse=True)

    if len(local_array) > 0:
        return local_array[0]
    else:
        return ""


def main() -> None:
    print(longestCommonSubstring("ABABC", "BABCA"))
    print(longestCommonSubstring("abcapple", "apple"))
    print(longestCommonSubstring("apple", "abcapple"))


if __name__ == '__main__':
    main()

# longestCommonSubstring('ABABC', 'BABCA') => 'BABC'
