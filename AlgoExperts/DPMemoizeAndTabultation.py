
from math import sqrt
tar = 7
arr = [5, 3, 4]

# Time O(n*m^2) where n is the length of the array and m is the target
# Space O(n*m)


def howSum(tar, arr):
    res = [None] * (tar+1)
    res[0] = []
    for i in range(tar+1):
        if res[i] == None:
            continue
        for num in arr:
            if num+i >= len(res):
                continue
            res[num+i] = res[i][:]
            res[num+i].append(num)


tar = 8
arr = [2, 3, 5]

# howSum(tar, arr)
# Time O(n*m^2) where n is the length of the array and m is the target
# Space O(n*m)


def bestSum(tar, arr):
    table = [None] * (tar+1)
    table[0] = []
    for i in range(tar+1):
        if table[i] == None:
            continue
        for num in arr:
            if num+i >= tar+1:
                continue
            if table[num+i] == None or len(table[i])+1 <= len(table[num+i]):
                table[num+i] = table[i][:]
                table[num+i].append(num)


# bestSum(tar, arr)

target = "abcdef"
words = ["ab", "abc", "cd", "def", "abcd"]


def canConstruct(target, words):
    if len(target) == 0:
        return True

    for word in words:
        n = len(word)
        if target[:n] == word:
            if canConstruct(target[n:], words):
                return True
    return False


def canConstructMemo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True

    for word in words:
        n = len(word)
        prefix = target[:n]
        if prefix == word:
            memo[target] = canConstructMemo(target[n:], words, memo)
            return True
    memo[prefix] = False
    return False


def canConstructTabulation(target, words):
    res = [False] * (len(target)+1)
    res[0] = True
    for i in range(len(target)):
        if res[i] == False:
            continue
        for word in words:
            n = len(word)
            if i + n > len(target):
                continue
            if word == target[i:n+i]:
                res[i+n] = True
    return res[-1]


# print(canConstructTabulation(target, words))
target = "purple"
words = ["purp", "p", "ur", "le", "purpl"]


# Time O(m^n * m) Space O(n*m) where m is the length of target and n is the length of words
def countConstruct(target, words):
    if target == "":
        return 1
    count = 0
    for word in words:
        n = len(word)
        prefix = target[:n]
        if prefix == word:
            count += countConstruct(target[n:], words)
    return count


# print(countConstruct(target, words))


# Time O(m^2 * n) Space O(n*m)
def countConstructMemo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    count = 0
    for word in words:
        n = len(word)
        prefix = target[:n]
        if prefix == word:
            count += countConstructMemo(target[n:], words, memo={})
        memo[target] = count
    return count


# print(countConstructMemo(target, words))

def countConstructTabulation(target, words):
    res = [0] * (len(target) + 1)
    res[0] = 1
    for i in range(len(target)):
        for word in words:
            n = len(word)
            if word == target[i:n+i]:
                res[n+i] += res[i]
    return res[-1]


# print(countConstructTabulation(target, words))

target = "abcdef"
words = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]

# Time O(n^m * m) Space O(m^2) where m is the length of the target, n is the length of the words array


def allConstruct(target, words):
    if target == "":
        return [[]]

    result = []

    for word in words:
        prefix = target[:len(word)]
        if prefix == word:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, words)
            for x in suffixWays:
                result.append([word] + x[:])
    return result


# print(allConstruct(target, words))

def allConstructMemo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in words:
        prefix = target[:len(word)]
        if prefix == word:
            suffix = target[len(word):]
            suffixWays = allConstructMemo(suffix, words)
            for x in suffixWays:
                result.append([word] + x[:])

    memo[target] = result
    return result


# print(allConstructMemo(target, words))
# allConstructMemo(target, words)
arr = [1, 1, 1, 1, 1, 1, 1]


def binearSearch(arr):
    l = 0
    r = len(arr)
    while l < r:
        m = l + (r-l)//2
        if arr[m] == 1:
            l = m+1
        elif arr[m] == 0:
            r = m
    return l


# a, b = map(int, input().split())
a = int(input())
b = int(input())

x = []
for i in range(1, int(sqrt(a)+1)):
    if a % i == 0:
        x.append(i)
        if i != sqrt(a):
            x.append(a//i)
x.sort()
print(x[b-1]) if b-1 < len(x) else print(-1)

# x = [i for i in range(1, a+1) if not a % i]
# print(x)
# print(b-1, len(x))
# print(x[b-1]) if b-1 < len(x) else print(-1)


# arr = [int(_) for _ in input().split()]

# count = n
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i] <= arr[j]:
#             count += 1
# print(count)

# dp = [0] * (n)
# for i in range(1, n):
#     print(dp)
#     sub = [dp[k] for k in range(i) if arr[k] < arr[i]]
#     dp[i] = 1 + max(sub, default=0)
# print(max(dp, default=0))
