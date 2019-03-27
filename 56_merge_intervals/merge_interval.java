/**
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Written by: Daniel Hocking
 * Date created: 27/03/2019
 * https://leetcode.com/problems/merge-intervals/
 */

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        int size = intervals.size();
        if(size < 2) {
            return intervals;
        }
        
        Collections.sort(intervals, new Comparator<Interval>() {
            @Override
            public int compare(Interval lhs, Interval rhs) {
                if(lhs.start < rhs.start || (lhs.start == rhs.start && lhs.end < rhs.end)) {
                    return -1;
                }
                return (lhs.start == rhs.start) && (lhs.end == rhs.end) ? 0 : 1;
            }
        });
        
        List<Interval> out_intervals = new ArrayList<Interval>();
        out_intervals.add(intervals.get(0));
        int j = 1;
        for(int i = 1; i < intervals.size(); i++) {
            Interval current = intervals.get(i);
            Interval previous = out_intervals.get(j - 1);
            
            if(current.start <= previous.end) {
                previous.end = Math.max(previous.end, current.end);
            } else {
                out_intervals.add(current);
                j++;
            }
        }
        return out_intervals;
    }
}