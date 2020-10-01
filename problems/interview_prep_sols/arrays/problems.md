**Arrays:**
1. [Missing Number](https://leetcode.com/problems/missing-number/)
   * sum of n numbers
   * xor solution
   * cyclic sort
   * sign inverse (if 0 is present then gets complicated)
   * * https://leetcode.com/problems/find-the-duplicate-number/
  
2. [Majority Element](https://leetcode.com/problems/majority-element/)
    * sort and check for (n/2)+1 th element
    * hash count
    * moore voting algorithm

3. [Rotate Array](https://leetcode.com/problems/rotate-array/)
    * naive
    * reverse method
    * gcd method

4. [Single Number](https://leetcode.com/problems/single-number/)
    * xor solution
    * https://leetcode.com/problems/single-number-ii/ - count%3 of set bit, handle negative numbers
    * https://leetcode.com/problems/single-number-iii - xor and divide in groups based on first set bit
    * similar problem solutions are also available in 004.py
  
5. [Numbers Smaller than current](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
    * sort and remember indices - O(NlogN)
    * count/bucket sort - O(N), O(N)

6.  [Sort Array by Parity](https://leetcode.com/problems/sort-array-by-parity/)
    * simple saving to seperate lists
    * two pointer approach

7. [Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/)
    * python insert
  
8. [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
    * traverse from right

9. [Unsorted Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)
    * sort and check for unequal elements
    * find min from begin and max from ene which fails order and try placing them in correct position.

10. [Sort Colors](https://leetcode.com/problems/sort-colors/)
    * sort
    * three pointer, left(end of 0's), current(iterator) and right(start of 2's)
  
11. [Inversions in Array](https://practice.geeksforgeeks.org/problems/inversion-of-array/0)
    * Merge sort approach
    * gotcha, don't forget about equal elements.
    * Similar problem: [Local and Global Inversions](https://leetcode.com/problems/global-and-local-inversions/)
        * Posted a solution in leetcode discuss, read it.(not a merge sort based solution)

12. [Increasing triplet subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)
    * maintain prefix min and suffix max from both sides
    * A cool solution from leetcode discuss. 

13. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
    * prefix and suffix product approach
    * two pointer
    * always start product with 1

14. [Maximum sum sub array](https://leetcode.com/problems/maximum-subarray)
    * Kadane algorithm
    * current sum and max sum variables
    * simple dp => nums[i] = max(nums[i], nums[i-1] + nums[i]) => return max(nums)
    * sliding window, set sum to 0 when approaches negative sum

15. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
    * Solve this problem for sure
    * Kadane like

16.  [Find two missing Number in consecutive numbers]()
    * Simple hash or count
    * Sum, average based solution
    * xor solution

17.  [Find two repeating numbers in consecutive numbers]()
    * Simple hash
    * Cyclic sort
    * negative bit set
    * sum, product based algebraic solution
    * xor solution

18. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
    * with and without stack solution

19. [Rotate Matrix](https://leetcode.com/problems/rotate-image/submissions/) 
    * Transpose and swap
  
20. [Three Sum](https://leetcode.com/problems/3sum)
    * Similar problem

21. [Set Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
    * note which row, col are zero and make them zero

22. [Count negative numbers in sorted matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix)
    * O(n+m) climbing solutionf
    * O(mlogn) binary search solution

23. [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)
    * Naive
    * Binary Search and sort
    * Binary search and heap, heapq.nsmallest() => for query with k elements

24. [Median of Two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
    * Merge and return middles
    * Binary Search
      * divide A,B at i, j
      * i + j = (m+n) - (i+j)
      * pick j while doing binary search
      * calculate j using formula in step 2
      * if a[i] > b[j+1] => move j to right
      * if a[i+1] < b[j] => move j to left

25. [Missing Possitive Number](https://leetcode.com/problems/first-missing-positive/)
    * Sorting approach
    * Hash based approach
    * Cyclic sort
    * Bit inverse
    * https://leetcode.com/problems/missing-number/
    * https://leetcode.com/problems/find-the-duplicate-number/
    * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

26. [Game of Life](https://leetcode.com/problems/game-of-life/)
    * O(m*n) Space approach
    * space optimization: use dummy values to represent previous and current states together.



