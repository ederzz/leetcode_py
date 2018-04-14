"""

Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

给定一个字符串，找到没有重复字符的最长子串的长度
例子：
字符串为 "abcabcbb"，最长子串为"abc"，长度为3
字符串为 "bbbbb"，最长子串为"b"，长度为1
字符串为 "pwwkew"，最长子串为"wke"，长度为3

解题思路：
	找到字符串中每个字符结尾的最长子串，时间复杂度为 O(n)
"""

def lengthOfLengestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""

	charPos = {} # 存储字符串中的每个字符的最新索引
	maxLength = 0 # 最长子串的长度
	prePos = -1 # 子串开始位置
	index = 0
	for char in s:
		charPos[char] = -1
	for char in s:
		prePos = max(prePos, charPos[char])
		maxLength = max(maxLength, index - prePos)
		charPos[char] = index
		index += 1

	return maxLength

print(lengthOfLengestSubstring('12333456777'))