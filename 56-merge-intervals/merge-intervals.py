class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0]) # sort by start
        output = [intervals[0]] # save into output

        for start,end in intervals[1:]:
            lastEnd = output[-1][1] # end of last element

            if start <= lastEnd: # if current start less than prev element's end then it overlaps
                output[-1][1] =  max(lastEnd, end) #update the lastEnd to the highest no
            else:
                output.append([start,end]) # if they don't overlap then simply append to output
        return output