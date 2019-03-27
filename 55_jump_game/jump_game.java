/**
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that position.
 * 
 * Determine if you are able to reach the last index.
 * 
 * Written by: Daniel Hocking
 * Date created: 27/03/2019
 * https://leetcode.com/problems/jump-game/
 */

class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length < 2) {
            return true;
        }
        
        int jumps_needed = 0;
        for(int i = nums.length - 2; i >= 0; i--) {
            jumps_needed++;
            if(nums[i] >= jumps_needed) {
                jumps_needed = 0;
            }
        }
        
        return jumps_needed == 0;
    }
}