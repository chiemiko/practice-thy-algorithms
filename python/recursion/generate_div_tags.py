class Solution:
    def generateDivTags(self, numberOfTags):
        """

        traversal choices: 
            
        <div> 
            next is a: <div>
            or b: </div

        """
        def dfs(left, right, curr, res):
            return

        res = []
        dfs(numberOfTags, numberOfTags, "", res)
        return res