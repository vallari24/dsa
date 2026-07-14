# See the Problem, Name the Pattern

*A field guide for recognizing DSA patterns in interviews — glance at this before you walk in.*

---

## The one idea that changes everything

An interview problem is **never new**. It's one of ~15 shapes wearing a costume.
Your job in the first 3 minutes isn't to solve it — it's to **undress it**.

```
  what they say                 what it actually is
  ─────────────────────         ───────────────────
  "elevation map, rain"    →    per-index needs max from both sides
  "best time to buy"       →    best ordered pair (i before j)
  "top k frequent"         →    count, then select
  "course prerequisites"   →    topological sort
```

Don't ask *"how do I solve this?"* Ask *"which shape is this?"*

---

## The 3-Question Script (run this on EVERY array/string problem)

> **Q1. Can I restate the answer as a formula?**
> max/min/count/sum … over what, exactly? Say it out loud. This alone impresses interviewers.
>
> **Q2. Can I decompose it per index?**
> "What is the answer *at position i* alone?"
>
> **Q3. What does position i need to know?**

```
  what index i needs              →  pattern
  ────────────────────────────────────────────────────────────
  nothing beyond itself           →  one pass
  something from its LEFT only    →  one pass + running variable
  something from BOTH sides       →  prefix/suffix arrays
                                     (then: can two pointers replace them?)
  nearest BIGGER/SMALLER element  →  monotonic stack
  best over a contiguous window   →  sliding window
  "have I seen this before?"      →  hash map
```

Q3 is where the pattern names itself.

---

## Read the constraints FIRST — they whisper the intended complexity

```
   n ≤ 20        →  O(2ⁿ) is fine     →  backtracking, bitmask
   n ≤ 1,000     →  O(n²) is fine     →  2D DP, nested loops
   n ≤ 100,000   →  need O(n log n)   →  sort, heap, binary search
   n ≤ 10⁶       →  need O(n)         →  hashmap, sliding window,
                                          prefix sum, monotonic stack
   n ≥ 10⁹       →  need O(log n)     →  binary search
   "O(1) space"  →  two pointers, running vars, bit tricks
```

---

## The Master Cue Table

| You see / hear | Think | Core move |
|---|---|---|
| "Have I seen this before?", counts, duplicates, complements | **Hash map/set** | Remember useful past info |
| Sorted array, pair search, palindrome, both ends | **Two pointers** | Shrink/search from both sides |
| Contiguous subarray/substring + condition | **Sliding window** | Expand right, shrink left |
| Subarray sums, "sum between i and j" | **Prefix sum** | Store cumulative history |
| Matching pairs, nesting, undo-like behavior | **Stack** | Last unresolved thing |
| Next greater/smaller, temperatures, histogram | **Monotonic stack** | Keep candidates sorted in stack |
| Top K, repeatedly need min/max, streaming | **Heap** | Keep best K available |
| Sorted input, OR monotonic yes/no condition | **Binary search** | Find the boundary |
| Trees, graphs, islands, levels, paths | **DFS / BFS** | Explore connected choices |
| Generate ALL combinations/permutations | **Backtracking** | Try, recurse, undo |
| Count ways, best over sequential choices | **DP** | Cache answers to subproblems |
| Meeting rooms, merge ranges, overlaps | **Intervals** | Sort by start, then sweep |
| Connected components, grouping, cycle in undirected | **Union-Find** | Merge sets efficiently |
| Prefix search, dictionary of words | **Trie** | Tree of characters |
| Prerequisites, dependency order | **Topological sort** | Peel nodes with no deps |
| Linked list cycle/middle | **Fast & slow pointers** | Hare catches tortoise |
| "Appears twice except one", no extra space | **Bit / XOR** | Pairs cancel out |

---

# The Patterns — one visual each

---

## 1. Hash Map — *"Have I seen this before?"*

**Cue words:** duplicate, complement, count, frequency, group, pair exists?

```
  Two Sum, target = 9        seen = {}
  [2, 7, 11, 15]
   ↑
   need 9-2=7 … not seen, remember 2
      ↑
      need 9-7=2 … SEEN IT ✓
```

**The thought:** *"I keep re-searching for something → remember it instead."*
Every time your brute force re-scans the array for a value, a hashmap kills the inner loop.

```python
seen = {}
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target-x], i]
    seen[x] = i
```

**Drill:** Two Sum · Contains Duplicate · Valid Anagram · Group Anagrams · Longest Consecutive Sequence

---

## 2. Two Pointers — *sorted, or attack from both ends*

**Cue words:** sorted, pair/triplet summing to target, palindrome, container, "in place"

```
  sorted:  [1, 3, 5, 8, 11, 14]      sum too small → L++
            L→              ←R       sum too big   → R--
```

**The thought:** *"Sorted means moving a pointer changes the sum in a KNOWN direction — so I never need to look back."*

```python
l, r = 0, len(a)-1
while l < r:
    if a[l] + a[r] == target: return ...
    elif a[l] + a[r] < target: l += 1
    else: r -= 1
```

**Drill:** Two Sum II · 3Sum · Container With Most Water · Valid Palindrome · Trapping Rain Water (optimized)

---

## 3. Sliding Window — *best CONTIGUOUS chunk*

**Cue words:** longest/shortest **substring/subarray**, "at most K", "window", consecutive

```
  "longest substring without repeats"
  a b c a b b
  [a b c]a b b      expand right while valid
  a[b c a]b b       hit repeat → shrink left
  ────────────
  window slides, never restarts  →  O(n)
```

**The thought:** *"Answer is a contiguous run + the condition only gets worse as I add → slide, don't restart."*

```python
l = 0
for r in range(n):
    add(a[r])                    # expand
    while invalid(): remove(a[l]); l += 1   # shrink
    best = max(best, r - l + 1)
```

⚠ **Trap:** if negatives can *fix* a broken window (e.g. subarray sum with negatives) → sliding window fails → use **prefix sum + hashmap**.

**Drill:** Best Time to Buy & Sell Stock · Longest Substring Without Repeating · Longest Repeating Character Replacement · Minimum Window Substring · Sliding Window Maximum

---

## 4. Prefix / Suffix Precompute — *each index needs its neighborhood's history*

**Cue words:** range sum, "product except self", "max to the left/right of i", between i and j

```
  nums:     [ 2,  4,  1,  3 ]
  prefix:   [ 2,  6,  7, 10 ]     sum(i..j) = prefix[j] - prefix[i-1]

  needs BOTH sides?  build two arrays:
  leftmax →  [ 2,  4,  4,  4 ]
  rightmax → [ 4,  4,  3,  3 ] ←
```

**The thought:** *"Every index asks the same question about everything before/after it → answer them all in one pre-pass."*

**Drill:** Products of Array Except Self · Subarray Sum Equals K · Range Sum Query · Trapping Rain Water (v1)

---

## 5. Stack — *the last unresolved thing*

**Cue words:** valid parentheses, nested, matching, undo, evaluate expression

```
  "( [ ) ]"        push ( → push [ → see ) …
                   top is [ ≠ (   →  INVALID
```

**The thought:** *"New things must resolve against the MOST RECENT open thing → LIFO."*

**Drill:** Valid Parentheses · Min Stack · Evaluate RPN · Generate Parentheses

---

## 6. Monotonic Stack — *nearest greater/smaller*

**Cue words:** next greater element, "how many days until warmer", histogram, stock span

```
  temps: [73, 74, 75, 71, 69, 72]
  stack keeps a DECREASING staircase of "still waiting" days:

  push 73 → 74 pops it (warmer!) → push 74 → 75 pops it …
  71, 69 pile up   [75, 71, 69]
  72 arrives → pops 69 ✓, pops 71 ✓, can't pop 75 → push
```

**The thought:** *"Each element pops everyone it 'answers', then waits its turn. Everyone pushed & popped once → O(n)."*

```python
stack = []                       # indices, values decreasing
for i, x in enumerate(a):
    while stack and a[stack[-1]] < x:
        j = stack.pop(); ans[j] = i - j
    stack.append(i)
```

**Drill:** Daily Temperatures · Next Greater Element · Largest Rectangle in Histogram · Car Fleet

---

## 7. Heap — *repeatedly need the best; Top K*

**Cue words:** top K, Kth largest, K closest, merge K lists, median of stream, scheduler

```
  keep a MIN-heap of size K  →  its root = Kth largest so far
        [ 5 ]
       /     \        anything bigger than root? push, pop root.
     [ 8 ]  [ 7 ]     heap always holds "the K best seen"
```

**The thought:** *"I don't need everything sorted — I only need the best K, maintained cheaply."*

**Tie-breaker:** one-shot & average-case OK → quickselect. Values in a small range → **bucket sort** (the O(n) trick in Top K Frequent).

**Drill:** Top K Frequent Elements · Kth Largest Element · K Closest Points · Merge K Sorted Lists · Find Median from Data Stream (two heaps)

---

## 8. Binary Search — *find the boundary of a monotonic condition*

**Cue words:** sorted, O(log n), rotated, "minimum X such that it works", minimize the maximum

```
  classic:                     on the ANSWER (Koko):
  [1,3,5,7,9,11]  find 7       speed:  1 2 3 4 5 6 7 8
        ↑ halve, halve          works?  ✗ ✗ ✗ ✓ ✓ ✓ ✓ ✓
                                              ↑ find this boundary
```

**The thought:** *"Is there a yes/no question that flips exactly once as X grows? Then binary search X — even if nothing is 'sorted'."*

```python
lo, hi = min_ans, max_ans
while lo < hi:
    mid = (lo + hi) // 2
    if works(mid): hi = mid
    else: lo = mid + 1
```

**Drill:** Binary Search · Search Rotated Array · Find Min in Rotated Array · Koko Eating Bananas · Median of Two Sorted Arrays

---

## 9. Fast & Slow Pointers — *linked lists, cycles, middles*

**Cue words:** cycle, middle of list, "happy number", repeating sequence

```
  slow →  1 → 2 → 3 → 4 → 5 ─┐
  fast ⇒⇒            ↑ ← ← ← ┘   if they meet: cycle
```

**Drill:** Linked List Cycle · Middle of Linked List · Find the Duplicate Number · Reorder List

---

## 10. Intervals — *sort by start, then sweep*

**Cue words:** meeting rooms, merge ranges, overlapping, schedule

```
  sort by start:   [1───4]
                       [3────6]      3 ≤ 4 → OVERLAP → merge to [1,6]
                              [8──10]  8 > 6 → new interval
```

**The thought:** *"After sorting by start, overlap is just: next.start ≤ current.end."*

**Drill:** Merge Intervals · Insert Interval · Non-Overlapping Intervals · Meeting Rooms I & II

---

## 11. Trees: DFS vs BFS — *paths vs levels*

```
  "any path / depth / combine children"  →  DFS (recursion)
  "level by level / nearest / view"      →  BFS (queue)

         1                DFS answer at node =
        / \                 f(answer(left), answer(right))
       2   3
      / \        BFS:  [1] → [2,3] → [4,5]   level by level
     4   5
```

**The DFS thought:** *"If my left child told me X and right child told me Y, my answer is …"* — that one sentence solves depth, diameter, path sum, balanced, LCA.

**Drill:** Max Depth · Diameter · Invert Tree · Level Order Traversal · Validate BST (pass down min/max bounds) · Lowest Common Ancestor

---

## 12. Graphs — *grids are graphs too*

**Cue words:** islands, connected, spread/infection, word ladder, prerequisites

```
  # # . .        every '#' cell = a node
  # . . #        neighbors = up/down/left/right
  . . # #        "number of islands" = count DFS/BFS floods
```

```
  unweighted shortest path  →  BFS
  weighted, non-negative    →  Dijkstra (heap)
  limited hops / negative   →  Bellman-Ford
  dependency order          →  Topological sort (peel in-degree 0)
  incremental connectivity  →  Union-Find
```

**Drill:** Number of Islands · Rotting Oranges (multi-source BFS) · Clone Graph · Course Schedule (topo) · Redundant Connection (union-find) · Network Delay Time (Dijkstra)

---

## 13. Backtracking — *generate ALL of something*

**Cue words:** all subsets / permutations / combinations / valid boards; n ≤ ~20

```
  subsets of [1,2,3]:  at each element, a fork:
                        take it ──┐
                        skip it ──┴─ recurse both, UNDO after

            []
          /    \
        [1]     []
       /  \    /  \
   [1,2] [1] [2]  []   ... every leaf = one answer
```

**The thought:** *"They want the LIST of all answers (not a count) → I must walk the whole decision tree: choose → recurse → un-choose."*

```python
def backtrack(path, choices):
    if done: ans.append(path[:]); return
    for c in choices:
        path.append(c)
        backtrack(path, next_choices)
        path.pop()                    # ← the undo IS the pattern
```

**Drill:** Subsets · Combination Sum · Permutations · Word Search · Palindrome Partitioning · N-Queens

---

## 14. Dynamic Programming — *count ways / best result over choices*

**Cue words:** how many ways, min cost, max value, "can you reach/partition", two sequences

```
  Climbing Stairs:  ways(n) = ways(n-1) + ways(n-2)
                    1  2  3  5  8  13 …

  spot it:  answer(big) = combine( answer(smaller) )
            AND the same subproblems repeat
```

**COUNT or BEST → DP.  LIST them all → backtracking.**
(Coin Change = DP. Combination Sum = backtracking. Same costume, different question.)

The four famous skeletons:
```
  take-or-skip (House Robber):   dp[i] = max(dp[i-1], dp[i-2] + a[i])
  unbounded coins (Coin Change): dp[x] = min(dp[x - coin] + 1)
  two sequences (LCS):           dp[i][j] from dp[i-1][j-1] / neighbors
  LIS:                           dp[i] = best chain ending at i
```

**Drill:** Climbing Stairs · House Robber · Coin Change · Longest Common Subsequence · Longest Increasing Subsequence · Unique Paths · Partition Equal Subset Sum

---

## 15. Greedy — *the local best is provably enough*

**Cue words:** jump game, gas station, assign/schedule max tasks

**The thought:** *"Do I ever regret the greedy choice? If a sort + one pass can't be beaten by looking ahead → greedy."* If you can't argue it, fall back to DP.

**Drill:** Jump Game · Gas Station · Hand of Straights · Merge Triplets

---

## 16. The specialists

```
  Trie          many words + prefix queries        Implement Trie, Word Search II
  Union-Find    merging groups over time           Valid Tree, Count Components
  Bit / XOR     "appears twice except one",        Single Number, Missing Number,
                O(1) space number tricks           Counting Bits
  Cyclic sort   array holds values 1..n            Find Duplicate, First Missing Positive
  Design        O(1) ops → hashmap + helper        LRU Cache (map + doubly-linked list)
```

---

# More mental pictures — structures you rebuild from memory

If you can redraw the picture on the whiteboard, the code writes itself.

**Trie** — one stored prefix serves every word; `startsWith` = walk the path
```
  root ── c ── a ── t ●   (cat)
              └──── r ●   (car)     cat + car share c-a, stored ONCE
         └── o ── d ── e ●  (code)  ● = word-end flag
```

**Union-Find** — forests that merge; same root ⇔ same group
```
      1           4        union(3,5): hang root 4 under root 1
     / \          |        find(x): climb parents to the root (compress!)
    2   3         5        edge joining two same-root nodes → CYCLE
```

**Topological sort** — peel the free nodes
```
  A(indeg 0) ──→ C(indeg 2) ──→ D(indeg 1)
  B(indeg 0) ──↗
  peel order: A B C D · peeled < n at the end → cycle → impossible
```

**Two heaps** — the median lives at the boundary
```
   small half  ▲ 5   |   7 ▼  large half      median = (5+7)/2
   (max-heap)        |        (min-heap)      keep sizes within 1
```

**LRU Cache** — two structures covering each other's weakness
```
  hashmap ──→ [A] ⇄ [B] ⇄ [C]
  key→node   head=just used   tail=evict me
  get/put O(1): map FINDS the node, list REORDERS it
```

**The 2-D DP grid** — every two-sequence problem is this table
```
  LCS("abc","ace"):     a  b  c
                     a  1  1  1     match → 1 + diagonal ↘
                     c  1  1  2     else  → max(left, up)
                     e  1  1 [2] ← answer bottom-right
  same table, new rules = Edit Distance, Distinct Subsequences
```

---

# Sorting — steal the algorithm, skip the sort

No interviewer asks you to implement mergesort. But the **machinery inside each sort** is a reusable pattern that solves famous problems on its own.

## Which tool, when

```
  need the full order, general values      →  built-in sort O(n log n), then
                                              two pointers / sweep / greedy
  only the Kth / top-K, not full order     →  quickselect O(n) or heap — DON'T sort
  values in a small range (0..n, colors)   →  counting / bucket sort O(n)
  data arrives as sorted pieces            →  the merge step, O(n + m)
  values are exactly 1..n + O(1) space     →  cyclic sort (swap each value home)
  stream keeps growing, need best-so-far   →  heap (heapsort's engine, run lazily)
```

## Mergesort's merge step — *two fingers, always take the smaller*

```
  A: [1, 4, 7]     ↑a
  B: [2, 3, 9]     ↑b        take min(A[a], B[b]), advance that finger
  out: 1  2  3  4  7  9      O(n+m), nothing re-compared

  bonus: while merging, every time B wins, A's remaining
  elements are all inversions → count them for free
```

**Powers:** Merge Two Sorted Lists · Merge Sorted Array · Merge K Sorted Lists (+ heap) · Sort List (mergesort on a linked list) · Count of Smaller Numbers After Self (inversions) · Reverse Pairs

## Quicksort's partition — *one pass finalizes the pivot's position*

```
  [ < pivot | = pivot | > pivot ]
            ↑lo       ↑hi           Dutch national flag: 3 regions, one pass

  quickselect: after one partition the pivot index is FINAL →
  recurse only into the side holding k:  n + n/2 + n/4 + … = 2n → O(n) avg
```

```python
def quickselect(lo, hi, k):          # kth smallest
    p = partition(lo, hi)
    if p == k: return a[p]
    return quickselect(p+1, hi, k) if p < k else quickselect(lo, p-1, k)
```

**Powers:** Kth Largest Element · K Closest Points · Top K Frequent (alt.) · Sort Colors (Dutch flag) · Wiggle Sort II

## Counting & bucket sort — *indexes replace comparisons*

```
  Top K Frequent, the O(n) way:
  bucket[count] = [values with that count]     count can't exceed n
  [ count1:[3] ][ count2:[2] ][ count3:[1] ]
                                    ↑ read right-to-left, collect k
```

**Powers:** Top K Frequent Elements ✓ · Sort Colors (count 0/1/2) · H-Index · Maximum Gap (buckets + pigeonhole) · Sort Characters by Frequency

## Cyclic sort — *every value has a home index*

```
  values 1..n → value v belongs at index v−1

  [3, 4, -1, 1]  → swap everyone home →  [1, -1, 3, 4]
   └──────↘ 3 goes to index 2               ↑
                                    first index where a[i] ≠ i+1 → answer 2
```

```python
i = 0
while i < n:
    home = a[i] - 1
    if 0 <= home < n and a[home] != a[i]:
        a[i], a[home] = a[home], a[i]     # send it home, stay put
    else:
        i += 1
```

**Powers:** Missing Number · First Missing Positive · Find the Duplicate Number · Find All Duplicates · Set Mismatch

## The quiet ones

- **Heapsort** is the heap pattern run to completion → Top K, Kth in a Stream, Last Stone Weight.
- **Patience sorting** is the O(n log n) trick behind Longest Increasing Subsequence.
- And the quietest cue of all: **"sort first" unlocks whole families** — 3Sum, Merge Intervals, Meeting Rooms, Non-Overlapping Intervals, Car Fleet, Hand of Straights all begin with one `sort()`.

---

# The Recognition Gym — all of NeetCode 150 (+ bonuses)

Read the statement and example, **name the pattern out loud**, then expand to check yourself. Problems marked ✓ are already solved in your repo. (For a shuffled quiz with the groupings hidden, use the [interactive version](https://claude.ai/code/artifact/c3d0bb5b-5cbd-46ec-bbdf-c19767477735).)

## Hash Map & Arrays

#### Contains Duplicate ✓
Given an integer array, return true if any value appears at least twice.
`[1,2,3,1] → true`
<details><summary>🤔 reveal pattern</summary>

**Hash set — O(n).** "Have I seen this before?" is literally the problem statement.

```python
seen = set()
for x in nums:
    if x in seen: return True
    seen.add(x)
return False
```
</details>

#### Valid Anagram ✓
Given two strings s and t, return true if t is an anagram of s.
`s="racecar", t="carrace" → true`
<details><summary>🤔 reveal pattern</summary>

**Hashmap of counts — O(n).** Anagram = identical letter counts. Counting anything = hashmap.

```python
return Counter(s) == Counter(t)
```
</details>

#### Two Sum ✓
Return indices of the two numbers that add up to target. Exactly one solution exists.
`nums=[3,4,5,6], target=7 → [0,1]`
<details><summary>🤔 reveal pattern</summary>

**Hashmap complement lookup — O(n).** The brute force keeps re-searching for `target − x` → remember what you've seen instead.

```python
seen = {}
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target - x], i]
    seen[x] = i
```
</details>

#### Group Anagrams ✓
Group a list of strings so that all anagrams end up together.
`["eat","tea","tan","ate"] → [["eat","tea","ate"],["tan"]]`
<details><summary>🤔 reveal pattern</summary>

**Hashmap with canonical key — O(n·k).** Anagrams share one identity: their sorted letters (or 26-count tuple). "Group by X" = hashmap keyed on X.

```python
groups = defaultdict(list)
for w in strs:
    groups[tuple(sorted(w))].append(w)
return list(groups.values())
```
</details>

#### Top K Frequent Elements ✓
Return the k most frequent elements of an array.
`nums=[1,1,1,2,2,3], k=2 → [1,2]`
<details><summary>🤔 reveal pattern</summary>

**Hashmap counts → bucket sort (or heap) — O(n).** Two shapes stacked: counting → hashmap; then top-K → heap, or buckets indexed by count (count ≤ n) for O(n).

```python
cnt = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]
for x, c in cnt.items(): buckets[c].append(x)
# walk buckets from the top, collect k
```
</details>

#### Encode and Decode Strings ✓
Design encode(list of strings) → one string, and decode back. Strings may contain any character.
`["neet","code"] → "4#neet4#code"`
<details><summary>🤔 reveal pattern</summary>

**Length-prefix encoding.** Any delimiter can be faked by the data — a length prefix cannot. `4#` says exactly how far to read.

```python
encode: "".join(f"{len(s)}#{s}" for s in strs)
decode: read digits until "#", slice that many chars, repeat
```
</details>

#### Valid Sudoku ✓
Given a 9×9 board (partially filled), check that no digit repeats in any row, column, or 3×3 box.
<details><summary>🤔 reveal pattern</summary>

**Hash sets per row / col / box — O(81).** Three simultaneous "seen before?" questions. Box key trick: `(r // 3, c // 3)`.

```python
if v in rows[r] or v in cols[c] or v in boxes[(r//3, c//3)]:
    return False
```
</details>

#### Longest Consecutive Sequence ✓
Given an unsorted array, return the length of the longest run of consecutive integers. Must run in O(n).
`[100,4,200,1,3,2] → 4  (1,2,3,4)`
<details><summary>🤔 reveal pattern</summary>

**Hash set + start-of-sequence check — O(n).** A sorted-sounding question with an O(n) demand → set. Only count up from x when x−1 is absent, so each chain is walked once.

```python
s = set(nums)
for x in s:
    if x - 1 not in s:
        run = 1
        while x + run in s: run += 1
        best = max(best, run)
```
</details>

## Two Pointers

#### Valid Palindrome ✓
Return true if the string reads the same forwards and backwards, ignoring non-alphanumerics and case.
`"Was it a car or a cat I saw?" → true`
<details><summary>🤔 reveal pattern</summary>

**Two pointers from both ends — O(n).** Palindrome = compare mirror positions → converge from the ends.

```python
l, r = 0, len(s) - 1
while l < r:
    if s[l] != s[r]: return False
    l += 1; r -= 1
```
</details>

#### Two Sum II (sorted input) ✓
Same as Two Sum, but the array is sorted. O(1) extra space required.
`[1,2,3,4], target=3 → [1,2]`
<details><summary>🤔 reveal pattern</summary>

**Two pointers — O(n), O(1) space.** SORTED changes everything: sum too small → only `l++` can help; too big → only `r--`.

```python
while l < r:
    s = a[l] + a[r]
    if s == target: return [l + 1, r + 1]
    if s < target: l += 1
    else: r -= 1
```
</details>

#### 3Sum ✓
Find all unique triplets in the array that sum to zero.
`[-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]`
<details><summary>🤔 reveal pattern</summary>

**Sort + fix one + two pointers — O(n²).** Fix `nums[i]`; what remains is Two Sum II on a sorted remainder. Skip duplicate values to avoid repeat triplets.

```python
nums.sort()
for i in range(n):
    if i and nums[i] == nums[i-1]: continue
    # two pointers on nums[i+1:] targeting -nums[i]
```
</details>

#### Container With Most Water ✓
Given line heights, choose two lines that hold the most water between them.
`[1,7,2,5,4,7,3,6] → 36`
<details><summary>🤔 reveal pattern</summary>

**Two pointers, move the shorter wall — O(n).** Width only shrinks as pointers close in — the only possible improvement is replacing the SHORTER wall.

```python
while l < r:
    best = max(best, (r - l) * min(h[l], h[r]))
    if h[l] < h[r]: l += 1
    else: r -= 1
```
</details>

#### Trapping Rain Water ✓
Given an elevation map, compute how much rain water it traps.
`[0,2,0,3,1,0,1,3] → 6`
<details><summary>🤔 reveal pattern</summary>

**min(leftmax, rightmax) per bar → prefix/suffix or two pointers.** "Water on bar i = min(best left wall, best right wall) − h[i]." Both sides needed → prefix/suffix arrays; the O(1)-space follow-up → advance the side with the smaller max.

```python
while l < r:
    if lmax <= rmax:
        l += 1; lmax = max(lmax, h[l]); water += lmax - h[l]
    else:
        r -= 1; rmax = max(rmax, h[r]); water += rmax - h[r]
```
</details>

## Sliding Window

#### Best Time to Buy & Sell Stock ✓
Given daily prices, maximize profit from one buy followed by one later sell.
`[10,1,5,6,7,1] → 6  (buy 1, sell 7)`
<details><summary>🤔 reveal pattern</summary>

**Running min — O(n), O(1) space.** Best ordered pair (buy BEFORE sell) → each day only needs the cheapest EARLIER day.

```python
lo, best = inf, 0
for p in prices:
    best = max(best, p - lo)
    lo = min(lo, p)
```
</details>

#### Longest Substring Without Repeating Characters
Length of the longest substring in which every character is distinct.
`"zxyzxyz" → 3`
<details><summary>🤔 reveal pattern</summary>

**Sliding window + set — O(n).** Contiguous + "longest" + a condition that only breaks when you ADD → expand right, shrink left on repeat. Never restart.

```python
for r in range(n):
    while s[r] in win:
        win.remove(s[l]); l += 1
    win.add(s[r]); best = max(best, r - l + 1)
```
</details>

#### Longest Repeating Character Replacement
Longest substring that can be made all one letter using at most k replacements.
`"XYYX", k=2 → 4`
<details><summary>🤔 reveal pattern</summary>

**Window; valid ⇔ size − maxFreq ≤ k.** Replacements needed = window size − count of its most common letter. That inequality IS the validity test.

```python
count[s[r]] += 1
while (r - l + 1) - max(count.values()) > k:
    count[s[l]] -= 1; l += 1
```
</details>

#### Permutation in String
Return true if s2 contains any permutation of s1 as a substring.
`s1="abc", s2="lecabee" → true ("cab")`
<details><summary>🤔 reveal pattern</summary>

**Fixed-size window + letter counts — O(n).** A permutation is a window of exactly len(s1) chars with identical counts → slide a fixed window, update two counters per step.
</details>

#### Minimum Window Substring
Smallest substring of s that contains every character of t, with multiplicity.
`s="OUZODYXAZV", t="XYZ" → "YXAZ"`
<details><summary>🤔 reveal pattern</summary>

**Window + need/have counts — O(n).** "Smallest window containing…" → expand until valid, then shrink from the left while STILL valid, recording each time.
</details>

#### Sliding Window Maximum
Return the maximum of every window of size k.
`[1,2,1,0,4,2,6], k=3 → [2,2,4,4,6]`
<details><summary>🤔 reveal pattern</summary>

**Monotonic deque — O(n).** Keep a DECREASING deque of candidate indices; the front is always the max; smaller elements behind a bigger one can never win — pop them.

```python
while dq and a[dq[-1]] < a[r]: dq.pop()
dq.append(r)
if dq[0] == r - k: dq.popleft()
if r >= k - 1: ans.append(a[dq[0]])
```
</details>

## Prefix / Suffix

#### Product of Array Except Self ✓
Return out where out[i] is the product of every element except nums[i]. No division; O(n).
`[1,2,4,6] → [48,24,12,8]`
<details><summary>🤔 reveal pattern</summary>

**Prefix products, then suffix pass — O(n).** Each index needs "product of everything to my left" × "…to my right" → two directional pre-passes.

```python
pre = 1
for i in range(n): out[i] = pre; pre *= a[i]
suf = 1
for i in reversed(range(n)): out[i] *= suf; suf *= a[i]
```
</details>

#### Subarray Sum Equals K (bonus)
Count contiguous subarrays summing to k. Negatives allowed.
`[1,2,3], k=3 → 2  ([1,2] and [3])`
<details><summary>🤔 reveal pattern</summary>

**Prefix sum + hashmap — O(n).** Negatives break sliding window. `sum(i..j) = pre[j] − pre[i]` → at each j ask "have I seen `pre − k` before?" — Two Sum in disguise.

```python
seen = {0: 1}
for x in nums:
    pre += x
    ans += seen.get(pre - k, 0)
    seen[pre] = seen.get(pre, 0) + 1
```
</details>

## Stack

#### Valid Parentheses
Given a string of `()[]{}`. Is every bracket closed by the right type, in the right order?
`"([{}])" → true   "[(])" → false`
<details><summary>🤔 reveal pattern</summary>

**Stack — O(n).** A closer must match the MOST RECENT unresolved opener → LIFO.

```python
for c in s:
    if c in "([{": st.append(c)
    elif not st or pair[c] != st.pop(): return False
return not st
```
</details>

#### Min Stack
Design a stack supporting push, pop, top, and getMin — every operation O(1).
<details><summary>🤔 reveal pattern</summary>

**Stack of (value, min-so-far) pairs.** getMin must survive pops in O(1) → store the running min WITH each entry; popping restores the previous min for free.
</details>

#### Evaluate Reverse Polish Notation
Evaluate an arithmetic expression given in postfix (RPN) form.
`["1","2","+","3","*"] → 9`
<details><summary>🤔 reveal pattern</summary>

**Stack — O(n).** An operator applies to the two most recent unresolved operands → pop two, push result.
</details>

#### Generate Parentheses
Generate all well-formed strings of n bracket pairs.
`n=2 → ["(())","()()"]`
<details><summary>🤔 reveal pattern</summary>

**Backtracking with open/close counters.** "Generate ALL valid X" → backtracking (even though NeetCode shelves it under Stack). Add `(` while any remain; add `)` only if it won't unbalance.

```python
def bt(s, o, c):
    if len(s) == 2 * n: ans.append(s); return
    if o < n: bt(s + "(", o + 1, c)
    if c < o: bt(s + ")", o, c + 1)
```
</details>

## Monotonic Stack

#### Daily Temperatures
For each day, how many days until a warmer temperature? 0 if it never comes.
`[73,74,75,71,69,72] → [1,1,3,2,1,0]`
<details><summary>🤔 reveal pattern</summary>

**Monotonic decreasing stack — O(n).** "Next greater to the right", verbatim. Each new temp pops every colder waiting day and answers it.

```python
for i, t in enumerate(temps):
    while st and temps[st[-1]] < t:
        j = st.pop(); ans[j] = i - j
    st.append(i)
```
</details>

#### Car Fleet
Cars at positions/speeds drive toward a target; a faster car stuck behind a slower one becomes one fleet. How many fleets arrive?
`target=10, pos=[1,4], speed=[3,2] → 1`
<details><summary>🤔 reveal pattern</summary>

**Sort by position + stack of arrival times.** Sort closest-to-target first. A car merges iff its arrival time ≤ the fleet ahead; surviving times form a monotonic stack.

```python
for pos, sp in sorted(cars, reverse=True):
    t = (target - pos) / sp
    if not st or t > st[-1]: st.append(t)
return len(st)
```
</details>

#### Largest Rectangle in Histogram
Find the largest rectangle that fits under a histogram.
`[2,1,5,6,2,3] → 10  (5×2)`
<details><summary>🤔 reveal pattern</summary>

**Monotonic increasing stack — O(n).** Bar i's best rectangle extends to the first SHORTER bar on each side → "nearest smaller", twice. When a bar pops, its right wall was just found.

```python
for i, h in enumerate(heights + [0]):
    while st and heights[st[-1]] >= h:
        H = heights[st.pop()]
        W = i - (st[-1] + 1 if st else 0)
        best = max(best, H * W)
    st.append(i)
```
</details>

#### Next Greater Element I (bonus)
For each element, find the first greater element to its right.
`[2,1,3] → [3,3,-1]`
<details><summary>🤔 reveal pattern</summary>

**Monotonic stack — O(n).** The template problem — drill the pop-and-answer motion here first.
</details>

## Binary Search

#### Binary Search
Find target's index in a sorted array, or −1. Must be O(log n).
`[-1,0,3,5,9,12], t=9 → 4`
<details><summary>🤔 reveal pattern</summary>

**Classic binary search.** Sorted + O(log n) demanded — the direct cue.
</details>

#### Search a 2D Matrix
Rows sorted; each row starts after the previous ends. Find target in O(log(n·m)).
<details><summary>🤔 reveal pattern</summary>

**One binary search over the flattened matrix.** It's one sorted array wearing 2D clothes: index k ↔ `(k // m, k % m)`.
</details>

#### Koko Eating Bananas
Koko eats piles at speed k/hour (max one pile per hour). Minimum k to finish within h hours.
`piles=[3,6,7,11], h=8 → 4`
<details><summary>🤔 reveal pattern</summary>

**Binary search on the ANSWER.** "Minimum speed that works" + works(k) flips ✗✗✗✓✓✓ monotonically → search the answer space, not the array.

```python
def works(k): return sum(ceil(p / k) for p in piles) <= h
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if works(mid): hi = mid
    else: lo = mid + 1
```
</details>

#### Find Minimum in Rotated Sorted Array
A sorted array was rotated an unknown amount. Find the minimum in O(log n).
`[3,4,5,1,2] → 1`
<details><summary>🤔 reveal pattern</summary>

**Binary search on the rotation break.** Compare mid to the RIGHT end: `a[mid] > a[hi]` means the break (and the min) lies right of mid.

```python
while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] > a[hi]: lo = mid + 1
    else: hi = mid
```
</details>

#### Search in Rotated Sorted Array
Find target in a rotated sorted array in O(log n).
`[4,5,6,7,0,1,2], t=0 → 4`
<details><summary>🤔 reveal pattern</summary>

**Binary search, pick the sorted half.** One half around mid is always properly sorted — test whether target lies inside it; else recurse into the other half.
</details>

#### Time Based Key-Value Store
`set(key, value, timestamp)`; `get(key, timestamp)` returns the latest value stored at or before that time.
<details><summary>🤔 reveal pattern</summary>

**Hashmap of lists + binary search.** Timestamps arrive in order → each key holds a SORTED list → "latest ≤ t" is a right-boundary bisect.
</details>

#### Median of Two Sorted Arrays
Two sorted arrays; find the median of their union in O(log(min(n,m))).
`[1,3] + [2] → 2.0`
<details><summary>🤔 reveal pattern</summary>

**Binary search the partition.** Search how many elements the smaller array contributes to the combined left half, so every left element ≤ every right element.
</details>

## Linked List

#### Reverse Linked List
Reverse a singly linked list.
`1→2→3 becomes 3→2→1`
<details><summary>🤔 reveal pattern</summary>

**In-place pointer flip — O(n).** Three pointers walk together: prev, cur, next.

```python
prev = None
while cur:
    cur.next, prev, cur = prev, cur, cur.next
return prev
```
</details>

#### Merge Two Sorted Lists
Merge two sorted linked lists into one sorted list.
<details><summary>🤔 reveal pattern</summary>

**Two pointers on lists.** Always take the smaller head; a dummy node kills the edge cases.
</details>

#### Reorder List
Reorder L0→L1→…→Ln into L0→Ln→L1→Ln−1→…, in place.
`1→2→3→4 → 1→4→2→3`
<details><summary>🤔 reveal pattern</summary>

**Find middle + reverse half + merge.** Composite of three drilled sub-patterns: fast/slow middle, in-place reversal, interleave.
</details>

#### Remove Nth Node From End
Delete the nth node from the end in one pass.
`1→2→3→4, n=2 → 1→2→4`
<details><summary>🤔 reveal pattern</summary>

**Two pointers, n apart.** Lead pointer gets an n-step head start; when it reaches the end, the trailer stands just before the victim.
</details>

#### Copy List with Random Pointer
Deep-copy a list whose nodes each have an extra random pointer to any node (or null).
<details><summary>🤔 reveal pattern</summary>

**Hashmap old→new, two passes.** Random pointers can point anywhere → pass 1 makes clones, pass 2 wires next/random through the map.
</details>

#### Add Two Numbers
Two numbers stored as reversed-digit linked lists; return their sum, same format.
`(2→4→3) + (5→6→4) → 7→0→8   (342+465=807)`
<details><summary>🤔 reveal pattern</summary>

**Digit-by-digit with carry.** Grade-school addition; the only trap is the leftover final carry.
</details>

#### Linked List Cycle
Does the linked list contain a cycle?
<details><summary>🤔 reveal pattern</summary>

**Fast & slow pointers — O(1) space.** If there's a loop, the hare must lap the tortoise.
</details>

#### Find the Duplicate Number
n+1 integers in range 1..n, one value repeated. Find it without modifying the array, O(1) space.
`[1,2,3,2,2] → 2`
<details><summary>🤔 reveal pattern</summary>

**Floyd's cycle detection on i → nums[i].** Values 1..n → treat index→value as a linked list; the duplicate is a cycle entrance. Phase 2 of Floyd's finds it.
</details>

#### LRU Cache
Fixed-capacity cache: get and put in O(1), evicting the least-recently-used entry when full.
<details><summary>🤔 reveal pattern</summary>

**Hashmap + doubly linked list.** O(1) lookup → hashmap; O(1) move-to-front and evict-oldest → doubly linked list. Design questions = compose two structures, each covering the other's weakness.
</details>

#### Merge K Sorted Lists
Merge k sorted linked lists into one sorted list.
<details><summary>🤔 reveal pattern</summary>

**Min-heap of k heads — O(n log k).** Repeatedly need "smallest among k candidates" → heap of the current heads.
</details>

#### Reverse Nodes in K-Group
Reverse every consecutive group of exactly k nodes; leftovers stay as-is.
`1→2→3→4→5, k=2 → 2→1→4→3→5`
<details><summary>🤔 reveal pattern</summary>

**In-place reversal per group.** Reverse Linked List applied window by window; the craft is stitching each group's tail to the next group's head.
</details>

## Trees

#### Invert Binary Tree
Mirror a binary tree (swap every left/right child).
<details><summary>🤔 reveal pattern</summary>

**DFS — O(n).** "Do X at every node" → any traversal; swap children, recurse.
</details>

#### Maximum Depth of Binary Tree
Return the height of a binary tree.
<details><summary>🤔 reveal pattern</summary>

**DFS combine children.** "My depth = 1 + max(left's answer, right's answer)."
</details>

#### Diameter of Binary Tree
Length (in edges) of the longest path between any two nodes.
<details><summary>🤔 reveal pattern</summary>

**DFS: return height, record through-path.** Best path THROUGH a node = left height + right height. Return height up; record diameter on the side.

```python
def h(n):
    if not n: return 0
    L, R = h(n.left), h(n.right)
    best = max(best, L + R)
    return 1 + max(L, R)
```
</details>

#### Balanced Binary Tree
Is the tree height-balanced (every subtree's halves differ by ≤ 1)?
<details><summary>🤔 reveal pattern</summary>

**DFS height with a veto flag.** Height computation that can veto: bubble up failure the moment any subtree unbalances.
</details>

#### Same Tree
Are two binary trees structurally identical with equal values?
<details><summary>🤔 reveal pattern</summary>

**Parallel DFS.** Recurse both trees in lockstep; nulls must match nulls.
</details>

#### Subtree of Another Tree
Is subRoot identical to some subtree of root?
<details><summary>🤔 reveal pattern</summary>

**DFS + Same Tree at each node.** Composite: run Same Tree from every node of root.
</details>

#### Lowest Common Ancestor of a BST
Find the LCA of two nodes in a binary SEARCH tree.
<details><summary>🤔 reveal pattern</summary>

**Walk down using BST ordering.** Both smaller → left; both bigger → right; the split point is the LCA.
</details>

#### Binary Tree Level Order Traversal
Return node values grouped level by level.
<details><summary>🤔 reveal pattern</summary>

**BFS with a queue.** "Level by level" is the literal definition of BFS; snapshot `len(queue)` per level.
</details>

#### Binary Tree Right Side View
Values visible looking from the right, top to bottom.
<details><summary>🤔 reveal pattern</summary>

**BFS, take each level's last node.** A per-level question in disguise.
</details>

#### Count Good Nodes in Binary Tree
Count nodes ≥ every ancestor on their root path.
<details><summary>🤔 reveal pattern</summary>

**DFS passing max-so-far DOWN.** The needed context flows downward → pass it as a recursion argument, not a return value.
</details>

#### Validate Binary Search Tree
Is the tree a valid BST?
`[5,4,6,null,null,3,7] → false (3 under 6 but < 5)`
<details><summary>🤔 reveal pattern</summary>

**DFS with (lo, hi) bounds.** Parent-vs-child checks miss deep violations — each subtree lives in an interval that tightens as you descend.

```python
def valid(n, lo, hi):
    if not n: return True
    if not (lo < n.val < hi): return False
    return valid(n.left, lo, n.val) and valid(n.right, n.val, hi)
```
</details>

#### Kth Smallest Element in a BST
Return the kth smallest value in a BST.
<details><summary>🤔 reveal pattern</summary>

**In-order traversal, count down.** In-order on a BST visits values in sorted order — stop at the kth visit.
</details>

#### Construct Tree from Preorder & Inorder
Rebuild the binary tree from its two traversals.
<details><summary>🤔 reveal pattern</summary>

**Recursion + hashmap of inorder positions.** `preorder[0]` is the root; its inorder position splits left and right subtrees.
</details>

#### Binary Tree Maximum Path Sum
Maximum sum over any node-to-node path.
`[-10,9,20,null,null,15,7] → 42  (15+20+7)`
<details><summary>🤔 reveal pattern</summary>

**DFS: through-value recorded, arm-value returned.** Record best THROUGH me (L + me + R); return my best single arm (me + max(L, R, 0)) — clamp negatives to 0.
</details>

#### Serialize and Deserialize Binary Tree
Encode a tree to a string and decode it back exactly.
`[1,2,3] ⇄ "1,2,N,N,3,N,N"`
<details><summary>🤔 reveal pattern</summary>

**Preorder with explicit null markers.** "N" for nulls makes the string self-describing: decode consumes tokens recursively.
</details>

## Heap / Priority Queue

#### Kth Largest Element in a Stream
Accept numbers one at a time; always answer "what is the kth largest so far?"
<details><summary>🤔 reveal pattern</summary>

**Min-heap capped at size k.** Keep only the k best; the root IS the answer.

```python
heappush(h, val)
if len(h) > k: heappop(h)
return h[0]
```
</details>

#### Last Stone Weight
Repeatedly smash the two heaviest stones (equal → both vanish; else the difference remains). What's left?
`[2,7,4,1,8,1] → 1`
<details><summary>🤔 reveal pattern</summary>

**Max-heap simulation.** "Repeatedly take the two largest" → heap; simulate.
</details>

#### K Closest Points to Origin
Return the k points nearest the origin.
<details><summary>🤔 reveal pattern</summary>

**Heap of size k (or quickselect).** Top-K by score; compare x² + y², no sqrt needed.
</details>

#### Kth Largest Element in an Array
Find the kth largest without fully sorting.
`[3,2,1,5,6,4], k=2 → 5`
<details><summary>🤔 reveal pattern</summary>

**Quickselect O(n) avg / min-heap O(n log k).** One-shot selection → partition toward index n−k.
</details>

#### Task Scheduler
Identical tasks need a cooldown of n ticks between runs. Minimum total ticks (idles count)?
`[A,A,A,B,B,B], n=2 → 8  (AB_AB_AB)`
<details><summary>🤔 reveal pattern</summary>

**Greedy frame from max frequency.** The most frequent task dictates the skeleton: `(maxf − 1)·(n + 1) + (tasks tied at maxf)`; everything else fills gaps.
</details>

#### Design Twitter
postTweet, follow, unfollow, getNewsFeed (10 most recent across followees).
<details><summary>🤔 reveal pattern</summary>

**Hashmaps + heap merge of feeds.** News feed = merge k time-sorted lists → Merge K Lists pattern.
</details>

#### Find Median from Data Stream
Support addNum and findMedian over a growing stream.
<details><summary>🤔 reveal pattern</summary>

**Two balanced heaps.** Median = the boundary between two halves → max-heap of the small half + min-heap of the large half, sizes within 1.
</details>

## Backtracking

#### Subsets
Return all subsets of an array of distinct integers.
`[1,2,3] → 8 subsets`
<details><summary>🤔 reveal pattern</summary>

**Backtracking take/skip — O(2ⁿ).** The output is ALL configurations → walk the decision tree.

```python
def bt(i):
    if i == n: ans.append(path[:]); return
    path.append(a[i]); bt(i + 1)   # take
    path.pop();        bt(i + 1)   # skip
```
</details>

#### Combination Sum
All unique combinations (elements reusable) summing to target.
`[2,3,6,7], t=7 → [[2,2,3],[7]]`
<details><summary>🤔 reveal pattern</summary>

**Backtracking, stay-or-advance.** Reuse allowed → after taking, recurse with the SAME index.
</details>

#### Subsets II
All subsets of an array WITH duplicates — no duplicate subsets in output.
<details><summary>🤔 reveal pattern</summary>

**Sort + skip repeated siblings.** When you SKIP a value, skip all its copies so equal branches never fork twice: `if j > start and a[j] == a[j-1]: continue`.
</details>

#### Combination Sum II
Combinations summing to target; each element used once; no duplicate combos.
<details><summary>🤔 reveal pattern</summary>

**Sort + same-depth dedup.** At one tree depth, never start two branches with the same value.
</details>

#### Permutations
All orderings of distinct integers.
`[1,2,3] → 6 permutations`
<details><summary>🤔 reveal pattern</summary>

**Backtracking with a used set — O(n!).** Each tree level picks any not-yet-used element.
</details>

#### Word Search
Does the word exist in the grid, moving through adjacent cells without reuse?
<details><summary>🤔 reveal pattern</summary>

**Backtracking DFS on the grid.** Path-finding toward an exact string → DFS with mark/unmark. The UNMARK makes it backtracking, not flood fill.
</details>

#### Palindrome Partitioning
All ways to split a string into palindromic substrings.
`"aab" → [["a","a","b"],["aa","b"]]`
<details><summary>🤔 reveal pattern</summary>

**Backtracking over cut positions.** Backtrack over prefixes, recursing only when the prefix is a palindrome.
</details>

#### Letter Combinations of a Phone Number
All letter strings a digit string could type on a keypad.
`"34" → ["dg","dh","di",...]`
<details><summary>🤔 reveal pattern</summary>

**Backtracking / cartesian product.** One fixed choice-set per digit → depth = digit index.
</details>

#### N-Queens
Place n queens so none attack; return all boards.
`n=4 → 2 solutions`
<details><summary>🤔 reveal pattern</summary>

**Backtracking row by row + attack sets.** One queen per row; O(1) conflict checks via sets for columns, diagonals (r−c), anti-diagonals (r+c).
</details>

## Tries

#### Implement Trie (Prefix Tree)
Build insert(word), search(word), startsWith(prefix).
<details><summary>🤔 reveal pattern</summary>

**Tree of char → child maps.** "startsWith" is the giveaway — hashmaps can't share prefixes; a character tree can.
</details>

#### Design Add and Search Words
A word dictionary where search supports `.` matching any letter.
`add "day" → search "d.y" = true`
<details><summary>🤔 reveal pattern</summary>

**Trie + DFS on wildcards.** `.` = branch into EVERY child at that position.
</details>

#### Word Search II
Find all dictionary words that appear in a letter grid.
<details><summary>🤔 reveal pattern</summary>

**Trie + backtracking DFS together.** Don't run Word Search per word — walk the grid and the trie IN LOCKSTEP; a missing trie child prunes the whole branch.
</details>

## Graphs

#### Number of Islands
Count groups of connected "1" (land) cells in a grid.
<details><summary>🤔 reveal pattern</summary>

**Flood fill — count the floods.** Grid = graph; "how many groups" = count connected components.
</details>

#### Max Area of Island
Area of the largest connected land blob.
<details><summary>🤔 reveal pattern</summary>

**Flood fill that returns size.** The DFS returns `1 + sum(neighbors)`.
</details>

#### Clone Graph
Deep-copy an undirected graph given one node.
<details><summary>🤔 reveal pattern</summary>

**DFS/BFS + hashmap old→new.** Cycles mean revisits → the visited map doubles as the clone directory.
</details>

#### Walls and Gates
Grid of gates (0), walls, empty rooms (∞). Fill each room with distance to its nearest gate.
<details><summary>🤔 reveal pattern</summary>

**Multi-source BFS from all gates.** "Nearest of MANY sources" → seed the queue with every gate at distance 0.
</details>

#### Rotting Oranges
Each minute rot spreads to adjacent fresh oranges. Minutes until nothing fresh, or −1.
<details><summary>🤔 reveal pattern</summary>

**Multi-source BFS; levels = minutes.** Simultaneous spreading = one BFS wavefront; each queue level is one minute.
</details>

#### Pacific Atlantic Water Flow
Heights grid; water flows to equal-or-lower neighbors. Which cells reach BOTH oceans?
<details><summary>🤔 reveal pattern</summary>

**Reverse DFS from both coastlines.** Flood UPHILL from each ocean's border; answer = intersection of the two reachable sets.
</details>

#### Surrounded Regions
Flip every region of "O" fully surrounded by "X". Border-touching regions survive.
<details><summary>🤔 reveal pattern</summary>

**Flood from the border, then invert.** "Surrounded" = NOT connected to the border → mark border-connected O's safe, flip the rest.
</details>

#### Course Schedule
Given prerequisite pairs, can all courses be finished?
`[[1,0],[0,1]] → false`
<details><summary>🤔 reveal pattern</summary>

**Cycle detection / topological sort.** Prerequisites = directed edges; "can finish" = "no cycle" → Kahn's peel or DFS three-color.
</details>

#### Course Schedule II
Return one valid order to take all courses, or empty.
<details><summary>🤔 reveal pattern</summary>

**Topological sort (Kahn's).** They want the ORDER → the peel sequence is the answer.
</details>

#### Graph Valid Tree
Do n nodes and this edge list form a valid tree?
<details><summary>🤔 reveal pattern</summary>

**Union-Find (or DFS).** Tree = n−1 edges + connected + acyclic; union-find flags the cycle when an edge joins two already-joined nodes.
</details>

#### Number of Connected Components
Count connected components of an undirected graph.
<details><summary>🤔 reveal pattern</summary>

**Union-Find.** Start with n components; every successful union is −1.
</details>

#### Redundant Connection
A tree plus ONE extra edge. Find the edge to remove.
`[[1,2],[1,3],[2,3]] → [2,3]`
<details><summary>🤔 reveal pattern</summary>

**Union-Find — first cycle-closing edge.** The first edge whose endpoints are already connected closes the cycle.
</details>

#### Word Ladder
Minimum transformations from beginWord to endWord, changing one letter at a time through the word list.
`hit → hot → dot → dog → cog = 5`
<details><summary>🤔 reveal pattern</summary>

**BFS on the implicit word graph.** "Fewest steps" unweighted = BFS. Neighbors via wildcard buckets: `h*t`, `*it`, `hi*`.
</details>

## Advanced Graphs

#### Reconstruct Itinerary
Use every flight ticket exactly once from JFK; return the lexically smallest itinerary.
<details><summary>🤔 reveal pattern</summary>

**Eulerian path (Hierholzer's).** "Use every EDGE once" (not node) → DFS greedily smallest-first, append each airport on the way OUT, then reverse.
</details>

#### Min Cost to Connect All Points
Connect all 2-D points minimizing total Manhattan-distance wiring.
<details><summary>🤔 reveal pattern</summary>

**Minimum Spanning Tree — Prim's.** "Connect everything, minimize total cost" = MST; grow the tree via a heap of frontier edges.
</details>

#### Network Delay Time
A signal leaves node k through weighted directed edges. Time until ALL nodes receive it, or −1.
<details><summary>🤔 reveal pattern</summary>

**Dijkstra.** Weighted non-negative shortest paths from one source; answer = max of the shortest distances.
</details>

#### Swim in Rising Water
Grid of elevations; at time t you can stand on cells ≤ t. Earliest time to cross corner to corner.
<details><summary>🤔 reveal pattern</summary>

**Dijkstra on max-along-path (or binary search + BFS).** "Minimize the MAXIMUM cell on the path" → path cost = max elevation so far.
</details>

#### Alien Dictionary
Words are sorted in an unknown alphabet. Recover a valid letter ordering, or report impossible.
`["wrt","wrf","er","ett","rftt"] → "wertf"`
<details><summary>🤔 reveal pattern</summary>

**Edges from adjacent words → topological sort.** Each adjacent pair's FIRST differing letter yields one edge. Then it's Course Schedule II. Trap: `["abc","ab"]` is instantly invalid.
</details>

#### Cheapest Flights Within K Stops
Cheapest route from src to dst using at most k stops.
<details><summary>🤔 reveal pattern</summary>

**Bellman-Ford, k+1 rounds.** The stop LIMIT breaks Dijkstra's greedy proof → k+1 rounds of relaxing all edges; snapshot the array so one round can't chain.

```python
for _ in range(k + 1):
    new = dist.copy()
    for u, v, w in edges:
        new[v] = min(new[v], dist[u] + w)
    dist = new
```
</details>

## 1-D Dynamic Programming

#### Climbing Stairs
Climb 1 or 2 steps at a time. How many distinct ways to reach step n?
`n=3 → 3`
<details><summary>🤔 reveal pattern</summary>

**DP — Fibonacci.** "COUNT the ways" + last move was 1 or 2 → `ways(n) = ways(n−1) + ways(n−2)`.
</details>

#### Min Cost Climbing Stairs
Pay cost[i] when stepping off stair i; start at index 0 or 1; get past the end cheapest.
`[10,15,20] → 15`
<details><summary>🤔 reveal pattern</summary>

**DP: cheapest arrival.** `dp[i] = cost[i] + min(dp[i−1], dp[i−2])`.
</details>

#### House Robber
Rob houses for max loot; adjacent houses trigger the alarm.
`[2,9,8,3,6] → 16  (rob 2, 8, 6)`
<details><summary>🤔 reveal pattern</summary>

**DP take-or-skip.** THE canonical recurrence: `dp[i] = max(dp[i−1], dp[i−2] + a[i])`.
</details>

#### House Robber II
Same, but the houses form a circle.
`[2,3,2] → 3`
<details><summary>🤔 reveal pattern</summary>

**Run House Robber twice.** House 0 and house n−1 can't both be robbed → `max(rob(a[1:]), rob(a[:-1]))`.
</details>

#### Longest Palindromic Substring
Return the longest palindromic substring.
`"babad" → "bab"`
<details><summary>🤔 reveal pattern</summary>

**Expand around each center — O(n²).** A palindrome grows symmetrically from its center → try all 2n−1 centers.
</details>

#### Palindromic Substrings
Count how many substrings are palindromes.
`"aaa" → 6`
<details><summary>🤔 reveal pattern</summary>

**Expand around centers, counting.** Every successful widening is one more palindrome.
</details>

#### Decode Ways
Digits decode as 1→A … 26→Z. How many ways can the string decode?
`"121" → 3  (ABA, AU, LA)`
<details><summary>🤔 reveal pattern</summary>

**DP over 1- or 2-digit takes.** Fibonacci with guards; "0" is the trap.

```python
if s[i] != "0": dp[i] += dp[i + 1]
if 10 <= int(s[i:i+2]) <= 26: dp[i] += dp[i + 2]
```
</details>

#### Coin Change
Fewest coins (reuse allowed) to make an amount; −1 if impossible.
`coins=[1,3,5], amount=7 → 3`
<details><summary>🤔 reveal pattern</summary>

**Unbounded knapsack — min.** `dp[x] = 1 + min(dp[x − coin])`. Counting ways instead? That's Coin Change II.
</details>

#### Maximum Product Subarray
Contiguous subarray with the largest product.
`[2,3,-2,4] → 6`
<details><summary>🤔 reveal pattern</summary>

**DP tracking max AND min.** A negative flips fortunes: today's max may be yesterday's MIN × a negative → carry both extremes.
</details>

#### Word Break
Can the string be segmented entirely into dictionary words?
`"neetcode", ["neet","code"] → true`
<details><summary>🤔 reveal pattern</summary>

**DP over break positions.** `dp[i] = any(dp[j] and s[j:i] in dict)`.
</details>

#### Longest Increasing Subsequence
Length of the longest strictly increasing subsequence (not contiguous).
`[10,9,2,5,3,7,101,18] → 4`
<details><summary>🤔 reveal pattern</summary>

**DP O(n²), or patience + bisect O(n log n).** "Best chain ending at i" → look back at smaller elements; upgrade with a tails[] array + binary search.
</details>

#### Partition Equal Subset Sum
Can the array split into two subsets with equal sums?
`[1,5,11,5] → true`
<details><summary>🤔 reveal pattern</summary>

**0/1 knapsack over total/2.** "Pick a subset hitting a target sum" = knapsack; iterate sums DOWNWARD so each number is used once.
</details>

## 2-D Dynamic Programming

#### Unique Paths
Robot moves only right/down on an m×n grid. Count paths corner to corner.
`m=3, n=7 → 28`
<details><summary>🤔 reveal pattern</summary>

**Grid DP.** Paths INTO a cell = from above + from the left.
</details>

#### Longest Common Subsequence
Longest subsequence appearing in both strings.
`"abcde", "ace" → 3`
<details><summary>🤔 reveal pattern</summary>

**2D DP over index pairs.** Match → 1 + diagonal; else max of dropping one char from either side.
</details>

#### Buy & Sell Stock with Cooldown
Unlimited trades, but after selling you must skip one day. Max profit.
<details><summary>🤔 reveal pattern</summary>

**State-machine DP.** Choices over time WITH states (holding / cooldown / free) → one dp value per state per day.
</details>

#### Coin Change II
COUNT the combinations of coins (reuse allowed) making the amount.
`amount=5, coins=[1,2,5] → 4`
<details><summary>🤔 reveal pattern</summary>

**Unbounded knapsack — coins in the OUTER loop,** so different orderings are never double-counted.
</details>

#### Target Sum
Assign + or − to every number so the expression equals target. Count the ways.
`[1,1,1,1,1], target=3 → 5`
<details><summary>🤔 reveal pattern</summary>

**Algebra → subset-sum knapsack.** Positives P satisfy P = (total + target)/2 → count subsets summing to P.
</details>

#### Interleaving String
Is s3 formed by interleaving s1 and s2, preserving each one's order?
<details><summary>🤔 reveal pattern</summary>

**2D DP on prefix lengths.** State = (chars used from s1, from s2); s3's next char must extend one of them.
</details>

#### Longest Increasing Path in a Matrix
Longest strictly increasing path moving 4-directionally.
<details><summary>🤔 reveal pattern</summary>

**Memoized DFS (DP on a DAG).** Edges point uphill → no cycles → memoized DFS from every cell IS the DP.
</details>

#### Distinct Subsequences
Count distinct subsequences of s that equal t.
`s="rabbbit", t="rabbit" → 3`
<details><summary>🤔 reveal pattern</summary>

**2D DP: use-or-skip each s char.** If it matches you may consume both — plus you may always skip the s char.
</details>

#### Edit Distance
Minimum insert/delete/replace operations turning word1 into word2.
`"horse" → "ros" = 3`
<details><summary>🤔 reveal pattern</summary>

**2D DP (alignment table).** Match → diagonal free; else 1 + min(insert, delete, replace).
</details>

#### Burst Balloons
Bursting balloon i earns left·i·right of its CURRENT neighbors. Maximize coins.
`[3,1,5,8] → 167`
<details><summary>🤔 reveal pattern</summary>

**Interval DP — choose the LAST burst.** Neighbors change → think backwards: the balloon popped LAST in a range locks that range's boundaries.

```python
dp[l][r] = max over k of dp[l][k] + a[l]*a[k]*a[r] + dp[k][r]
```
</details>

#### Regular Expression Matching
Match a string against a pattern with `.` (any char) and `*` (zero+ of previous).
`s="aab", p="c*a*b" → true`
<details><summary>🤔 reveal pattern</summary>

**2D DP over (i, j).** `*` gives two branches: use it zero times (jump 2 pattern chars) or one more time (consume a matching string char, stay).
</details>

## Greedy

#### Maximum Subarray
Contiguous subarray with the largest sum.
`[-2,1,-3,4,-1,2,1,-5,4] → 6`
<details><summary>🤔 reveal pattern</summary>

**Kadane's — reset negative prefixes.** A negative running prefix can never help what follows → drop it and restart.

```python
cur = max(x, cur + x)
best = max(best, cur)
```
</details>

#### Jump Game
nums[i] is your max jump length from i. Can you reach the last index?
`[2,3,1,1,4] → true`
<details><summary>🤔 reveal pattern</summary>

**Greedy farthest-reach.** One running number — the farthest reachable index — answers everything.
</details>

#### Jump Game II
Minimum number of jumps to reach the last index.
`[2,3,1,1,4] → 2`
<details><summary>🤔 reveal pattern</summary>

**Greedy windows (implicit BFS levels).** Each jump unlocks a window of new indices → count windows until the end is inside one.
</details>

#### Gas Station
Circular route: gain gas[i], pay cost[i] to advance. Find the unique valid start, or −1.
<details><summary>🤔 reveal pattern</summary>

**Greedy reset after failure.** If total gas ≥ total cost an answer exists; when the tank dips negative, no station in that stretch can start → restart after it.
</details>

#### Hand of Straights
Can the cards split into groups of k consecutive values?
`[1,2,3,6,2,3,4,7,8], k=3 → true`
<details><summary>🤔 reveal pattern</summary>

**Greedy from the smallest + counts.** The smallest remaining card MUST start a straight — no branching → greedy, not backtracking.
</details>

#### Merge Triplets to Form Target
Merging two triplets takes the elementwise max. Can some merges produce the target exactly?
<details><summary>🤔 reveal pattern</summary>

**Greedy filter.** Any triplet exceeding the target ANYWHERE is poison; among the safe rest, check each target coordinate is hit.
</details>

#### Partition Labels
Split a string into the most parts so each letter appears in only one part.
`"ababcc" → [4,2]`
<details><summary>🤔 reveal pattern</summary>

**Greedy on last occurrences.** A part must stretch to the LAST occurrence of every letter inside it → running max of last-seen positions; cut when i reaches it.
</details>

#### Valid Parenthesis String
String of `(`, `)`, `*` where * can be any of the three (or empty). Can it be valid?
`"(*))" → true`
<details><summary>🤔 reveal pattern</summary>

**Greedy range of open counts.** Track [lo, hi] of possible open counts; `*` widens both ways. Dead if hi < 0; valid if lo can end at 0.
</details>

## Intervals

#### Insert Interval
Insert a new interval into a sorted non-overlapping list, merging as needed.
`[[1,3],[6,9]] + [2,5] → [[1,5],[6,9]]`
<details><summary>🤔 reveal pattern</summary>

**Three phases: before, absorb, after.** Copy intervals ending before it; absorb overlaps into one; copy the rest.
</details>

#### Merge Intervals
Merge all overlapping intervals.
`[[1,3],[2,6],[8,10]] → [[1,6],[8,10]]`
<details><summary>🤔 reveal pattern</summary>

**Sort by start + sweep.** After sorting, overlap is local: `next.start ≤ current.end`.
</details>

#### Non-Overlapping Intervals
Minimum intervals to remove so none overlap.
<details><summary>🤔 reveal pattern</summary>

**Greedy — keep the earliest END.** Activity selection: earliest-ending interval leaves the most room; count evictions.
</details>

#### Meeting Rooms
Can one person attend every meeting?
<details><summary>🤔 reveal pattern</summary>

**Sort + adjacent overlap check.** Any meeting starting before the previous ends → false.
</details>

#### Meeting Rooms II
Minimum number of conference rooms needed.
`[(0,40),(5,10),(15,20)] → 2`
<details><summary>🤔 reveal pattern</summary>

**Sweep starts vs ends (or min-heap of end times).** Rooms = PEAK simultaneous meetings: +1 per start, −1 per end, track the max.
</details>

#### Minimum Interval to Include Each Query
For each query point, the size of the smallest interval containing it.
<details><summary>🤔 reveal pattern</summary>

**Sort both + min-heap by interval size.** Offline: process queries in order; push started intervals into a size-keyed heap; pop the ones that already ended.
</details>

## Math & Matrix

#### Rotate Image
Rotate an n×n matrix 90° clockwise, in place.
<details><summary>🤔 reveal pattern</summary>

**Transpose + reverse each row.** A rotation is two reflections.
</details>

#### Spiral Matrix
Return all matrix elements in spiral order.
<details><summary>🤔 reveal pattern</summary>

**Four shrinking boundaries.** Walk one edge, shrink that wall, turn; stop when walls cross.
</details>

#### Set Matrix Zeroes
If any cell is 0, zero its whole row and column — in place, O(1) space.
<details><summary>🤔 reveal pattern</summary>

**First row/col as marker space.** The matrix's own first row and column become the flags (plus one variable for their overlap).
</details>

#### Happy Number
Repeatedly replace n with the sum of squared digits. Does it reach 1?
`19 → 82 → 68 → 100 → 1 → true`
<details><summary>🤔 reveal pattern</summary>

**Cycle detection (fast & slow or set).** A repeating sequence hiding a cycle question — same tools as linked-list cycle.
</details>

#### Plus One
Add one to a number stored as an array of digits.
`[9,9] → [1,0,0]`
<details><summary>🤔 reveal pattern</summary>

**Carry from the right.** Only trailing 9s propagate; all 9s → prepend a 1.
</details>

#### Pow(x, n)
Compute x^n in O(log n).
<details><summary>🤔 reveal pattern</summary>

**Fast exponentiation.** x^n = (x^(n/2))² — halve the exponent, square the result. Negative n → 1/x.
</details>

#### Multiply Strings
Multiply two numbers given as strings, no int conversion.
`"12" × "34" → "408"`
<details><summary>🤔 reveal pattern</summary>

**Grade-school digit grid.** digit i × digit j lands at output positions i+j and i+j+1; one carry pass at the end.
</details>

#### Detect Squares
add(point) many times; count(point) asks how many axis-aligned squares use it as a corner.
<details><summary>🤔 reveal pattern</summary>

**Hashmap of point counts + diagonal pairing.** Any stored point DIAGONAL to the query (|dx| = |dy| ≠ 0) proposes a square — multiply the counts of the two remaining corners.
</details>

## Bit Manipulation

#### Single Number
Every element appears twice except one. Find it in O(n) time, O(1) space.
`[4,1,2,1,2] → 4`
<details><summary>🤔 reveal pattern</summary>

**XOR everything.** a ⊕ a = 0 — pairs annihilate; the array XORs down to the loner.
</details>

#### Number of 1 Bits
Count the set bits in an integer.
`11 (1011) → 3`
<details><summary>🤔 reveal pattern</summary>

**n & (n−1) trick.** It deletes the LOWEST set bit; loop until zero.
</details>

#### Counting Bits
For every i in 0..n, output how many set bits i has.
`n=4 → [0,1,1,2,1]`
<details><summary>🤔 reveal pattern</summary>

**DP on bits.** `bits(i) = bits(i >> 1) + (i & 1)` — the smaller answer already exists.
</details>

#### Reverse Bits
Reverse the 32 bits of an unsigned integer.
<details><summary>🤔 reveal pattern</summary>

**Pop one end, push the other, ×32.** `res = (res << 1) | (n & 1); n >>= 1`.
</details>

#### Missing Number
Array holds n distinct numbers from 0..n. Which is missing?
`[3,0,1] → 2`
<details><summary>🤔 reveal pattern</summary>

**XOR indices vs values (or sum formula).** Everything pairs off except the missing number.
</details>

#### Sum of Two Integers
Add two integers without + or −.
<details><summary>🤔 reveal pattern</summary>

**XOR + shifted carry loop.** XOR adds without carrying; `(a & b) << 1` is exactly the carries; repeat until none remain.
</details>

#### Reverse Integer
Reverse an int's digits; return 0 on 32-bit overflow.
`123 → 321   -120 → -21`
<details><summary>🤔 reveal pattern</summary>

**Digit peel + pre-push overflow check.** Pop with `% 10`, push with `× 10` — check the bound BEFORE multiplying.
</details>

## Bonus — beyond the 150

#### Middle of the Linked List
Return the middle node (second middle if even length).
<details><summary>🤔 reveal pattern</summary>

**Fast & slow pointers.** When fast reaches the end, slow stands at the middle.
</details>

#### Squares of a Sorted Array
Sorted array (may contain negatives); return sorted squares in O(n).
`[-4,-1,0,3,10] → [0,1,9,16,100]`
<details><summary>🤔 reveal pattern</summary>

**Two pointers from the ends, fill output backwards.** The largest square sits at one of the two ENDS.
</details>

#### First Missing Positive
Smallest missing positive integer — O(n) time, O(1) space.
`[3,4,-1,1] → 2`
<details><summary>🤔 reveal pattern</summary>

**Cyclic sort / index as hash.** Values 1..n belong at index v−1 → swap everyone home; first index holding the wrong value is the answer.
</details>

#### Kth Smallest in a Sorted Matrix
Rows and columns both sorted; find the kth smallest.
<details><summary>🤔 reveal pattern</summary>

**Heap of row-heads, or binary search on VALUE.** Merge-K-Lists in disguise — or binary search the value range, counting elements ≤ mid per row.
</details>

---

# Mystery set — no categories, like the real thing

The sections above tell you the chapter before you read the problem — the interview won't. These are deliberately shuffled across every family. Read, **name the category AND pattern out loud**, then reveal.

#### Mystery 1
Koko eats banana piles at speed k per hour (max one pile per hour). Minimum k to finish within h hours.
`piles=[3,6,7,11], h=8 → 4`
<details><summary>🤔 reveal</summary>

**Binary Search → on the answer.** "Minimum X that works" + a monotonic works(k) → search the answer space.
*(Problem: Koko Eating Bananas)*
</details>

#### Mystery 2
Group a list of strings so all anagrams end up together.
`["eat","tea","tan"] → [["eat","tea"],["tan"]]`
<details><summary>🤔 reveal</summary>

**Hash Map → canonical key.** "Group by X" = hashmap keyed on sorted letters / count tuple.
*(Problem: Group Anagrams)*
</details>

#### Mystery 3
For each day, how many days until a warmer temperature?
`[73,74,75,71,69,72] → [1,1,3,2,1,0]`
<details><summary>🤔 reveal</summary>

**Monotonic Stack.** "Next greater to the right" — each new value pops and answers every smaller waiting one.
*(Problem: Daily Temperatures)*
</details>

#### Mystery 4
Each minute rot spreads to adjacent fresh oranges in a grid. Minutes until nothing fresh, or −1.
<details><summary>🤔 reveal</summary>

**Graphs → multi-source BFS.** Simultaneous spread = one BFS wavefront; queue levels = minutes.
*(Problem: Rotting Oranges)*
</details>

#### Mystery 5
Rob houses for max loot; adjacent houses trigger the alarm.
`[2,9,8,3,6] → 16`
<details><summary>🤔 reveal</summary>

**1-D DP → take-or-skip.** `dp[i] = max(dp[i-1], dp[i-2] + a[i])`.
*(Problem: House Robber)*
</details>

#### Mystery 6
Given line heights, choose two lines that hold the most water.
`[1,7,2,5,4,7,3,6] → 36`
<details><summary>🤔 reveal</summary>

**Two Pointers → move the shorter wall.** Width only shrinks, so only replacing the shorter wall can help.
*(Problem: Container With Most Water)*
</details>

#### Mystery 7
Find the kth largest element without fully sorting.
`[3,2,1,5,6,4], k=2 → 5`
<details><summary>🤔 reveal</summary>

**Heap / Quickselect.** Only the kth needed → partition toward index n−k (O(n) avg), or a size-k min-heap.
*(Problem: Kth Largest Element in an Array)*
</details>

#### Mystery 8
Given prerequisite pairs, can all courses be finished?
`[[1,0],[0,1]] → false`
<details><summary>🤔 reveal</summary>

**Graphs → topological sort / cycle detection.** Prerequisites = directed edges; "can finish" = "no cycle".
*(Problem: Course Schedule)*
</details>

#### Mystery 9
Smallest substring of s containing every character of t, with multiplicity.
`s="OUZODYXAZV", t="XYZ" → "YXAZ"`
<details><summary>🤔 reveal</summary>

**Sliding Window → need/have counts.** Expand until valid, shrink while still valid, record.
*(Problem: Minimum Window Substring)*
</details>

#### Mystery 10
n+1 integers in range 1..n, one value repeated. Find it — no modifying, O(1) space.
`[1,2,3,2,2] → 2`
<details><summary>🤔 reveal</summary>

**Fast & Slow Pointers → Floyd's cycle on i → nums[i].** Values 1..n = hidden linked list; the duplicate is a cycle entrance.
*(Problem: Find the Duplicate Number)*
</details>

#### Mystery 11
Return all subsets of an array of distinct integers.
`[1,2,3] → 8 subsets`
<details><summary>🤔 reveal</summary>

**Backtracking → take/skip.** ALL configurations wanted → walk the decision tree.
*(Problem: Subsets)*
</details>

#### Mystery 12
Minimum number of conference rooms needed for all meetings.
`[(0,40),(5,10),(15,20)] → 2`
<details><summary>🤔 reveal</summary>

**Intervals → sweep.** Rooms = peak simultaneous meetings: +1 per start, −1 per end, track the max.
*(Problem: Meeting Rooms II)*
</details>

#### Mystery 13
Every element appears twice except one. Find it — O(n) time, O(1) space.
`[4,1,2,1,2] → 4`
<details><summary>🤔 reveal</summary>

**Bit Manipulation → XOR.** Pairs annihilate; the array XORs down to the loner.
*(Problem: Single Number)*
</details>

#### Mystery 14
Find all dictionary words that appear in a letter grid via adjacent cells.
<details><summary>🤔 reveal</summary>

**Trie + Backtracking.** Many words at once → walk grid and trie in lockstep; missing child prunes the branch.
*(Problem: Word Search II)*
</details>

#### Mystery 15
Can the array split into two subsets with equal sums?
`[1,5,11,5] → true`
<details><summary>🤔 reveal</summary>

**DP → 0/1 knapsack.** "Pick a subset hitting a target" = knapsack; target = total/2.
*(Problem: Partition Equal Subset Sum)*
</details>

#### Mystery 16
Merge k sorted linked lists into one.
<details><summary>🤔 reveal</summary>

**Heap → merge of k heads.** Repeatedly need "smallest of k candidates" — mergesort's merge step, k-wide.
*(Problem: Merge K Sorted Lists)*
</details>

#### Mystery 17
Unsorted array; length of the longest run of consecutive integers. Must be O(n).
`[100,4,200,1,3,2] → 4`
<details><summary>🤔 reveal</summary>

**Hash Set → start-of-sequence check.** Sorted-sounding + O(n) demand → set; only count up from x when x−1 is absent.
*(Problem: Longest Consecutive Sequence)*
</details>

#### Mystery 18
Find target in a rotated sorted array in O(log n).
`[4,5,6,7,0,1,2], t=0 → 4`
<details><summary>🤔 reveal</summary>

**Binary Search → pick the sorted half.** One half around mid is always sorted; test whether target lives in it.
*(Problem: Search in Rotated Sorted Array)*
</details>

#### Mystery 19
Length (in edges) of the longest path between any two nodes of a binary tree.
<details><summary>🤔 reveal</summary>

**Trees → DFS return-height, record through-path.** Through a node = left height + right height.
*(Problem: Diameter of Binary Tree)*
</details>

#### Mystery 20
Cheapest route from src to dst using at most k stops (weighted flights).
<details><summary>🤔 reveal</summary>

**Advanced Graphs → Bellman-Ford, k+1 rounds.** The stop limit breaks Dijkstra's greedy proof.
*(Problem: Cheapest Flights Within K Stops)*
</details>

#### Mystery 21
Return the max of every window of size k.
`[1,2,1,0,4,2,6], k=3 → [2,2,4,4,6]`
<details><summary>🤔 reveal</summary>

**Sliding Window + Monotonic Deque.** Keep a decreasing deque of candidates; the front is always the max.
*(Problem: Sliding Window Maximum)*
</details>

#### Mystery 22
String of `(`, `)`, `*` (* = any of the three or empty). Can it be valid?
`"(*))" → true`
<details><summary>🤔 reveal</summary>

**Greedy → range of open counts.** Track [lo, hi] of possible opens; `*` widens both ways.
*(Problem: Valid Parenthesis String)*
</details>

#### Mystery 23
Smallest missing positive integer — O(n) time, O(1) space.
`[3,4,-1,1] → 2`
<details><summary>🤔 reveal</summary>

**Cyclic Sort.** Values 1..n belong at index v−1 → swap everyone home; first squatter is the answer.
*(Problem: First Missing Positive)*
</details>

#### Mystery 24
Digits decode as 1→A … 26→Z. How many ways can the string decode?
`"121" → 3`
<details><summary>🤔 reveal</summary>

**1-D DP → 1- or 2-digit takes.** Fibonacci with guards; "0" is the trap.
*(Problem: Decode Ways)*
</details>

#### Mystery 25
Cars at positions/speeds drive to a target; faster cars stuck behind slower ones merge. How many fleets arrive?
<details><summary>🤔 reveal</summary>

**Sort + Monotonic Stack.** Sort by position; a car merges iff its arrival time ≤ the fleet ahead.
*(Problem: Car Fleet)*
</details>

#### Mystery 26
Do n nodes and this edge list form a valid tree?
<details><summary>🤔 reveal</summary>

**Union-Find.** Tree = n−1 edges + connected + no cycle; a union of already-joined nodes flags the cycle.
*(Problem: Graph Valid Tree)*
</details>

#### Mystery 27
Return the kth smallest value in a binary search tree.
<details><summary>🤔 reveal</summary>

**Trees → in-order traversal.** In-order on a BST is sorted order; stop at the kth visit.
*(Problem: Kth Smallest Element in a BST)*
</details>

#### Mystery 28
Count contiguous subarrays summing to k. Negatives allowed.
`[1,2,3], k=3 → 2`
<details><summary>🤔 reveal</summary>

**Prefix Sum + Hashmap.** Negatives break the window; `pre[j] − pre[i] = k` → "seen pre − k before?"
*(Problem: Subarray Sum Equals K)*
</details>

#### Mystery 29
Reorder L0→L1→…→Ln into L0→Ln→L1→Ln−1→…, in place.
`1→2→3→4 → 1→4→2→3`
<details><summary>🤔 reveal</summary>

**Linked List → composite.** Fast/slow middle + in-place reversal + interleave — three drilled moves chained.
*(Problem: Reorder List)*
</details>

---

# Worked recognitions — watch the script run

### Two Sum
> Q1: find i,j with `a[i]+a[j] = target`. Brute force re-scans for the complement.
> **"I keep searching for the complement" → hash map.** One pass, remember what I've seen.

### Best Time to Buy & Sell Stock
> Q1: `max(prices[j] − prices[i])` for `j > i`.
> Q2: *"if I sell today, best profit = today − cheapest earlier day."*
> Q3: index needs only **min from its left** →
> **"I keep searching for the cheapest earlier buy" → running `min_price`, one pass, O(1) space.**

### Trapping Rain Water
> Q2: *"water on bar i = min(best left wall, best right wall) − height[i]"* ← saying this = 90% solved.
> Q3: needs **both sides** → prefix/suffix max arrays.
> Follow-up "less space?": only `min(left, right)` matters → **two pointers**, advance the shorter wall's side.

### Top K Frequent Elements
> Two shapes stacked: *"I need counts first"* → **hash map**, then *"top K"* → **heap** — or bucket-by-count for O(n).

### Course Schedule
> "Prerequisites" = edges, "can you finish" = is there a cycle →
> **dependency order → topological sort** (or DFS cycle-coloring).

---

# The 60-second decision flowchart

```
                          READ CONSTRAINTS (n tells you the target complexity)
                                        │
        ┌───────────────────────────────┼──────────────────────────────┐
     ARRAY / STRING                TREE / GRAPH                  "ALL ways"? "COUNT ways"?
        │                              │                               │
  sorted? ── yes → two pointers    levels/nearest → BFS          all → backtracking
        │         or binary search  paths/combine → DFS          count/best → DP
  contiguous chunk? → sliding       prerequisites → toposort
        │            window/prefix  connectivity → union-find
  seen before / counts? → hashmap   weighted path → dijkstra
        │
  nearest greater/smaller? → monotonic stack
        │
  top K / streaming best? → heap
        │
  each i needs left context → running var
  each i needs both sides  → prefix/suffix → two pointers
```

---

# In the room: the 5-step interview loop

1. **Restate + constraints.** "n up to 10⁵, so I'm aiming for O(n log n) or better." *(you just showed seniority)*
2. **Say the brute force in one sentence.** It's your safety net AND the pattern often hides in its inefficiency: *"the inner loop re-searches for X"* → hashmap/stack/window replaces it.
3. **Run the 3-question script out loud.** "What does each index need to know?" Interviewers reward hearing this.
4. **Name the pattern, state complexity, THEN code.** The skeleton is muscle memory if you've drilled it.
5. **Test with a tiny example + one edge case** (empty, size 1, all-same, negatives).

If stuck 2+ minutes: **sort the input mentally** (does two pointers unlock?), **try a hashmap** (what would I remember?), **solve size-3 by hand** (the pattern shows itself in the small case).

---

## The glance card — read this in the hallway

```
  sorted            →  two pointers / binary search
  contiguous        →  sliding window / prefix sum
  seen before?      →  hashmap
  nearest greater   →  monotonic stack
  top K             →  heap
  both sides needed →  prefix+suffix → two pointers
  all possibilities →  backtracking
  count/best ways   →  DP
  prerequisites     →  toposort
  connectivity      →  union-find
  levels/nearest    →  BFS        paths/subtrees → DFS
  1..n array trick  →  cyclic sort / XOR
  n ≤ 20 → 2ⁿ ok    n ≤ 10³ → n²    n ≤ 10⁵ → n log n    n ≥ 10⁶ → n or log n
```

You've already solved these problems. The interview isn't asking you to invent — it's asking you to **recognize**. Say the formula, name what each index needs, and the pattern will introduce itself.
