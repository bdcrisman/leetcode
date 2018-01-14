#!/usr/bin/env python

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_list = sorted(nums1 + nums2)
        length = len(sorted_list)
        mid = int(length / 2)
        
        return sorted_list[mid] if length % 2 != 0 else \
              (sorted_list[mid] + sorted_list[mid - 1]) / 2.0

def main():
    l1 = [4, 18]
    l2 = [1, 3]
    print((Solution()).findMedianSortedArrays(l1, l2))

if __name__=='__main__':
    main()