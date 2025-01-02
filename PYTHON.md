1. Contains Duplicate
```python
# Solution 1: Using HashSet
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Solution 2: Using HashSet with manual tracking
def containsDuplicate2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Variation: Find duplicates within k distance
def containsNearbyDuplicate(nums, k):
    window = {}
    for i, num in enumerate(nums):
        if num in window and i - window[num] <= k:
            return True
        window[num] = i
    return False
```

2. Valid Anagram
```python
# Solution 1: Using Sorting
def isAnagram1(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Solution 2: Using HashMap
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

# Variation: Group Strings by Anagram Index
def groupAnagramIndices(words):
    anagram_map = {}
    
    for i, word in enumerate(words):
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(i)
        else:
            anagram_map[sorted_word] = [i]
    
    return list(anagram_map.values())
```

3. Two Sum
```python
# Solution 1: Using HashMap
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Variation 1: Two Sum II (sorted array)
def twoSum2(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Variation 2: Find all pairs that sum to target
def findAllPairs(nums, target):
    pairs = []
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            for j in num_map[complement]:
                pairs.append([j, i])
        if num in num_map:
            num_map[num].append(i)
        else:
            num_map[num] = [i]
    return pairs
```

4. Group Anagrams
```python
from collections import defaultdict

# Solution 1: Using Sorted String as Key
def groupAnagrams1(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    return list(anagram_map.values())

# Solution 2: Using Character Count as Key
def groupAnagrams2(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        anagram_map[tuple(count)].append(s)
    return list(anagram_map.values())

# Variation: Group Anagrams by Size
def groupAnagramsBySize(strs):
    size_groups = defaultdict(list)
    for group in groupAnagrams1(strs):
        size_groups[len(group)].append(group)
    return dict(size_groups)
```

5. Top K Frequent Elements
```python
from collections import Counter
import heapq

# Solution 1: Using Heap
def topKFrequent1(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Solution 2: Using Bucket Sort
def topKFrequent2(nums, k):
    count = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        bucket[freq].append(num)
    
    flat_list = []
    for i in range(len(bucket)-1, -1, -1):
        flat_list.extend(bucket[i])
    
    return flat_list[:k]

# Variation: Top K Frequent Pairs
def topKFrequentPairs(nums, k):
    pair_count = Counter((nums[i], nums[i+1]) for i in range(len(nums)-1))
    return heapq.nlargest(k, pair_count.keys(), key=pair_count.get)
```

6. Encode and Decode Strings
```python
class Codec:
    # Solution 1: Length Prefixing
    def encode1(self, strs):
        return ''.join(f"{len(s)}#{s}" for s in strs)
    
    def decode1(self, s):
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result
    
    # Solution 2: Using Delimiter with Escaping
    def encode2(self, strs):
        return ','.join(s.replace(',', ',,') for s in strs)
    
    def decode2(self, s):
        return [part.replace(',,', ',') for part in s.split(',')]
```

7. Product of Array Except Self
```python
# Solution 1: Using Left and Right Products
def productExceptSelf1(nums):
    n = len(nums)
    output = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    # Calculate right products
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# Solution 2: Using Division (if no zeros)
def productExceptSelf2(nums):
    total_product = 1
    for num in nums:
        if num != 0:
            total_product *= num
    
    return [total_product // num if num != 0 else 0 for num in nums]

# Variation: Product of K Numbers Except Self
def productExceptSelfK(nums, k):
    n = len(nums)
    output = []
    for i in range(n):
        product = 1
        for j in range(max(0, i-k), min(n, i+k+1)):
            if i != j:
                product *= nums[j]
        output.append(product)
    return output
```

8. Longest Consecutive Sequence
```python
# Solution 1: Using HashSet
def longestConsecutive1(nums):
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Solution 2: Using Union Find
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def longestConsecutive2(nums):
    if not nums:
        return 0
    
    uf = UnionFind()
    for num in nums:
        uf.find(num)
        if num - 1 in uf.parent:
            uf.union(num, num - 1)
        if num + 1 in uf.parent:
            uf.union(num, num + 1)
    
    sequences = {}
    for num in nums:
        parent = uf.find(num)
        sequences[parent] = sequences.get(parent, 0) + 1
    
    return max(sequences.values()) if sequences else 0

# Variation: Find All Consecutive Sequences
def findAllConsecutiveSequences(nums):
    num_set = set(nums)
    sequences = []
    
    while num_set:
        num = num_set.pop()
        current_sequence = [num]
        
        # Check consecutive numbers in both directions
        next_num = num + 1
        while next_num in num_set:
            current_sequence.append(next_num)
            num_set.remove(next_num)
            next_num += 1
        
        prev_num = num - 1
        while prev_num in num_set:
            current_sequence.insert(0, prev_num)
            num_set.remove(prev_num)
            prev_num -= 1
        
        sequences.append(current_sequence)
    
    return sequences
```

These solutions cover various approaches and variations for each problem. Key points to remember:
1. Always consider time and space complexity
2. Think about edge cases
3. Consider different data structures (HashSet, HashMap, Heap)
4. Look for opportunities to optimize
5. Consider the trade-offs between different approaches

Practice these variations to build a strong understanding of array and hashing problems. They often appear in interviews with slight modifications, so understanding the core concepts is crucial.


---


Here are **10 practice problems** to strengthen your skills in using **hashmaps, lists, sets, and dictionaries**, with a focus on coding speed, logic building, and typing practice.

---

### **Hashmap Problems**
1. **Frequency Counter**:  
   Write a function to count the frequency of each character in a string using a hashmap.  
   ```python
   # Input: "abracadabra"
   # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
   ```

2. **Two-Sum Problem**:  
   Given an array of integers, return indices of two numbers that add up to a target. Use a hashmap to store seen numbers for efficient lookup.  
   ```python
   # Input: nums = [2, 7, 11, 15], target = 9
   # Output: [0, 1]
   ```

3. **Group Anagrams**:  
   Write a function to group anagrams together from a list of strings using a hashmap.  
   ```python
   # Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
   # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
   ```

---

### **List Problems**
4. **Rotate a List**:  
   Write a function to rotate a list to the right by `k` steps.  
   ```python
   # Input: nums = [1, 2, 3, 4, 5], k = 2
   # Output: [4, 5, 1, 2, 3]
   ```

5. **Remove Duplicates**:  
   Remove duplicates from a list while maintaining the order.  
   ```python
   # Input: [1, 2, 2, 3, 4, 4, 5]
   # Output: [1, 2, 3, 4, 5]
   ```

6. **Find Intersection of Two Lists**:  
   Write a function to find the intersection of two lists.  
   ```python
   # Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
   # Output: [2]
   ```

---

### **Set Problems**
7. **Find Missing Number**:  
   Given a list of numbers from `1` to `n` with one missing, find the missing number using a set.  
   ```python
   # Input: [1, 2, 4, 6, 3, 7, 8]
   # Output: 5
   ```

8. **Unique Elements**:  
   Write a function to return only the unique elements from a list using a set.  
   ```python
   # Input: [1, 2, 2, 3, 4, 4, 5]
   # Output: [1, 3, 5]
   ```

---

### **Dictionary Problems**
9. **Word Count in a Sentence**:  
   Write a function to count the frequency of each word in a sentence using a dictionary.  
   ```python
   # Input: "the quick brown fox jumps over the lazy dog"
   # Output: {'the': 2, 'quick': 1, 'brown': 1, ...}
   ```

10. **Invert a Dictionary**:  
    Write a function to invert a dictionary, swapping keys and values.  
    ```python
    # Input: {'a': 1, 'b': 2, 'c': 3}
    # Output: {1: 'a', 2: 'b', 3: 'c'}
    ```

---
Combine these data structures in one program:
- Use a hashmap to store frequencies.
- Use a list to sort results.
- Use a set to find unique items.
- Use a dictionary to map each unique frequency to corresponding values.

This ensures you practice all concepts in one exercise.
