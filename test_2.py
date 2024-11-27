def reverse_string(s: str):
    ans = ''                          #empty string for store output
    for i in range(len(s)-1,-1,-1):   #Start at last letter, Stop at position -1 (for include first letter), Step -1 (reverse order)
        ans += s[i]
    return ans

assert reverse_string("abcd") == "dcba"
assert reverse_string("a3bE5dQPos") == "soPQd5Eb3a"
assert reverse_string("aka$aka") == "aka$aka"