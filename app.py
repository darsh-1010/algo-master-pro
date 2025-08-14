from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# DSA Problems Database - Comprehensive Collection
DSA_PROBLEMS = {
    # Array Problems
    "Two Sum": {
        "statement": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
        "difficulty": "Easy",
        "category": "Array, Hash Table",
        "tags": ["array", "hash-table", "two-pointers"]
    },
    "Best Time to Buy and Sell Stock": {
        "statement": "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.",
        "difficulty": "Easy",
        "category": "Array, Dynamic Programming",
        "tags": ["array", "dynamic-programming", "greedy"]
    },
    "Maximum Subarray": {
        "statement": "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
        "difficulty": "Medium",
        "category": "Array, Dynamic Programming",
        "tags": ["array", "dynamic-programming", "divide-and-conquer"]
    },
    "Move Zeroes": {
        "statement": "Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.",
        "difficulty": "Easy",
        "category": "Array, Two Pointers",
        "tags": ["array", "two-pointers", "in-place"]
    },
    "Container With Most Water": {
        "statement": "Given n non-negative integers height where each represents a point at coordinate (i, height[i]). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.",
        "difficulty": "Medium",
        "category": "Array, Two Pointers",
        "tags": ["array", "two-pointers", "greedy"]
    },
    "3Sum": {
        "statement": "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.",
        "difficulty": "Medium",
        "category": "Array, Two Pointers",
        "tags": ["array", "two-pointers", "sorting"]
    },
    "Subarray Sum Equals K": {
        "statement": "Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.",
        "difficulty": "Medium",
        "category": "Array, Hash Table",
        "tags": ["array", "hash-table", "prefix-sum"]
    },
    "Product of Array Except Self": {
        "statement": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.",
        "difficulty": "Medium",
        "category": "Array, Prefix Sum",
        "tags": ["array", "prefix-sum", "math"]
    },
    "Trapping Rain Water": {
        "statement": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        "difficulty": "Hard",
        "category": "Array, Two Pointers",
        "tags": ["array", "two-pointers", "dynamic-programming", "stack"]
    },
    "Merge Intervals": {
        "statement": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the points in the input.",
        "difficulty": "Medium",
        "category": "Array, Sorting",
        "tags": ["array", "sorting", "greedy"]
    },

    # String Problems
    "Valid Parentheses": {
        "statement": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.",
        "difficulty": "Easy",
        "category": "String, Stack",
        "tags": ["string", "stack", "matching"]
    },
    "Longest Substring Without Repeating Characters": {
        "statement": "Given a string s, find the length of the longest substring without repeating characters.",
        "difficulty": "Medium",
        "category": "String, Sliding Window",
        "tags": ["string", "sliding-window", "hash-table"]
    },
    "Longest Palindromic Substring": {
        "statement": "Given a string s, return the longest palindromic substring in s.",
        "difficulty": "Medium",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dynamic-programming", "palindrome"]
    },
    "Valid Anagram": {
        "statement": "Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.",
        "difficulty": "Easy",
        "category": "String, Hash Table",
        "tags": ["string", "hash-table", "sorting"]
    },
    "Group Anagrams": {
        "statement": "Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.",
        "difficulty": "Medium",
        "category": "String, Hash Table",
        "tags": ["string", "hash-table", "sorting"]
    },
    "Longest Common Prefix": {
        "statement": "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ''.",
        "difficulty": "Easy",
        "category": "String, Trie",
        "tags": ["string", "trie", "divide-and-conquer"]
    },
    "Valid Palindrome": {
        "statement": "A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.",
        "difficulty": "Easy",
        "category": "String, Two Pointers",
        "tags": ["string", "two-pointers", "palindrome"]
    },
    "Minimum Window Substring": {
        "statement": "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ''.",
        "difficulty": "Hard",
        "category": "String, Sliding Window",
        "tags": ["string", "sliding-window", "hash-table", "two-pointers"]
    },

    # Linked List Problems
    "Reverse Linked List": {
        "statement": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
        "difficulty": "Easy",
        "category": "Linked List, Recursion",
        "tags": ["linked-list", "recursion", "two-pointers"]
    },
    "Merge Two Sorted Lists": {
        "statement": "You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.",
        "difficulty": "Easy",
        "category": "Linked List, Recursion",
        "tags": ["linked-list", "recursion", "sorting"]
    },
    "Linked List Cycle": {
        "statement": "Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.",
        "difficulty": "Easy",
        "category": "Linked List, Two Pointers",
        "tags": ["linked-list", "two-pointers", "cycle-detection"]
    },
    "Remove Nth Node From End of List": {
        "statement": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
        "difficulty": "Medium",
        "category": "Linked List, Two Pointers",
        "tags": ["linked-list", "two-pointers", "fast-slow"]
    },
    "Add Two Numbers": {
        "statement": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
        "difficulty": "Medium",
        "category": "Linked List, Math",
        "tags": ["linked-list", "math", "carry"]
    },
    "Merge k Sorted Lists": {
        "statement": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
        "difficulty": "Hard",
        "category": "Linked List, Divide and Conquer",
        "tags": ["linked-list", "divide-and-conquer", "heap", "merge-sort"]
    },

    # Tree Problems
    "Binary Tree Inorder Traversal": {
        "statement": "Given the root of a binary tree, return the inorder traversal of its nodes' values.",
        "difficulty": "Easy",
        "category": "Tree, Depth-First Search",
        "tags": ["tree", "dfs", "inorder", "recursion"]
    },
    "Maximum Depth of Binary Tree": {
        "statement": "Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "difficulty": "Easy",
        "category": "Tree, Depth-First Search",
        "tags": ["tree", "dfs", "recursion", "height"]
    },
    "Symmetric Tree": {
        "statement": "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).",
        "difficulty": "Easy",
        "category": "Tree, Depth-First Search",
        "tags": ["tree", "dfs", "symmetric", "recursion"]
    },
    "Binary Tree Level Order Traversal": {
        "statement": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
        "difficulty": "Medium",
        "category": "Tree, Breadth-First Search",
        "tags": ["tree", "bfs", "level-order", "queue"]
    },
    "Construct Binary Tree from Preorder and Inorder Traversal": {
        "statement": "Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.",
        "difficulty": "Medium",
        "category": "Tree, Array",
        "tags": ["tree", "array", "recursion", "divide-and-conquer"]
    },
    "Binary Tree Maximum Path Sum": {
        "statement": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.",
        "difficulty": "Hard",
        "category": "Tree, Dynamic Programming",
        "tags": ["tree", "dynamic-programming", "dfs", "path-sum"]
    },

    # Dynamic Programming Problems
    "Climbing Stairs": {
        "statement": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "difficulty": "Easy",
        "category": "Dynamic Programming, Math",
        "tags": ["dynamic-programming", "math", "fibonacci"]
    },
    "Coin Change": {
        "statement": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Greedy",
        "tags": ["dynamic-programming", "greedy", "coin-change"]
    },
    "Longest Increasing Subsequence": {
        "statement": "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Binary Search",
        "tags": ["dynamic-programming", "binary-search", "subsequence"]
    },
    "Word Break": {
        "statement": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, String",
        "tags": ["dynamic-programming", "string", "segmentation"]
    },
    "House Robber": {
        "statement": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Array",
        "tags": ["dynamic-programming", "array", "robbery"]
    },
    "Edit Distance": {
        "statement": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word: Insert a character, Delete a character, Replace a character.",
        "difficulty": "Hard",
        "category": "Dynamic Programming, String",
        "tags": ["dynamic-programming", "string", "edit-distance", "levenshtein"]
    },

    # Graph Problems
    "Number of Islands": {
        "statement": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.",
        "difficulty": "Medium",
        "category": "Graph, Depth-First Search",
        "tags": ["graph", "dfs", "flood-fill", "islands"]
    },
    "Course Schedule": {
        "statement": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses. Otherwise, return false.",
        "difficulty": "Medium",
        "category": "Graph, Topological Sort",
        "tags": ["graph", "topological-sort", "dfs", "cycle-detection"]
    },
    "Clone Graph": {
        "statement": "Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.",
        "difficulty": "Medium",
        "category": "Graph, Depth-First Search",
        "tags": ["graph", "dfs", "clone", "hash-table"]
    },
    "Pacific Atlantic Water Flow": {
        "statement": "There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.",
        "difficulty": "Medium",
        "category": "Graph, Depth-First Search",
        "tags": ["graph", "dfs", "ocean-flow", "multi-source"]
    },
    "Redundant Connection": {
        "statement": "In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph. Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.",
        "difficulty": "Medium",
        "category": "Graph, Union Find",
        "tags": ["graph", "union-find", "cycle-detection", "disjoint-set"]
    },

    # Heap Problems
    "Top K Frequent Elements": {
        "statement": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
        "difficulty": "Medium",
        "category": "Heap, Hash Table",
        "tags": ["heap", "hash-table", "frequency", "top-k"]
    },
    "Find Median from Data Stream": {
        "statement": "The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values. Implement the MedianFinder class: MedianFinder() initializes the MedianFinder object. void addNum(int num) adds the integer num from the data stream to the data structure. double findMedian() returns the median of all elements so far.",
        "difficulty": "Hard",
        "category": "Heap, Design",
        "tags": ["heap", "design", "median", "two-heaps"]
    },
    "Merge k Sorted Lists": {
        "statement": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
        "difficulty": "Hard",
        "category": "Heap, Linked List",
        "tags": ["heap", "linked-list", "merge", "priority-queue"]
    },

    # Binary Search Problems
    "Binary Search": {
        "statement": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.",
        "difficulty": "Easy",
        "category": "Binary Search, Array",
        "tags": ["binary-search", "array", "search"]
    },
    "Search in Rotated Sorted Array": {
        "statement": "There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.",
        "difficulty": "Medium",
        "category": "Binary Search, Array",
        "tags": ["binary-search", "array", "rotated", "pivot"]
    },
    "Find First and Last Position of Element in Sorted Array": {
        "statement": "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.",
        "difficulty": "Medium",
        "category": "Binary Search, Array",
        "tags": ["binary-search", "array", "range", "first-last"]
    },
    "Median of Two Sorted Arrays": {
        "statement": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).",
        "difficulty": "Hard",
        "category": "Binary Search, Array",
        "tags": ["binary-search", "array", "median", "divide-and-conquer"]
    },

    # Backtracking Problems
    "Subsets": {
        "statement": "Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.",
        "difficulty": "Medium",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "subsets", "power-set"]
    },
    "Permutations": {
        "statement": "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
        "difficulty": "Medium",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "permutations", "recursion"]
    },
    "Combination Sum": {
        "statement": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.",
        "difficulty": "Medium",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "combination", "sum"]
    },
    "N-Queens": {
        "statement": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.",
        "difficulty": "Hard",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "n-queens", "chess"]
    },

    # Design Problems
    "LRU Cache": {
        "statement": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the LRUCache class: LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of the key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.",
        "difficulty": "Medium",
        "category": "Design, Hash Table",
        "tags": ["design", "hash-table", "lru", "doubly-linked-list"]
    },
    "Implement Trie (Prefix Tree)": {
        "statement": "A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker. Implement the Trie class: Trie() Initializes the trie object. void insert(String word) Inserts the string word into the trie. boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise. boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.",
        "difficulty": "Medium",
        "category": "Design, Trie",
        "tags": ["design", "trie", "prefix-tree", "string"]
    },
    "Design Underground System": {
        "statement": "An underground railway system is tracking customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another. Implement the UndergroundSystem class: void checkIn(int id, string stationName, int t), void checkOut(int id, string stationName, int t), double getAverageTime(string startStation, string endStation).",
        "difficulty": "Medium",
        "category": "Design, Hash Table",
        "tags": ["design", "hash-table", "average", "transportation"]
    },
    
    # Advanced Array Problems
    "Sliding Window Maximum": {
        "statement": "Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.",
        "difficulty": "Hard",
        "category": "Array, Sliding Window",
        "tags": ["array", "sliding-window", "deque", "monotonic-queue"]
    },
    "Longest Consecutive Sequence": {
        "statement": "Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.",
        "difficulty": "Medium",
        "category": "Array, Hash Table",
        "tags": ["array", "hash-table", "union-find"]
    },
    "Find All Duplicates in an Array": {
        "statement": "Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.",
        "difficulty": "Medium",
        "category": "Array, Hash Table",
        "tags": ["array", "hash-table", "in-place"]
    },
    "Rotate Array": {
        "statement": "Given an array, rotate the array to the right by k steps, where k is non-negative.",
        "difficulty": "Medium",
        "category": "Array, Two Pointers",
        "tags": ["array", "two-pointers", "rotation"]
    },
    "Spiral Matrix": {
        "statement": "Given an m x n matrix, return all elements of the matrix in spiral order.",
        "difficulty": "Medium",
        "category": "Array, Matrix",
        "tags": ["array", "matrix", "simulation"]
    },
    "Set Matrix Zeroes": {
        "statement": "Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.",
        "difficulty": "Medium",
        "category": "Array, Matrix",
        "tags": ["array", "matrix", "in-place"]
    },
    "Game of Life": {
        "statement": "According to Wikipedia's article: 'The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.' The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).",
        "difficulty": "Medium",
        "category": "Array, Matrix",
        "tags": ["array", "matrix", "simulation"]
    },
    "Word Search": {
        "statement": "Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.",
        "difficulty": "Medium",
        "category": "Array, Backtracking",
        "tags": ["array", "backtracking", "dfs"]
    },
    "Number of Islands": {
        "statement": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.",
        "difficulty": "Medium",
        "category": "Array, Depth-First Search",
        "tags": ["array", "dfs", "flood-fill"]
    },
    "Surrounded Regions": {
        "statement": "Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.",
        "difficulty": "Medium",
        "category": "Array, Depth-First Search",
        "tags": ["array", "dfs", "boundary"]
    },
    
    # Advanced String Problems
    "Regular Expression Matching": {
        "statement": "Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where '.' matches any single character and '*' matches zero or more of the preceding element.",
        "difficulty": "Hard",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dp", "regex", "matching"]
    },
    "Wildcard Matching": {
        "statement": "Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where '?' matches any single character and '*' matches any sequence of characters (including the empty sequence).",
        "difficulty": "Hard",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dp", "wildcard", "matching"]
    },
    "Longest Valid Parentheses": {
        "statement": "Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.",
        "difficulty": "Hard",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dp", "parentheses", "stack"]
    },
    "Minimum Window Substring": {
        "statement": "Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ''.",
        "difficulty": "Hard",
        "category": "String, Sliding Window",
        "tags": ["string", "sliding-window", "hash-table"]
    },
    "Substring with Concatenation of All Words": {
        "statement": "You are given a string s and an array of strings words. All the strings of words are of the same length. A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.",
        "difficulty": "Hard",
        "category": "String, Hash Table",
        "tags": ["string", "hash-table", "sliding-window"]
    },
    "Text Justification": {
        "statement": "Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.",
        "difficulty": "Hard",
        "category": "String, Greedy",
        "tags": ["string", "greedy", "text-formatting"]
    },
    "Word Break": {
        "statement": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.",
        "difficulty": "Medium",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dp", "segmentation"]
    },
    "Word Break II": {
        "statement": "Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.",
        "difficulty": "Hard",
        "category": "String, Backtracking",
        "tags": ["string", "backtracking", "dp"]
    },
    "Palindrome Partitioning": {
        "statement": "Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.",
        "difficulty": "Medium",
        "category": "String, Backtracking",
        "tags": ["string", "backtracking", "palindrome"]
    },
    "Palindrome Partitioning II": {
        "statement": "Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.",
        "difficulty": "Hard",
        "category": "String, Dynamic Programming",
        "tags": ["string", "dp", "palindrome"]
    },
    
    # Advanced Dynamic Programming Problems
    "Longest Increasing Subsequence": {
        "statement": "Given an integer array nums, return the length of the longest strictly increasing subsequence. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Binary Search",
        "tags": ["dp", "binary-search", "subsequence"]
    },
    "Longest Common Subsequence": {
        "statement": "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "lcs"]
    },
    "Edit Distance": {
        "statement": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word: Insert a character, Delete a character, Replace a character.",
        "difficulty": "Hard",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "edit-distance"]
    },
    "Distinct Subsequences": {
        "statement": "Given two strings s and t, return the number of distinct subsequences of s which equals t. A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.",
        "difficulty": "Hard",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "subsequence"]
    },
    "Interleaving String": {
        "statement": "Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2. An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that: s = s1 + s2 + ... + sn, t = t1 + t2 + ... + tm, |n - m| <= 1, The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...",
        "difficulty": "Medium",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "interleaving"]
    },
    "Scramble String": {
        "statement": "We can scramble a string s to get a string t using the following algorithm: If the length of the string is 1, stop. If the length of the string is > 1, do the following: Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y. Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x. Apply step 1 recursively on each of the two substrings x and y. Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.",
        "difficulty": "Hard",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "scramble"]
    },
    "Decode Ways": {
        "statement": "A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> '1', 'B' -> '2', ..., 'Z' -> '26'. To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, '11106' can be mapped into: 'AAJF' with the grouping (1 1 10 6), 'KJF' with the grouping (11 10 6). Note that the grouping (1 11 06) is invalid because '06' cannot be mapped into 'F' since '6' is different from '06'. Given a string s containing only digits, return the number of ways to decode it.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, String",
        "tags": ["dp", "string", "decoding"]
    },
    "Unique Paths": {
        "statement": "There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Math",
        "tags": ["dp", "math", "combinatorics"]
    },
    "Unique Paths II": {
        "statement": "You are given an m x n integer array obstacleGrid. There is a robot initially located at the top-left corner (i.e., obstacleGrid[0][0]). The robot tries to move to the bottom-right corner (i.e., obstacleGrid[m - 1][n - 1]). The robot can only move either down or right at any point in time. An obstacle and space are marked as 1 or 0 respectively in obstacleGrid. A path that the robot takes cannot include any square that is an obstacle. Return the number of possible unique paths that the robot can take to reach the bottom-right corner.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Array",
        "tags": ["dp", "array", "obstacles"]
    },
    "Minimum Path Sum": {
        "statement": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. Note: You can only move either down or right at any point in time.",
        "difficulty": "Medium",
        "category": "Dynamic Programming, Array",
        "tags": ["dp", "array", "min-path"]
    },
    
    # Advanced Tree Problems
    "Binary Tree Maximum Path Sum": {
        "statement": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.",
        "difficulty": "Hard",
        "category": "Tree, Dynamic Programming",
        "tags": ["tree", "dp", "dfs", "path-sum"]
    },
    "Serialize and Deserialize Binary Tree": {
        "statement": "Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.",
        "difficulty": "Hard",
        "category": "Tree, Design",
        "tags": ["tree", "design", "serialization", "bfs"]
    },
    "Binary Tree Right Side View": {
        "statement": "Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
        "difficulty": "Medium",
        "category": "Tree, Breadth-First Search",
        "tags": ["tree", "bfs", "right-view"]
    },
    "Count Complete Tree Nodes": {
        "statement": "Given the root of a complete binary tree, return the number of the nodes in the tree. In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.",
        "difficulty": "Medium",
        "category": "Tree, Binary Search",
        "tags": ["tree", "binary-search", "complete-tree"]
    },
    "Path Sum III": {
        "statement": "Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum. The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).",
        "difficulty": "Medium",
        "category": "Tree, Hash Table",
        "tags": ["tree", "hash-table", "prefix-sum"]
    },
    
    # Advanced Graph Problems
    "Course Schedule": {
        "statement": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses. Otherwise, return false.",
        "difficulty": "Medium",
        "category": "Graph, Topological Sort",
        "tags": ["graph", "topological-sort", "dfs", "cycle-detection"]
    },
    "Course Schedule II": {
        "statement": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.",
        "difficulty": "Medium",
        "category": "Graph, Topological Sort",
        "tags": ["graph", "topological-sort", "bfs", "ordering"]
    },
    "Clone Graph": {
        "statement": "Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.",
        "difficulty": "Medium",
        "category": "Graph, Depth-First Search",
        "tags": ["tree", "dfs", "clone", "hash-table"]
    },
    "Pacific Atlantic Water Flow": {
        "statement": "There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.",
        "difficulty": "Medium",
        "category": "Graph, Depth-First Search",
        "tags": ["graph", "dfs", "ocean-flow", "multi-source"]
    },
    "Redundant Connection": {
        "statement": "In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph. Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.",
        "difficulty": "Medium",
        "category": "Graph, Union Find",
        "tags": ["graph", "union-find", "cycle-detection", "disjoint-set"]
    },
    
    # Advanced Backtracking Problems
    "N-Queens": {
        "statement": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.",
        "difficulty": "Hard",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "n-queens", "chess"]
    },
    "Sudoku Solver": {
        "statement": "Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules: Each of the digits 1-9 must occur exactly once in each row. Each of the digits 1-9 must occur exactly once in each column. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid. The '.' character indicates empty cells.",
        "difficulty": "Hard",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "sudoku", "constraint-satisfaction"]
    },
    "Word Search II": {
        "statement": "Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.",
        "difficulty": "Hard",
        "category": "Backtracking, Trie",
        "tags": ["backtracking", "trie", "dfs", "word-search"]
    },
    "Combination Sum": {
        "statement": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.",
        "difficulty": "Medium",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "combination", "sum"]
    },
    "Combination Sum II": {
        "statement": "Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination. Note: The solution set must not contain duplicate combinations.",
        "difficulty": "Medium",
        "category": "Backtracking, Array",
        "tags": ["backtracking", "array", "combination", "sum", "unique"]
    },
    
    # Advanced Heap Problems
    "Top K Frequent Elements": {
        "statement": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
        "difficulty": "Medium",
        "category": "Heap, Hash Table",
        "tags": ["dp", "hash-table", "frequency", "top-k"]
    },
    "Find Median from Data Stream": {
        "statement": "The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values. Implement the MedianFinder class: MedianFinder() initializes the MedianFinder object. void addNum(int num) adds the integer num from the data stream to the data structure. double findMedian() returns the median of all elements so far.",
        "difficulty": "Hard",
        "category": "Heap, Design",
        "tags": ["heap", "design", "median", "two-heaps"]
    },
    "Merge k Sorted Lists": {
        "statement": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
        "difficulty": "Hard",
        "category": "Heap, Linked List",
        "tags": ["heap", "linked-list", "merge", "priority-queue"]
    },
    "Kth Largest Element in an Array": {
        "statement": "Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.",
        "difficulty": "Medium",
        "category": "Heap, Array",
        "tags": ["heap", "array", "kth-largest", "quick-select"]
    },
    "Sliding Window Median": {
        "statement": "The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values. For example, for arr = [2,3,4], the median is 3. For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. Given an integer array nums and an integer k, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the median array for each window in the original array.",
        "difficulty": "Hard",
        "category": "Heap, Sliding Window",
        "tags": ["heap", "sliding-window", "median", "two-heaps"]
    },
    
    # Bit Manipulation Problems
    "Single Number": {
        "statement": "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.",
        "difficulty": "Easy",
        "category": "Array, Bit Manipulation",
        "tags": ["array", "bit-manipulation", "xor"]
    },
    "Single Number II": {
        "statement": "Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.",
        "difficulty": "Medium",
        "category": "Array, Bit Manipulation",
        "tags": ["array", "bit-manipulation", "counting"]
    },
    "Single Number III": {
        "statement": "Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order. You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.",
        "difficulty": "Medium",
        "category": "Array, Bit Manipulation",
        "tags": ["array", "bit-manipulation", "xor", "two-numbers"]
    },
    "Power of Two": {
        "statement": "Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.",
        "difficulty": "Easy",
        "category": "Math, Bit Manipulation",
        "tags": ["math", "bit-manipulation", "power"]
    },
    "Counting Bits": {
        "statement": "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.",
        "difficulty": "Easy",
        "category": "Dynamic Programming, Bit Manipulation",
        "tags": ["dp", "bit-manipulation", "counting"]
    },
    
    # Math Problems
    "Happy Number": {
        "statement": "Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy.",
        "difficulty": "Easy",
        "category": "Math, Hash Table",
        "tags": ["math", "hash-table", "cycle-detection"]
    },
    "Ugly Number": {
        "statement": "An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return true if n is an ugly number.",
        "difficulty": "Easy",
        "category": "Math",
        "tags": ["math", "prime-factors", "divisibility"]
    },
    "Ugly Number II": {
        "statement": "An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return the nth ugly number.",
        "difficulty": "Medium",
        "category": "Math, Dynamic Programming",
        "tags": ["math", "dp", "ugly-numbers", "pointers"]
    },
    "Super Ugly Number": {
        "statement": "A super ugly number is a positive integer whose prime factors are in the array primes. Given an integer n and an array of integers primes, return the nth super ugly number. The nth super ugly number is guaranteed to fit in a 32-bit signed integer.",
        "difficulty": "Medium",
        "category": "Math, Dynamic Programming",
        "tags": ["math", "dp", "ugly-numbers", "primes"]
    },
    "Perfect Squares": {
        "statement": "Given an integer n, return the least number of perfect square numbers that sum to n. A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.",
        "difficulty": "Medium",
        "category": "Math, Dynamic Programming",
        "tags": ["math", "dp", "perfect-squares", "lagrange"]
    },
    
    # Advanced Linked List Problems
    "Reverse Nodes in k-Group": {
        "statement": "Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.",
        "difficulty": "Hard",
        "category": "Linked List, Recursion",
        "tags": ["linked-list", "recursion", "reverse", "k-group"]
    },
    "Copy List with Random Pointer": {
        "statement": "A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null. Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointer values in the original list and copied list represent the same list state. None of the pointer values in the copied list should point to nodes in the original list.",
        "difficulty": "Medium",
        "category": "Linked List, Hash Table",
        "tags": ["linked-list", "hash-table", "copy", "random-pointer"]
    },
    "Reorder List": {
        "statement": "You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln. Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … You may not modify the values in the list's nodes. Only nodes themselves may be changed.",
        "difficulty": "Medium",
        "category": "Linked List, Two Pointers",
        "tags": ["linked-list", "two-pointers", "reorder", "middle"]
    },
    "Sort List": {
        "statement": "Given the head of a linked list, return the list after sorting it in ascending order.",
        "difficulty": "Medium",
        "category": "Linked List, Sorting",
        "tags": ["linked-list", "sorting", "merge-sort", "divide-conquer"]
    },
    "Insertion Sort List": {
        "statement": "Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head. The steps of the insertion sort algorithm: Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.",
        "difficulty": "Medium",
        "category": "Linked List, Sorting",
        "tags": ["linked-list", "sorting", "insertion-sort"]
    }
}

@app.route('/')
def index():
    return render_template('index.html', problems=DSA_PROBLEMS)

@app.route('/get_problem')
def get_problem():
    problem_name = request.args.get('name')
    if problem_name in DSA_PROBLEMS:
        return jsonify(DSA_PROBLEMS[problem_name])
    return jsonify({"error": "Problem not found"})

@app.route('/solve_problem', methods=['POST'])
def solve_problem():
    try:
        data = request.get_json()
        problem_name = data.get('problem_name')
        problem_statement = data.get('problem_statement')
        language = data.get('language')
        
        # Create a comprehensive prompt for the LLM
        prompt = f"""
        You are an expert DSA tutor. Please solve the following problem: "{problem_name}"

        Problem Statement: {problem_statement}

        Please provide your response in the following structured format:

        EXPLANATION:
        Provide a clear, step-by-step explanation of the optimal solution approach. Explain the logic, algorithm, and why this approach is optimal.

        CODE:
        Provide the complete code solution in {language} with proper comments and clear variable names.

        COMPLEXITY ANALYSIS:
        Analyze the time and space complexity of your solution. Explain why these complexities are achieved.

        DRY RUN EXAMPLES:
        Provide 2-3 concrete examples showing how the solution works step by step. Use actual input values and trace through the algorithm.

        ALTERNATIVE APPROACHES:
        If applicable, mention other approaches that could solve this problem and briefly explain their trade-offs.

        Format each section clearly and make your response educational and easy to understand for students learning DSA.
        """

        # Get response from Groq
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192",
            temperature=0.3,
            max_tokens=4000
        )

        response = chat_completion.choices[0].message.content
        
        return jsonify({
            "success": True,
            "solution": response,
            "language": language
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route('/search_problems')
def search_problems():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify(list(DSA_PROBLEMS.keys()))
    
    filtered_problems = [
        name for name in DSA_PROBLEMS.keys() 
        if query in name.lower() or query in DSA_PROBLEMS[name]['category'].lower()
    ]
    return jsonify(filtered_problems)

@app.route('/get_problem_categories')
def get_problem_categories():
    # Return the full DSA_PROBLEMS dictionary with all problem details
    return jsonify(DSA_PROBLEMS)

@app.route('/get_problems_by_difficulty')
def get_problems_by_difficulty():
    difficulty = request.args.get('difficulty', 'all')
    if difficulty == 'all':
        return jsonify(DSA_PROBLEMS)
    
    filtered_problems = {
        name: details for name, details in DSA_PROBLEMS.items() 
        if details['difficulty'] == difficulty
    }
    return jsonify(filtered_problems)

@app.route('/get_problems_by_category')
def get_problems_by_category():
    category = request.args.get('category', 'all')
    if category == 'all':
        return jsonify(DSA_PROBLEMS)
    
    filtered_problems = {
        name: details for name, details in DSA_PROBLEMS.items() 
        if category.lower() in details['category'].lower()
    }
    return jsonify(filtered_problems)

@app.route('/get_available_categories')
def get_available_categories():
    categories = set()
    for details in DSA_PROBLEMS.values():
        categories.add(details['category'])
    return jsonify(list(categories))

@app.route('/get_available_difficulties')
def get_available_difficulties():
    difficulties = set()
    for details in DSA_PROBLEMS.values():
        difficulties.add(details['difficulty'])
    return jsonify(list(difficulties))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
