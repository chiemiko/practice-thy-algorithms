/*
MAIN IDEA:
    Use dynamic programming to save on run time

ORIGINAL PROBLEM: 
    https://leetcode.com/problems/fibonacci-number/
    
    Fibonacci Number equation: 
    The Fibonacci numbers, commonly denoted F(n) form a sequence, 
    called the Fibonacci sequence, such that each number is the sum 
    of the two preceding ones, starting from 0 and 1. 


*/
var fib = function(N) {
    // recursion but do recursive memoization! 
    var backtrack = function(curr_n){
        if (curr_n<=0){return 0}
        else if (curr_n===1){return 1}

        if (!memo[curr_n]) {
            memo[curr_n] = backtrack(curr_n-1) + backtrack(curr_n-2)
        }
        return memo[curr_n]
    }
    
    var memo = new Array(N).fill(0)
    res = backtrack(N)
    return res
};

var test = function(input, output){
    if (fib(input)===output) {
        console.log("success")
    }
    else {
        console.log("failure")
    }
}

test(2, 1)
test(3, 2)
test(4, 3)