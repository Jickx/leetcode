# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


print(str_str('notsadbutsad', 'sad'))
