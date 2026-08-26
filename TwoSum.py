# 1. Two Sum

- **Difficulty:** Easy
- **Topic:** Array, Hash Table
- **LeetCode Link:** [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

---

## Intuition & Approach

The brute-force approach compares every pair of numbers using nested loops, which takes $O(n^2)$ time. 

We can optimize this to **$O(n)$** using a **Hash Map** (Python `dict`):
1. Traverse the array while keeping track of numbers and their indices in a hash map `seen`.
2. For each element `num`, calculate its required complement: `partner = target - num`.
3. If `partner` is already in `seen`, return `[seen[partner], i]`.
4. Otherwise, record `seen[num] = i` and continue.

---

## Python Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in seen:
                return [seen[partner], i]
            seen[num] = i
