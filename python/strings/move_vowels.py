from collections import OrderedDict

class Solution():
    def moveVowels(s):
        """
        {1: e, 2: e, 5: o, 7: e, 8: a}
        
        [1, 2, 5, 7, 8]
            ^
        """
        vowels = set(['a','e','i','o','u'])
        s = list(s)
        v = OrderedDict()
        # create dictionary of vowels O(n*n)
        for i, letter in enumerate(s):
            if letter in vowels:
                v[i] = letter

        # update the original string
        v_idxes = list(v.keys())
        if len(v) > 0:
            for key_i in range(len(v_idxes)):
                s[v_idxes[key_i]] = v[v_idxes[key_i-1]]
        
        # last one
        res = "".join(s)
        print(res)
        return res

input = 'leatcodea'
output = 'laetcadoe'
print(Solution.moveVowels(input) == output)
