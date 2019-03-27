/**
 * Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
 * 
 * The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
 * 
 * You may assume the integer does not contain any leading zero, except the number 0 itself.
 * 
 * Written by: Daniel Hocking
 * Date created: 27/03/2019
 * https://leetcode.com/problems/plus-one/
 */

class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 0;
        int pos = digits.length - 1;
        
        digits[pos] += 1;
        do {
            digits[pos] += carry;
            carry = 0;
            if(digits[pos] == 10) {
                digits[pos] = 0;
                carry = 1;
            }
            pos--;
        } while(pos >= 0 && carry == 1);
        
        if(carry == 1) {
            int[] digits_1 = new int[digits.length + 1];
            digits_1[0] = 1;
            return digits_1;
        }
        return digits;
    }
}