'''
93. Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 


Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
'''


class Solution(object):
    '''
    First, we can check if the given string size is less than equal to 4, then return ?
    use four loops to get the each integers and check the if the current integer is valid, no leading 0 and less than equal to 255.
    Store the string as a int value with conversion
    at the last loop, check if it's valid, then append ther result into the fianl result array

    Time O(27) Space O(19) where 27 combiatnions to check and not more than 19 valid IP addresses
    '''

    def restoreIpAddresses(self, s):
        res = []
        n = len(s)
        for i in range(1, min(4, n)):
            address = ["", "", "", ""]
            address[0] = s[:i]
            if not self.validAt(address[0]):
                continue

            for j in range(i + 1, min(4, n-i) + i):
                address[1] = s[i:j]
                if not self.validAt(address[1]):
                    continue

                for k in range(j + 1, min(4, n-j) + j):
                    address[2] = s[j:k]
                    address[3] = s[k:]
                    if not self.validAt(address[2]) or not self.validAt(address[3]):
                        continue
                    res.append(".".join(address))
        return res

    def validAt(self, sValue):
        iValue = int(sValue)
        if iValue > 255:
            return False
        return len(str(iValue)) == len(sValue)
