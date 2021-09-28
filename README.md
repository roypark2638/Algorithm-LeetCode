# Algorithm-Leetcode

|  #  | Title  | Solution | Basic Idea |
| --- | ------------- | -------- | ------------ |
|  161  | [Reverse String](https://leetcode.com/problems/reverse-string/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ReverseString.py) | 1. Recursion<br/> Time O(n) Space O(n)<br/> 2. Two pointers<br/> Time O(n) Space O(1)
|  160  | [Reverse Prefix Of Word](https://leetcode.com/problems/reverse-prefix-of-word/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ReversePrefixOfWord.py) | 1. Pointer<br/> - Iterate word with enumerate and find the index of given ch.<br/> - Reverse word by slicing and return the result.
|  159  | [Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinimizeMaximumPairSumInArray.py) | 1. Sort and two pointers<br/> Time O(nlogn) Space O(1)
|  158  | [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/DotProductOfTwoSparesVectors.py) | Spare Vector is a vector that has mostly zero values, while a dense vector is a vector where most of the elements are non-zero. It's ineifficient to store a sparese vector as a one-dimentioanl array. Instead, we can store the non-zero values and their corresponding indices in a dictionary, with the index being the key.
|  157  | [Print Immutable Linked List in Reverse](https://leetcode.com/problems/print-immutable-linked-list-in-reverse/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/PrintImmutableLinkedListInReverse.py) | 1. Recursion<br/> Time O(n) Space O(n)<br/> 2. Divide and conquer<br/> Time O(nlogn) Space O(logn)<br/> 3. Two pointers, print from the back<br/> Time O(n^2) Space O(1)
|  156  | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/PeakIndexInAMountainArray.py) | 1. Bruth force<br/> Time O(n) space O(1)<br/> 2. Binary search<br/> Time O(logn) Space O(1)
|  155  | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/TheKWeakestRowsInAMatrix.py) | 1. Linear searching and sorting<br/> - Calculate Strengths and store in a tuple of strength and index.<br/> - Sort the tuple and return the indices.<br/> Time O(nm) + O(mlogm) = O(m * (n + logm)) Space O(m)<br/> 2. Binary searching and sorting/map<br/> - Find the number of 1s with binary search and same process from the above.<br/> Time O(m * (n + logm)) Space O(m)
|  154  | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/CountNegativeNumbersInASortedMatrix.py) | 1. Bruth Force. <br/> - Count all the negatives and return the count. <br/>Time O(nm) Space O(1)<br/> 2. Take advantage of the fact that it's sorted in non-increasing order.<br/> - Staircase. Start from left bottom and count the negatives. <br/>Time O(nm) Space O(1)
|  153  | [Find Smallest Common Element in All Rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/FindSmallestCommonElementInAllRows.py) | 1. Bruth-Force Hashmap <br/> 2. Binary Search 
|  152  | [Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/IntersectionOfThreeSortedArrays.py) | - Binary Search Time O(nlogn) Space O(logn)<br/> - Bruth-Force HashMap Time O(n) Space O(n)<br/> - Three Pointers Time O(n) Space O(1)
|  151  | [Remove Kth Node From End](https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/RemoveKthNodeFromEnd.py) | - Create 2 pointers, first and second.<br/> - Move second pointer to kth times<br/> - And move both of pointers until second is pointing to None<br/> - Now remove the node where first pointer is pointing to<br/> Time O(n) Space O(1).
|  150  | [Valid Starting City](https://www.algoexpert.io/questions/Valid%20Starting%20City)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ValidStartingCity.py) | Greedy Algorithm<br/> - Keep track of minGas and minCity.<br/> - Calculate milesLeft on each city and returns the city where has a minimum milesLeft. <br/>Time O(n) Space O(1)
|  149  | [Task Assignment](https://www.algoexpert.io/questions/Task%20Assignment)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/TaskAssignment.py) | Greedy Algorthim<br/> - Create a dictionary with an array as a value holding indicies.<br/> - Sort the given tasks and iterate k times<br/> Time O(nlogn) Space O(n)
|  148  | [Minimum Passes Of Matrix](https://www.algoexpert.io/questions/Minimum%20Passes%20Of%20Matrix)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinimumPassesOfMatrix.py) | - Find positive value index<br/> - From that index, find and update neighbors where has negative values. <br/> - Keep those updated neighbors for the next queue to update.<br/> Time O(w * h) SpaceO(w * h)
|  147  | [Disk Stacking](https://www.algoexpert.io/questions/Disk%20Stacking)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/DiskStacking.py) | Dyanmic Programming Time O(n^2) Space O(n)<br/> - Sort the disks by height and keep track of the tallest heights on each index<br/> - Use two for-in loop to find stackable disks and store the heights and sequences.
|  146  | [Reverse Linked List](https://www.algoexpert.io/questions/Reverse%20Linked%20List)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ReverseLinkedList.py) | - Create 3 pointers. prev, curr, and next. <br/> Time O(n) Space O(1)
|  145  | [Remove Islands](https://www.algoexpert.io/questions/Remove%20Islands)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/RemoveIslands.py) | - Iterate the edges of the matrix and mark all of the connected 1s by converting it to the 2<br/> - Iterate the entire matrix and change left 1s to the 0 and 2s to the 1<br/> Time O(wh) Space O(wh) width and height.
|  144  | [First Non-Repeating Character](https://www.algoexpert.io/questions/First%20Non-Repeating%20Character)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/FirstNon-RepeatingCharacter.py) | - Create a frequency table for each char in string.<br/> - And iterate string index and compare to the frequency table.<br/> - If the frequency value is equal to 1, return the current index.<br/> Time O(n) Space O(1). Space is constant because lowercase English alphabet letters are constant.
|  143  | [Selection Sort](https://www.algoexpert.io/questions/Selection%20Sort)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/SelectionSort.py) | - Divide into two sections into sorted and unsorted. <br/> - Find the smallestIndex and at the end of each iteration, swap the value to the left. <br/>Time O(n^2) Space O(1)
|  142  | [Insertion Sort](https://www.algoexpert.io/questions/Insertion%20Sort)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/InsertionSort.py) | Time O(n^2) Space O(1)
|  141  | [Bubble Sort](https://www.algoexpert.io/questions/Bubble%20Sort)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/BubbleSort.py) | - i, j pointer moves together until j < len(array) - i<br/> - Check if there is a change happended each loop, if not, break and return.<br/> Time O(n^2) Space O(1).
|  140  | [Youngest Common Ancestor](https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/YoungestCommonAncestor.py) | - Given two descendatns have different level in the tree<br/> - In order to find the common ancestor, we need to make those two decendants at the same level.<br/> - Calculate both of depth in the tree and move lower decendant to the same level of higher decendant.<br/> - Now, two decendants are at the same level.<br/> - Move both of decendants until they are pointing to the same node.
|  139  | [River Sizes](https://www.algoexpert.io/questions/River%20Sizes)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/RiverSizes.py) | - Create an array to hold the result sizes<br/> - Copy the matrix and assign initial value of False to mark if we visited or not<br/> - Use two for loops<br/> - If visited, then continue, otherwise call traverseNode function<br/> - Use BFS and queue to traverse the adjacent nodes<br/> - Check if current position's status is true or not, if yes, continue, if not then set the current position's visit status True<br/> - getUnvisitiedNeighbors and append those neighbors to the queue<br/> - If currentRiverSize > 0, then append that into the result sizes array.
|  138  | [Breath-first Search](https://www.algoexpert.io/questions/Breadth-first%20Search)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/Breadth-firstSearch.py) | Time O(v + e) Space O(v).<br/> Use a queue data structure.
|  137  | [Single Cycle Check](https://www.algoexpert.io/questions/Single%20Cycle%20Check)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/SingleCycleCheck.py) | - Handle the index that exceed the len(array)<br/> - Handle a negative index <br/> While we're iterating the array, if we come back to the starting index, we know it fails the condition.<br/> Time O(n) Space O(1)
|  136  | [Kadane's Algorithm](https://www.algoexpert.io/questions/Kadane's%20Algorithm)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/KadanesAlgorithm.py) | Dynamic Programming<br/> Kadane's algorithm is used to find the maxmimum adjacent sum in the given integer array including negative values. Time O(n) Space O(1).<br/> - Keep track of two variables, currentMaxEnding and maxSoFar.
|  135  | [Levenshtein Distance](https://www.algoexpert.io/questions/Levenshtein%20Distance)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/LevenshteinDistance.py) | Dynaimc Programming<br/> Solution 1<br/> - Create two dimentional array size of (n+1) * (m+1) to keep track of the minimum editions. Time O(nm) Space O(nm) where n is the length of str1 and m is the length of the str2<br/>Optimal Solution<br/> - Create only two smaller length of rows to keep track the minimum editions. Time O(nm) Space O(min(n, m)).
|  134  | [Min Number Of Coins For Chnage](https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinNumberOfCoinsForChange.py) | Dynaimc Programming<br/> - Create an array with Nth number filled with float("inf") in Python and set array[0] = 0.<br/> - Each array position represetns the minimum number of ways to make the given change and we will build it with each iteration of denoms.<br/> Time O(nd) where n is the given target amount and d is the number of elements in denoms array. <br/> Space O(n).
|  133  | [Number Of Ways To Make Change](https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/NumberOfWaysToMakeChange.py) | Dynamic Programming<br/> - Create an array with Nth number filled with 0 and set array[0] = 1<br/> - Each array position represents the number of ways to make the change and we will build with each iteration of denoms.<br/> If denom <= ways: then ways[amount] += ways[amount - denom]<br/> Time O(nd) where n is the given target amount and d is the number of elements in denoms array.<br/> Space O(n).
|  132  | [Max Subset Sum No Adjacent](https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MaxSubsetSumNoAdjacent.py) | Dynamic Programming solution<br/> 1. Using a new array space solution Time O(n) Space O(n)<br/> 2. Using two temp variables first, second to keep track of current sum. <br/> - Optimal Solution Time O(n) Space O(1).
|  131  | [Invert Binary Tree](https://www.algoexpert.io/questions/Invert%20Binary%20Tree)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/InvertBinaryTree.py) | 1. Breath First Search (Iterative Solution) Time O(n) Space O(n)<br/> 2. Recursive Solution <br/> - Time O(n) where n is the number of the nodes in the tree<br/> - Space O(d) where d is the depth of the tree.
|  130  | [Min Height BST](https://www.algoexpert.io/questions/Min%20Height%20BST)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinHeightBST.py) | Either write a function by using given insert method -> Time O(nlogn) Space O(n)<br/> Or write a function manually constrcuting the min height bst with given sorted array consisting of distinct integers -> Time O(n) Space O(n).
|  129  | [BST Traversal](https://www.algoexpert.io/questions/BST%20Traversal)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/BSTTraversal.py) | Use recursion to create inOrderTraverse, preOrderTraverse, and postOrderTraverse. Time O(n) and Space O(n) where n is the number of the nodes in the BST.
|  128  | [Validate BST](https://www.algoexpert.io/questions/Validate%20BST)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ValidateBST.py) | Use recursion, divide and conquer algorithm. Find out if each subtree is valid BST. Time O(n) and Space O(d) where n is the number of the nodes and d is the depth of the tree.
|  127  | [BST Construction](https://www.algoexpert.io/questions/BST%20Construction)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/BSTContruction.py) | insert, contains, and remove methods
|  126  | [Merge Overlapping Intervals](https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/mergeOverlappingIntervals.py) | - Sort the array based on the startInterval in the given intervals array<br/> - Create a mergedIntervals array to store the result, and append the first interval from the sorted intervals<br/> - Iterate range from 1 to end of the array<br/>  - - Get the currentStartInterval and previousEndInterval value<br/> - - If currentStart is less than or equal to the previousEndInterval<br/> - - - True, update the mergedIntervals's last interval's endInterval to max value of sortedInterval end or mergedIntervals end<br/> - - - False, append the sortedIntervals to mergedIntervals<br/> - return mergedIntervals as the result
|  125  | [First Duplicate Value](https://www.algoexpert.io/questions/First%20Duplicate%20Value)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/FirstDuplicateValue.py) | 1. HashMap Time O(n) Space O(n)<br/> - Create a hashmap to store the value that we found and mark it.<br/> - Iterate the array and check if the value exist in our hashmap.<br/><br/> 2. Array Munipulation Time O(n) SpaceO(1)<br/> - Since the given prompt indicates that an array of integers between 1 and n, inclusive, where n is the length of the array and we can mutate the given array, we can use this method.<br/> - Iterate array and create seenIndex by abs(value) - 1 to mark by negative value the found value on that index.<br/> - If the value from seenIndex is negative, return that abs(value).
|  124  | [Array Of Products](https://www.algoexpert.io/questions/Array%20Of%20Products)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ArrayOfProducts.py) | - Create a new array with value 1 on each position<br/> - Use for-in loop to store a current leftRunningProduct value into the new array products<br/> - Use another for-in loop to multiple the current products[i] with a current rightRunningProduct value into products array.<br/> - Return products array as the result.
|  123  | [Longest Peak](https://www.algoexpert.io/questions/Longest%20Peak)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/LongestPeak.py) | - Start from index 1 and check if current position is a peak<br/> - If it's a peak then calculate left and right length to find currentPeakLength<br/> - Update the longestPeakLength if currentPeakLength is greater<br/> - Update index to right pointer.
|  122  | [Spiral Traverse](https://www.algoexpert.io/questions/Spiral%20Traverse)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/SpiralTraverse.py) | Time O(n) and Space O(n) where n is the total number of the two dimential array elements.
|  121  | [Monotonic Array](https://www.algoexpert.io/questions/Monotonic%20Array)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MonotonicArray.py) | 1. check if len(array) <= 2, then return true.<br/>2. get first direction by array[1] - array[0].<br/>3. loop through the array from range 2.<br/>  4. check if the direction is meaningful(if direction == 0, then update the direction by array[i] - array[i-1].<br/>  5. check if current direction is broken from previous direction then return False. Otherwise return True.
|  120  | [Move Element To End](https://www.algoexpert.io/questions/Move%20Element%20To%20End)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ElementToEnd.py) | 1. Use left and right pointers.<br/>2. While left < right<br/>3. while left < right and left value is not toMove value update the left and while left < right and array[right] is equal to toMove value, update the right pointer. <br/>Swap the values.
|  119  | [Smallest Difference](https://www.algoexpert.io/questions/Smallest%20Difference)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/SmallestDifference.py) | Use two pointers to compare the difference. Keep track of smallest and current differences. Loop while any of them doesn't exceed their array index. Keep track of a current difference and check if smallest > current than, update the smallest variable.
|  118  | [Permutations](https://www.algoexpert.io/questions/Permutations)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/Permutations.py) | Time O(n^2*n!) Space O(n*n!). <br/> Pass curPerm and resultPerms recursively. When given array is not empty and curPerm is not empty, append the curPerm to resultPerms. Otherwise, iterate the rest of the given array and slice the slice the array to newArray and newPerm.
|  117  | [Palindrome Check](https://www.algoexpert.io/questions/Palindrome%20Check)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/PalindromeCheck.py) | 1. Create two pointers, one on the left and one on the right. <br/>2. While left < right: check if the char is the same or not. If it's not same, return False. Otherwise, increment both of the pointers.
|  116  | [Find Three Laregest Numbers](https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/FindThreeLargestNumbers.py) | Time: O(n) and Space: O(1)<br/>Set a result array with 3 given array values and sort it. and iterate rest of the array and swap the values depends on large numbers.
|  115  | [Binary Search](https://www.algoexpert.io/questions/Binary%20Search)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/BinarySearch.py)  | Use 3 pointers, left, right, mid.<br/>1. left = 0<br/>2. right = len(array) - 1<br/>3. mid = (left + right) // 2<br/>Iterate the sorted array and find the target with 3 pointers.
|  114  | [Nth Fibonacci](https://www.algoexpert.io/questions/Nth%20Fibonacci)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/NthFibonacci/main.py)  | Create a temp array to hold two values, lastTwo = [0,1]. And update the value.<br/>lastTwo[1] = lastTwo[0] + lastTwo[1] <br/>lastTwo[0] = lastTwo[1]
|  113  | [Remove Duplicates From Linked List](https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/RemoveDuplicatesFromLinkedList/main.py)  | Start from the head and check if nextDistinctNode.value is not none and equal to currentNode.value, if yes, then keep move the nextDistinctNode to next and finally move currentNode pointer to the nextDistinctNode to remove duplicates until we reach the end of the sorted singly linked list.
|  112  | [Tandem Bicycle](https://www.algoexpert.io/questions/Tandem%20Bicycle)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/TandemBicycle/main.py)  | 1. Sort the speeds based on fastest value<br/>2. iterate through speeds array and add up the max speeds
|  111  | [Class Photo](https://www.algoexpert.io/questions/Class%20Photos)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ClassPhotos/main.py)  | 1. Sort the array in reverse order<br/>2. Find the group where has tallest student and place that color student group to back row<br/>3. Compare each value in the array if back row students are strictly greater than front row students
|  110  | [Minimum Waiting Time](https://www.algoexpert.io/questions/Minimum%20Waiting%20Time)  | [Python](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinimumWaitingTime/main.py)  | 1. Sort the array<br/>2. Create two variables waitingTime, minimumTotal<br/>3. Iterate array<br/>- 4. MinimumTotal += waitingTime<br/>- 5. WaitingTime += n|
|  109  | [Merge Overlapping Intervals](https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MergeOverlappingIntervals.playground/Contents.swift)  | 1. Sort by start time<br/>2. Create an empty mergedIntervals for result<br/>3. Create currentInterval variable<br/>4. Insert first interval into the result array<br/>5. Loop the intervals.<br/>- 6. Get currentIntervalEnd, nextIntervalStart and nextIntervalEnd<br/>- 7. If overlapping -> get the max from currentEnd & nextEnd and update existing merged result array.<br/>- 8. if not overlapping -> assign nextInterval to currentInterval and append the updated currentInterval to the result array|
|  108  | [Three Number Sum](https://www.algoexpert.io/questions/Three%20Number%20Sum)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ThreeNumberSum.playground/Contents.swift)  | 1. Sort given array<br/>2. Create an empty triplets array<br/>3. for pivot in 0..<array.count-2<br/>- 4. Create two pointers, left and right. Left = pivot + 1, right = array.count - 1<br/>- 5. while left < right<br/>-- 6. Sum up 3 numbers and move the pointer accordingly depends on the comparison. |
|  107  | [Minimum Characters For Words](https://www.algoexpert.io/questions/Minimum%20Characters%20For%20Words)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/MinimumCharactersForWords.playground/Contents.swift)  | O(n * I) time, O(c) space - where n is the number of words, I is the length of the longest word, and c is the number of unique characters across all words. |
|  106  | [Height Balanced Binary Tree](https://www.algoexpert.io/questions/Height%20Balanced%20Binary%20Tree)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/HeightBalancedBinaryTree.playground/Contents.swift)  | Recursively calculate the left and right subtree heights from each node. determine if the subtree rooted at that node is balanced. If you make it through the entire tree without finding any unbalanced subtrees, and if you determine that the heights of the main two subtrees aren't more than 1 apart, then the entire tree is balanced. |
|  105  | [Non-Constrcutible Change](https://www.algoexpert.io/questions/Non-Constructible%20Change)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/Non-ConstructibleChange.playground/Contents.swift)  | Create a variable to store the amount of change that you can curerntly create up to. Sort all of your coins, and loop through them in ascending order. At every iteration, compare the current coin to the maount of change that you can currently create up to. |
|  104  | [Tournament Winner](https://www.algoexpert.io/questions/Tournament%20Winner)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/TournamentWinner.playground/Contents.swift)  | 1. Create a map [String: Int]<br/>2. Loop each competitions and increase winner's point at the map<br/>3. Return the highest score of the team|
|  103  | [Sorted Squared Array](https://www.algoexpert.io/questions/Sorted%20Squared%20Array)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/SortedSquaredArray.playground/Pages/Pointer-Method.xcplaygroundpage/Contents.swift)  | 2 methods are available and the optimal solution. <br/>1. Create array with the same length of the given array<br/>2. Create pointers for left, right and index<br/>3. Loop while left <= right.<br/> - Fill the array from the back with larger number. <br/> - Move the pointer and index accordingly |
|  102  | [Validate Subsequence](https://www.algoexpert.io/questions/Validate%20Subsequence)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/ValidateSubsequence.playground/Contents.swift)  | 1.Set sequence index = 0 and final index = sequence.count<br/>2. Increment index<br/> - If sequence == array -> increment both<br/> - If sequence != array -> increment array only<br/>3. If sequence index == sequence.count -> true<br/>Time O(N), Space O(1)|
|  101  | [Two Number Sum](https://www.algoexpert.io/questions/Two%20Number%20Sum)  | [Swift](https://github.com/roypark2638/Algorithm-Leetcode/blob/main/TwoNumberSum.playground/Pages/HashMap-Method.xcplaygroundpage/Contents.swift)  | 1. HashMap. Time: O(n), Sapce: O(n)<br/>2. Sort and search with two pointers O(n) and O(1) space|
