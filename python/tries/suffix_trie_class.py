class Trie():
    def __init__(self, s):
        self.root = {}
        self.populate_trie(s)

    def populate_trie(self, s):
        """ 
        TIMER: do it in five minutes!
        
        main idea, iterate ONE SUFFIX SUBSTRING AT A TIME
         
        !!! BUILDING THE RECURSIVE TRIE STRUCUTRE! 

        base case: sub  
           
            
         """
        def populate(substring, curr_node):
            if len(substring) == 0:
                curr_node['*'] = True
                return

            char = substring[0]
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node.get(char)
            populate(substring[1:], curr_node)

        for i, char in enumerate(s):
            populate(s[i:], self.root)
    
    def search(self, search_s):
        curr = self.root
        for char in search_s:
            if char not in curr:
                return False
            else:
                curr = curr.get(char)
        if "*" in curr:
            return True
        else:
            return False
    

solution = True
input = "babc"



# ex = {
#     'c': True,
#     'b': {
#         'c': True,
#         'a': {
#              'b': {
#                 'c': 
#                     True } }
#         },
#     'a': {'b': {'c': True}} 

# }



search_string = "abc"

t = Trie(input)
print(t.root)

print(t.search(search_string) == solution)