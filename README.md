# 🧠 DSA in Python — Data Structures & Algorithms

A comprehensive collection of **Data Structures and Algorithms** problems and implementations in **Python**, organized by topic. This repository covers everything from fundamental bit manipulation to advanced recursion, backtracking, greedy algorithms, and tree traversals — with 50+ LeetCode & GeeksforGeeks solutions.

---

## 📁 Repository Structure

```
DSA_PYTHON/
├── XOR/                              # Bit Manipulation (Classes 71–74)
├── ADVANCE RECURSION/                # Advanced Recursion & Backtracking (Classes 75–87)
├── Stacks AND Queues(C88_C)/         # Stacks, Queues, Sliding Window & Greedy (Days 88–111)
├── PRIFIX_INFIX_POSTFIX_conversions/ # Expression Conversions (Day 96)
├── SINGLY_LINKED_LIST/               # Singly Linked List Operations
├── Doubly_Linked_List/               # Doubly Linked List Operations
├── Tree/                             # Binary Tree Problems
├── DSA_LAB/                          # University Lab Programs (11 experiments)
├── LC/                               # 50+ LeetCode Solutions
├── GG/                               # GeeksforGeeks Practice Problems
└── Practice_problems/                # Miscellaneous Practice
```

---

## 📚 Topics Covered

### 1. 🔢 Bit Manipulation / XOR (`XOR/`)

Bit manipulation uses bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) to perform operations at the binary level for optimal performance.

| Class | File | Topic | Logic |
|-------|------|-------|-------|
| 71 | `check_iTH_bit.py` | **Check if i-th bit is set** | Uses `n & (1 << i)` — left-shifts 1 to the i-th position and ANDs with n. Non-zero result means the bit is set. |
| 71 | `set_ith_bit.py` | **Set the i-th bit** | Uses `n \| (1 << i)` — forces the i-th bit to 1 regardless of its current value. |
| 71 | `clear_ith_bit.py` | **Clear the i-th bit** | Uses `n & ~(1 << i)` — creates a mask with all bits set except the i-th, then ANDs. |
| 71 | `toggle.py` | **Toggle i-th bit** | Uses `n ^ (1 << i)` — XOR flips the bit: 0→1 or 1→0. |
| 71 | `swap_XOR.py` | **Swap two numbers without temp** | Three XOR operations: `a ^= b; b ^= a; a ^= b`. Works because XOR is self-inverse. |
| 71 | `remove_last_set_bit.py` | **Remove last set bit** | Uses `n & (n - 1)` — subtracting 1 flips all bits from the rightmost set bit onward. |
| 72 | `count.py` | **Count bit flips to convert A to B** | XOR both numbers (differing bits become 1), then count set bits in the result. |
| 73 | `find_single(optimal).py` | **Find single element** | XOR all elements — duplicates cancel out (`a ^ a = 0`), leaving the unique element. **O(n) time, O(1) space.** |
| 73 | `find_single(bruit_solution).py` | **Find single (brute force)** | Nested loop comparison. **O(n²) time.** |
| 74 | `power_set.PY` | **Generate all subsets (Power Set)** | Iterates from 0 to 2ⁿ−1. Each number's binary representation determines which elements to include. |
| 74 | `2^n_find.py` | **Check power of 2** | Uses `n & (n - 1) == 0` — powers of 2 have exactly one set bit. |

---

### 2. 🔄 Advanced Recursion & Backtracking (`ADVANCE RECURSION/`)

Recursion solves problems by breaking them into smaller subproblems. Backtracking extends this by exploring all possibilities and "undoing" choices that don't lead to a solution.

| Class | File | Topic | Logic |
|-------|------|-------|-------|
| 75 | `find_subSequence.py` | **Generate all subsequences** | At each index, two choices: include or exclude the element. Recursively builds all 2ⁿ subsets. |
| 76 | `subsequence_sum_K.py` | **Subsequences with sum K** | Same include/exclude pattern, but prunes branches when the running sum exceeds K. |
| 77 | `check.py` / `without.py` | **Check if subsequence with sum K exists** | Returns `True` on first valid subsequence found, short-circuiting further exploration. |
| 78 | `find_no_of_sum_k.py` | **Count subsequences with sum K** | Counts (instead of collecting) all subsequences whose sum equals K. |
| 79 | `find_howMany.py` | **Count combinations** | Counts valid combinations using recursion with a running total. |
| 80 | `generateParenthesis.py` | **Generate Parentheses (LC #22)** | Backtracking with two counters: add `(` if `left < n`, add `)` if `right < left`. Ensures every combination is valid. |
| 81 | `combinationSum.py` | **Combination Sum (LC #39)** | At each index: either pick the element again (stay at same index) or move to the next. Allows unlimited reuse of candidates. |
| 82 | `combineSUM.py` | **Combination Sum II (LC #40)** | Similar to above but each element used at most once. Skips duplicates by checking `candidates[i] == candidates[i-1]`. |
| 83 | `subsetSum.py` | **Subset Sum** | Generates all subsets and computes their sums using include/exclude recursion. |
| 84 | `combinationSum3.py` | **Combination Sum III (LC #216)** | Find k numbers (1–9) that sum to n. Backtracking with constraints on count and range. |
| 85 | `seatch_word.py` | **Letter Combinations of Phone (LC #17)** | Maps digits to letters, then recursively builds all letter combinations via backtracking. |
| 86 | `bruitsol.py` / `optimalsol.py` | **N-Queens Problem** | Places queens column by column. Checks row, upper-diagonal, and lower-diagonal for conflicts. Brute: O(n!×n), Optimal: O(n!) using hash arrays. |
| 87 | `demo.py` / `new.py` | **Rat in a Maze** | Explores all 4 directions (D, L, R, U) from `(0,0)` to `(n-1,n-1)`. Uses a visited matrix to avoid cycles. Records the path string. |

---

### 3. 📦 Stacks & Queues (`Stacks AND Queues(C88_C)/`)

**Stack** = LIFO (Last In, First Out). **Queue** = FIFO (First In, First Out). These are fundamental data structures used in expression evaluation, BFS/DFS, and many algorithmic problems.

| Day | File | Topic | Logic |
|-----|------|-------|-------|
| 88 | `implementStack.py` | **Stack using list** | Uses Python list with `append()` for push, `pop()` for pop, `[-1]` for peek. |
| 88 | `code.py` | **Stack class (OOP)** | Full class with `push`, `pop`, `top`, `size`, `is_empty` methods and error handling. |
| 89 | `implementationOFqueues.py` | **Queue class (OOP)** | Uses list with `append()` for enqueue, `pop(0)` for dequeue, plus `front`, `rear`, `size` methods. |
| 90 | `understandingDEQUE.py` | **Deque** | Demonstrates Python's `collections.deque` for double-ended operations. |
| 91 | `code.py` | **Stack using Deque** | After each push, rotates all existing elements to maintain LIFO order using a single queue. |
| 92 | `stackQueue.py` | **Stack using Queue** | Implements stack behavior using queue operations. |
| 93 | `stack_usingDLL.py` | **Stack using Doubly Linked List** | Each push adds a node at the top; pop removes from top. Achieves O(1) for all operations. |
| 93 | `queue_usingDLL.py` | **Queue using Doubly Linked List** | Enqueue at tail, dequeue from head. O(1) for both operations using DLL pointers. |
| 94 | `LC_20_validPaarentheses.py` | **Valid Parentheses (LC #20)** | Push opening brackets onto stack; for closing brackets, check if top matches. Valid if stack is empty at the end. |
| 95 | `LC_155_minStack.py` | **Min Stack (LC #155)** | Maintains two stacks — one for values, one tracking the current minimum. O(1) `getMin()`. |
| 97 | `next_greaterElement.py` | **Next Greater Element** | Traverses array right-to-left using a stack. Pops elements smaller than current; top of stack is the answer. **O(n).** |
| 98 | `next_max_element.py` | **Next Greater Element II** | Same logic but handles circular arrays by iterating `2n` times using modular indexing. |
| 99 | `asteroid.py` | **Asteroid Collision (LC #735)** | Stack-based simulation: positive asteroids are pushed; negative ones pop smaller positive asteroids. **O(2n) time.** |

#### Sliding Window Problems (Days 100–103)

| Day | File | Topic | Logic |
|-----|------|-------|-------|
| 100 | `longest_substring.py` | **Longest Substring Without Repeating Chars (LC #3)** | Two-pointer sliding window with a hash set. Expand right pointer; shrink left pointer when duplicate found. |
| 101 | `OPTIMALmax_consicutiveONES.py` | **Max Consecutive Ones III (LC #1004)** | Sliding window tracking zero count. Shrink window from left when zeros exceed k. |
| 102 | `optimal_totalFruit.py` | **Fruits into Baskets (LC #904)** | Sliding window with at most 2 distinct fruit types using a hash map. Shrink when types exceed 2. |
| 103 | `optimalSOL.py` | **Longest Repeating Character Replacement (LC #424)** | Sliding window tracking character frequencies. Window is valid when `window_size - max_freq ≤ k`. |

#### Greedy Algorithm Problems (Days 104–111)

| Day | File | Topic | Logic |
|-----|------|-------|-------|
| 104 | `assigncookies.py` | **Assign Cookies (LC #455)** | Sort both greed factors and cookie sizes. Greedily assign smallest sufficient cookie to each child. **O(n log n).** |
| 105 | `factorialKnapsack.py` | **Fractional Knapsack** | Sort items by value/weight ratio (descending). Greedily take whole items, then a fraction of the last. |
| 106 | `greddyOptimal.py` | **Greedy Optimization** | Greedy approach for optimization problems. |
| 107 | `LC860.py` | **Lemonade Change (LC #860)** | Track $5 and $10 bills. For $10 change: use one $5. For $20 change: prefer $10+$5, else three $5s. |
| 108 | `meetingINaRoom.py` | **N Meetings in One Room** | Sort meetings by end time. Greedily select next meeting that starts after the previous one ends. **O(n log n).** |
| 109 | `jump.py` | **Jump Game (LC #55)** | Track maximum reachable index. If current index exceeds `max_reachable`, return False. |
| 110 | `jump2.py` | **Jump Game II (LC #45)** | BFS-like approach: track current window `[left, right]`, find farthest reachable, count jumps. **O(n).** |
| 111 | `platform.py` / `optimal.py` | **Minimum Platforms** | Sort arrival and departure. Use two pointers to count overlapping trains. |

---

### 4. 🔀 Prefix, Infix & Postfix Conversions (`PRIFIX_INFIX_POSTFIX_conversions/`)

Expression notations differ in operator placement. Converting between them uses stacks and operator precedence rules.

| File | Conversion | Logic |
|------|-----------|-------|
| `InfixTOpostfix.py` | **Infix → Postfix** | Scan left-to-right. Operands go to output. Operators are pushed to stack (popping higher/equal precedence operators first). Parentheses handled by pushing `(` and popping until `)`. **O(n) time.** |
| `infixTOprefix.py` | **Infix → Prefix** | Reverse the expression, swap `(` and `)`, apply infix-to-postfix, then reverse the result. The only change: use strict `<` instead of `<=` for precedence comparison. **O(n) time.** |
| `postfixTOinfix.py` | **Postfix → Infix** | Use a stack. Push operands; on operator, pop two operands, combine as `(operand1 op operand2)`, push back. |
| `prefixTOinfix.py` | **Prefix → Infix** | Traverse right-to-left. Same stack logic as postfix→infix but reversed direction. |
| `postfisTOprefix.py` | **Postfix → Prefix** | Stack-based. On operator, pop two, combine as `op + operand1 + operand2`, push result. |
| `prefixTOpostfix.py` | **Prefix → Postfix** | Traverse right-to-left. On operator, pop two, combine as `operand1 + operand2 + op`, push result. |

---

### 5. 🔗 Singly Linked List (`SINGLY_LINKED_LIST/`)

A singly linked list is a linear data structure where each node contains data and a pointer to the next node. Traversal is one-directional.

| File | Operation | Logic |
|------|-----------|-------|
| `delete.py` | **Delete a node by value** | Traverse to find the node. Update the previous node's `next` pointer to skip the target node. Handles head deletion separately. |
| `swap_pair.py` | **Swap nodes in pairs (LC #24)** | Uses a dummy node and two pointers (`slow`, `fast`). Swaps adjacent pairs by relinking pointers. |
| `reverse.py` | **Reverse a linked list** | Iteratively reverse `next` pointers using three variables: `prev`, `curr`, `next`. **O(n) time, O(1) space.** |

---

### 6. 🔗🔗 Doubly Linked List (`Doubly_Linked_List/`)

A doubly linked list has nodes with both `next` and `prev` pointers, enabling bidirectional traversal.

| File | Operation | Logic |
|------|-----------|-------|
| `creat.py` | **Create a DLL** | Define `Node` class with `val`, `next`, `prev`. Manually link nodes in both directions. |
| `traverse.py` | **Traverse a DLL** | Start from head, follow `next` pointers until `None`, printing each node's value. |
| `insertFirst.py` | **Insert at beginning** | Create new node, set its `next` to current head, update head's `prev` to new node, make new node the head. **O(1).** |
| `insertKth.py` | **Insert at k-th position** | Traverse to position `k-1`, relink `next` and `prev` pointers around the new node. **O(n).** |
| `appendLast.py` | **Append at end** | Traverse to the last node, set its `next` to new node, set new node's `prev` to last node. **O(n) time, O(1) space.** |

---

### 7. 🌳 Binary Tree (`Tree/`)

A binary tree is a hierarchical data structure where each node has at most two children (left, right). Most tree problems are solved using DFS (recursion) or BFS (level-order with queue).

| File | Problem | Logic |
|------|---------|-------|
| `104. Maximum Depth of Binary Tree.py` | **Max Depth (LC #104)** | Recursively compute `1 + max(left_height, right_height)`. Base case: `None` returns 0. **O(n).** |
| `543. Diameter of Binary Tree.py` | **Diameter (LC #543)** | At each node, diameter = `left_height + right_height`. Track the global maximum using `nonlocal`. Return `1 + max(left, right)` for height. |
| `LC110_BalancedBinaryTree.py` | **Balanced Tree (LC #110)** | Compute height recursively. Return `-1` if any subtree is unbalanced (height difference > 1). Single-pass O(n). |
| `124. Binary Tree Maximum Path Sum.py` | **Max Path Sum (LC #124)** | At each node, compute `max(left, 0) + max(right, 0) + node.val`. Track global max with `nonlocal`. Return `node.val + max(left, right)` upward. |
| `199. Binary Tree Right Side View.py` | **Right Side View (LC #199)** | DFS traversal visiting right child first. Add node to result when `len(result) == level` (first node seen at each depth). |
| `GG_Top View of Binary Tree.py` | **Top View (GFG)** | BFS with horizontal distance (`line`). Store only the **first** node seen at each horizontal distance in a hash map. |
| `GG_Bottom View of Binary Tree.py` | **Bottom View (GFG)** | BFS with horizontal distance. **Overwrite** the hash map at each horizontal distance — the last node at each distance is the bottom view. |

---

### 8. 🧪 DSA Lab Programs (`DSA_LAB/`)

University lab experiments covering core algorithm design paradigms.

| # | File | Topic | Paradigm | Logic |
|---|------|-------|----------|-------|
| 1 | `1.py` | **Binary Search** | Divide & Conquer | Recursively halve the search space. Compare target with mid element: go left if smaller, right if larger. **O(log n).** |
| 2 | `2.py` | **Quick Sort** | Divide & Conquer | Choose pivot (last element), partition array so elements < pivot go left. Recursively sort both halves. **Avg O(n log n), Worst O(n²).** |
| 3 | `3.py` | **Infix → Postfix** | Stack | Operator precedence-based conversion using a stack. Handles `+`, `-`, `*`, `/`, `^`, and parentheses. |
| 4 | `4.py` | **BFS Traversal** | Branch & Bound | Uses a queue (`deque`) to visit nodes level-by-level. Marks visited nodes to avoid revisiting. **O(V + E).** |
| 5 | `5.py` | **N-Queens (DFS)** | Backtracking | Column-by-column placement with row, upper-diagonal, and lower-diagonal safety checks. |
| 6 | `6.py` | **TSP (Greedy)** | Greedy | From current city, always travel to the nearest unvisited city. Returns path and total cost. |
| 7 | `7.py` | **Fractional Knapsack** | Greedy | Sort by value/weight ratio. Take whole items until capacity is full, then take a fraction of the next. **O(n log n).** |
| 8 | `8.py` | **0/1 Knapsack** | Dynamic Programming | Build a 2D DP table `dp[i][w]`. For each item, decide: take it (if weight allows) or skip it. **O(n × W).** |
| 9 | `9.py` | **Matrix Chain Multiplication** | Dynamic Programming | Find optimal parenthesization to minimize scalar multiplications. Uses interval DP: try all split points. **O(n³).** |
| 10 | `10_nQueen.py` | **N-Queens (Optimized)** | Backtracking | Uses hash arrays for O(1) conflict checking: `leftrow[]`, `upperDiagonal[]`, `lowerDiagonal[]`. |
| 11 | `11.py` | **Hashing (Linear Probing)** | Hashing | Hash function: `key % size`. On collision, probe next slot `(index + 1) % size` until an empty slot is found. |
| — | `stackquestion.py` | **Two Stacks** | Stack | Implements two independent stacks using two separate lists with push/pop for each. |
| — | `que_useing_stack.py` | **Queue using List** | Queue | Simple queue with `append` for enqueue and `pop(0)` for dequeue. |

---

### 9. 💻 LeetCode Solutions (`LC/`)

50+ LeetCode problems solved in Python, covering arrays, binary search, math, strings, linked lists, and more.

| Problem | File | Category | Approach |
|---------|------|----------|----------|
| LC #14 | `lc14.py` | String | Longest Common Prefix |
| LC #26 | `LC_26_` | Array | Remove Duplicates from Sorted Array |
| LC #27 | `LC_27_remove element.py` | Array | Remove Element (Two Pointers) |
| LC #33 | `LC_33.py` | Binary Search | Search in Rotated Sorted Array |
| LC #34 | `LC34.py` | Binary Search | Find First & Last Position |
| LC #46 | `lc_46.py` | Backtracking | Permutations |
| LC #49 | `lc49.py` | Hash Map | Group Anagrams |
| LC #67 | `lc67.py` | Math | Add Binary |
| LC #69 | `LC_69_sqrt.py` | Binary Search | Sqrt(x) |
| LC #73 | `LC_73.py` | Matrix | Set Matrix Zeroes |
| LC #74 | `#lc_74.py` | Binary Search | Search a 2D Matrix |
| LC #80 | `lc80.py` | Array | Remove Duplicates II |
| LC #83 | `LC_83.py` | Linked List | Remove Duplicates from Sorted List |
| LC #108 | `LC_108.py` | Tree/BST | Convert Sorted Array to BST |
| LC #120 | `LC_120.py` | DP | Triangle Minimum Path Sum |
| LC #128 | `lc128.py` | Hash Set | Longest Consecutive Sequence |
| LC #130 | `lc130.py` | DFS/BFS | Surrounded Regions |
| LC #137 | `lc137.py` | Bit Manipulation | Single Number II |
| LC #151 | `lc151.py` | String | Reverse Words in a String |
| LC #152 | `lc152.py` | DP | Maximum Product Subarray |
| LC #167 | `lc167.py` | Two Pointers | Two Sum II - Sorted Array |
| LC #169 | `lc169.py` | Boyer-Moore | Majority Element |
| LC #202 | `LC_202.py` | Math | Happy Number |
| LC #203 | `LC_203_removeElement.py` | Linked List | Remove Linked List Elements |
| LC #204 | `lc204.py` | Math | Count Primes (Sieve of Eratosthenes) |
| LC #238 | `lc238.py` | Array | Product of Array Except Self |
| LC #260 | `lc260.py` | Bit Manipulation | Single Number III |
| LC #274 | `#274lc.py` | Sorting | H-Index |
| LC #326 | `LC_326.py` | Math | Power of Three |
| LC #371 | `lc371.py` | Bit Manipulation | Sum of Two Integers |
| LC #390 | `lc390.py` | Math | Elimination Game |
| LC #396 | `lc396.py` | Math | Rotate Function |
| LC #414 | `LC414.PY` | Array | Third Maximum Number |
| LC #496 | `lc496.py` | Stack | Next Greater Element I |
| LC #537 | `lc537.py` | String/Math | Complex Number Multiplication |
| LC #560 | `#DUE_lc560.py` | Prefix Sum | Subarray Sum Equals K |
| LC #593 | `lc593.py` | Math/Geometry | Valid Square |
| LC #633 | `lc633.py` | Two Pointers | Sum of Square Numbers |
| LC #692 | `lc692.py` | Heap | Top K Frequent Words |
| LC #832 | `lc832.py` | Matrix | Flipping an Image |
| LC #941 | `lc941.py` | Array | Valid Mountain Array |
| LC #1089 | `lc1089.py` | Array | Duplicate Zeros |
| LC #1262 | `lc1262.py` | Greedy | Greatest Sum Divisible by Three |
| LC #1909 | `lc1909.py` | Array | Remove One Element to Make Strictly Increasing |
| LC #2248 | `lc2248.py` | Hash Map | Intersection of Multiple Arrays |
| LC #2520 | `lc2520.py` | Math | Count Digits That Divide a Number |
| LC #2652 | `lc2652.py` | Math | Sum Multiples |

---

### 10. 🟢 GeeksforGeeks Problems (`GG/`)

| File | Problem | Logic |
|------|---------|-------|
| `gg.py` | **Max Subarray XOR of size K** | Sliding window XOR: XOR out the leftmost element and XOR in the new element. **O(n).** |
| `2nd.py` | **Count Distinct Elements in Every Window** | Sliding window with a hash map to count distinct elements per window of size k. |
| `stack.py` | **Two Stacks** | Two independent stacks with separate push/pop operations. |
| `3rd.py` | **Count Subarrays with K Odd Numbers** | Subarray counting problem (template). |

---

## 🧩 Key Algorithm Paradigms

| Paradigm | Description | Examples in Repo |
|----------|-------------|------------------|
| **Divide & Conquer** | Split problem into subproblems, solve recursively, combine results | Binary Search, Quick Sort |
| **Greedy** | Make locally optimal choices at each step | Fractional Knapsack, Assign Cookies, Jump Game, Meeting Rooms |
| **Dynamic Programming** | Store results of overlapping subproblems to avoid recomputation | 0/1 Knapsack, MCM, Triangle Path Sum, Max Product Subarray |
| **Backtracking** | Explore all solutions, undo invalid choices | N-Queens, Rat in a Maze, Combination Sum, Generate Parentheses |
| **Sliding Window** | Maintain a window of elements and slide it across the array | Longest Substring, Max Consecutive Ones, Fruits into Baskets |
| **Two Pointers** | Use two pointers to traverse data from different ends | Two Sum II, Remove Duplicates, Sum of Squares |
| **Bit Manipulation** | Use bitwise operators for efficient computation | XOR Swap, Power Set, Single Number, Bit Counting |

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/roylaxmikanta/DSA-In-Python.git
cd DSA-In-Python

# Run any Python file
python <folder>/<filename>.py

# Examples
python DSA_LAB/1.py             # Binary Search
python "ADVANCE RECURSION/CLASS_80/generateParenthesis.py"  # Generate Parentheses
python LC/lc49.py               # Group Anagrams
```

> **Requirements:** Python 3.x (no external libraries needed for most files)

---

## 📊 Complexity Reference

| Algorithm | Time | Space |
|-----------|------|-------|
| Binary Search | O(log n) | O(log n) recursive / O(1) iterative |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) |
| BFS / DFS | O(V + E) | O(V) |
| 0/1 Knapsack (DP) | O(n × W) | O(n × W) |
| Matrix Chain Multiplication | O(n³) | O(n²) |
| N-Queens (Backtracking) | O(n!) | O(n²) |
| Infix → Postfix/Prefix | O(n) | O(n) |
| Sliding Window | O(n) | O(k) |

---

## 👤 Author

**Roy Laxmi Kanta**

---

## 📝 License

This project is for educational purposes. Feel free to use and learn from these implementations.

---

> ⭐ **If you find this helpful, give it a star!**
