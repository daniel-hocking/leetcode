/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 * 
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 * 
 * Note: Given n will be a positive integer.
 * 
 * Written by: Daniel Hocking
 * Date created: 27/03/2019
 * https://leetcode.com/problems/climbing-stairs/
 */

class Solution {
    public int climbStairs(int n) {
        if(n <= 3) {
            return n;
        }
        
        int nm1 = 2;
        int nm2 = 1;
        int total = 0;
        for(int i = 0; i < (n - 2); i++) {
            total = nm1 + nm2;
            nm2 = nm1;
            nm1 = total;
        }
        return total;
    }
}