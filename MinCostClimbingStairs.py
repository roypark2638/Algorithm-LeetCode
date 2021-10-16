'''
746. Min Cost Climbing Stairs

ou are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''


class Solution(object):
    '''
    DP is based on the concept of overlapping subproblems and optimal substructure. This is when the solution to a problem can be constructed from solutions to similar and smaller subproblems. Solving a smaller version of the problem can be easier and faster, thus if we break up the problem into smaller subproblems, solving them can lead us to the final solution eaiser and faster.

    Let's a look at an example costs = [0,1,2,3,4,5]. Since we can take 1 or 2 steps at a time, we need to reach either step 4 or step 5 (0-indexed), and then pay the respective cost to reach the top. For this example, to reach step 4 optimally would cost 2 by taking apth 0 -> 2 -> 4 (not counting the cost of step 4 yet since we are only talking about reaching the step right now). To reach step 5 optimally would cost 4 by taking path 1->3->5.

    Now, imagine that before we started the problem, somebody came up to us and said "to optimally reach step 4 costs 2 and to optimally reach step 5 costs 4." Well, then the problem is trivial - the answer is the minimum of 2 + cost[4] = 6 and 4 + cost[5] = 9. The only reason this was so easy was because we already knew the cost to reach steps 4 and 5.

    So how do we find the minimum cost to reach step 4 or step 5? Well, you might notice that it's the exact same problem, just with a smaller input. For example, finding the minimum cost to reach step 4 is like solving the original problem with input [01,2,3] (step 4 is the "top of the floor" now). To solve this subproblem, we need to find the minimum cost to reach steps 2 and 3, which requires us to answer the original problem for inputs [0,1] and [0,1,2].

    This pattern is known as a "recurrence relation", and in this case, the minimum cost to reach the ith step is equal to minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2]). As you can see, we get the soltuion for the ith step by using solutions from eariler steps. So, when does the sequence terminate? For this question, the base cases are given in the problem description - we are allowed to start at either step 0 or step 1, so minimumCost[0] and minimumCost[1] are both 0.

    Algorithm

    With out base cases and recurrence relation, we can now easily solve this problem.

    1. Define an array minimumCost, where minimumCost[i] represents the minimum cost of reaching the ith step. The array should be one element longer than costs and start with all elements set to 0.
        The reason why the array should contain one additional element is because we will treat the top floor as the step to reach.

    2. Iterate over the array starting at the 2nd index. The problem statement says we are allowed to start at the 0th or 1st step, so we know the minimum cost to reach those steps is 0.

    3. For each step, apply the recurrence relation - minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2]). As you can see, as we populate minimumCost, it becomes possible to solve future subproblems. For example, before solving the 5th and 6th steps we are required to solve the 4th step.

    4. At the end, return the final element of minimumCost. Remember, we are treating this "step" as the top floor that we need to reach.


    '''

    # Time O(n) Space O(n)
    # Bottom-Up Tabulation
    # def minCostClimbingStairs(self, cost):
    #     # Define an array minimumCost, where minimumCost[i] represents the minimum cost of reaching the ith step. the array should be one element longer than costs and start with all elements set to 0. The reason why the array should contain one additional element is because we will treat the top floor as the step to reach.
    #     minimumCost = [0 for _ in range(len(cost)+1)]

    #     # Iterate over the array starting at the 2nd index. The problem statement says we are allowed to start at the 0th or 1st step, so we know the minimum cost to reach those steps is 0.
    #     for i in range(2, len(minimumCost)):
    #         # For each step, apply the recurrence relation: minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2]). As you can see, as we populate minimumCost, it becomes possible to solve future subproblems. For example, before solving the 5th and 6th steps we are required to solve the 4th step.
    #         minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2])

    #     # At the end, return the final element of minimumCost. Remember, we are treating this "step" as the top floor that we need to reach.
    #     return minimumCost[-1]

    # Time O(n) Space O(n)
    # Top-down Memoization
    '''
    Top-down DP starts at the top and works its way down to the base cases. Typically, this is implemented through recursion, and then made eifficient using memoization. Memoization refers to sotring the results of expensive function calls in order to avoid duplicate computations.
    
    We will make use of the recurrence relation we found. This time, we will implement minimumCost as a function instead of an array. Again, minimumCost(i) will represent the minimum cost to reach the ith step. The base cases for this function will be minimumCost(0) = minimumCost(1) = 0, since we are allowed to start on either step 0 or step 1. For any other step i, we can refer to our recurrence relation - we know minimumCost(i) = min(cost[i-1] + minimumCost[i-1], cost[i-2] + minimumCost[i-2]).
    
    We can implement this function easily enough, but there's major problem - repeated computations. If we want to find minimumCost(5), then we call minimumCost(3) and minimumCost(4). However, minimumCost(4) will then call minimumCost(3), and both minimumCost(3) calls will call minimumCost(2), on top of another minimumCost(2) call from minimumCost(4).
    
    As you can see, there are a ton of repeat computations. When there are only 5 stairs, it might not seem that bad. However, imagine if there were 6 stairs instead. This entire image would be one child of the root. As n increases, the amount of computations required grows exponentially. So, how do we resolve this issue? If we calculate, say, minimumCost(3), then why should we calculate it again? Instead of going through the entire subtree every time we want to calculate minimumCost(#), let's instead of going through the entire subtree every time we want to calculate minimumCost(3), let's just store the value of minimumCost(3) after calculating it the first time, and refer to that instead.
    
    This is what memoization is - caching "expensive" function calls to avoid duplicate computaitons. Imagine what the recursion tree would look like for a call to minimumCost(10000), and how expensive calls like minimumCost(9998) would be to compute multiple times. We can use a hashmap for the memoization, where each key will have the value minimumCost(key).
    
    Algorithm.
    1. Define a hashmap memo, where memo[i] represents the minimum cost of reaching the ith step.
    2. Define a function minimumCost, where minimumCost(i) will determine the minimum cost to reach the ith step.
    3. In our function minimumCost, first check the base cases: return 0 when i == 0 or i == 1. Next, check if the argument i has already been calculated and stored in our hashmap memo. If so, return memo[i]. Otherwise, use the recurrence relation to calculate memo[i], and then return memo[i].
    4. Simply call and return minimumCost(cost.length). Once again, we can make use of the trick from approach 1 where we treat the top floor as an extra "step". Since cost is 0-indexed, cost.length will be an index 1 step above the last element of cost.
    '''
#     def minCostClimbingStairs(self, cost):
#         memo = {}
#         def minimumCost(i):
#             if i in memo:
#                 return memo[i]
#             if i <= 1:
#                 return 0
#             downOne = cost[i-1] + minimumCost(i-1)
#             downTwo = cost[i-2] + minimumCost(i-2)

#             memo[i] = min(downOne, downTwo)
#             return memo[i]


#         return minimumCost(len(cost))

    '''
    Our recurrence relation from the previous two approaches only cares about 2 steps below the current step. For example, if we are calculating the minimum cost to reach step 12, we only care about data from step 10 and step 11. While we would have needed to calculate the minimum cost for steps 2-9 as well, at the time of the actual calculation fro step 12, we no longer care about any of those steps.
    Therefore, instead of using O(n) space to keep an array, we can improve to O(1) space using only two variables.
    '''

    def minCostClimbingStairs(self, cost):
        minimumCost = [0, 0, 0]

        for i in range(2, len(cost)+1):
            minimumCost[2] = min(minimumCost[1] + cost[i-1],
                                 minimumCost[0] + cost[i-2])
            minimumCost[0] = minimumCost[1]
            minimumCost[1] = minimumCost[2]
        return minimumCost[2]
