/**
 * Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
 * 
 * If the last word does not exist, return 0.
 * 
 * Note: A word is defined as a character sequence consists of non-space characters only.
 * 
 * Written by: Daniel Hocking
 * Date created: 27/03/2019
 * https://leetcode.com/problems/length-of-last-word/
 */

class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        if(s.length() == 0) {
            return 0;
        }
        
        String[] split_s = s.split("\\s+");
        return split_s[split_s.length - 1].length();
    }
}