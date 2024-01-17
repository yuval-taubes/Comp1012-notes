s = " My, name is Yuval Taubes"

print(len(s)) 
# Output: 26
# len(s) returns the length of the string, including spaces.

print(s.lower())
# Output: " my, name is yuval taubes"
# s.lower() returns a new string with all characters in lowercase.

print(s.upper())
# Output: " MY, NAME IS YUVAL TAUBES"
# s.upper() returns a new string with all characters in uppercase.

s.find("a") 
# Output: 4
# s.find("a") returns the index of the first occurrence of "a" in the string.

print(s.find("a", 4, 8))
# Output: -1
# s.find("a", 4, 8) searches for "a" between indices 4 and 8 (exclusive),
# but it doesn't find it, so it returns -1.

print(s.replace("a", "z"))
# Output: " My, nzme is Yuvzl Tzubes"
# s.replace("a", "z") replaces all occurrences of "a" with "z" in the string.

print(s.replace("a", "z", 2))
# Output: " My, nzme is Yuval Taubes"
# s.replace("a", "z", 2) replaces the first two occurrences of "a" with "z" in the string.

print(s.strip())
# Output: "My, name is Yuval Taubes"
# s.strip() removes leading and trailing whitespace from the string.

print(s.split())
# Output: ['My,', 'name', 'is', 'Yuval', 'Taubes']
# s.split() splits the string into a list of words based on whitespace.

print(s.split(","))
# Output: [' My', ' name is Yuval Taubes']
# s.split(",") splits the string into a list of substrings based on the comma.
