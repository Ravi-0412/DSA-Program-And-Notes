# 1st method: using hashmap like as usual for all problems of this type.
'''
Approach :
1) Here we take i to traverse the list and take  hashmap to store ith number and its index 
2)for each ith element compute  target- numbers[i]
3)if , res_sum is not found in hashmap store this ith element and its index
4) else , return the indices of the pair here we are given to 1 based indices 

Time Complexity : O(n) , n is the length of the list
Space Complexity : O(n) , for Hashmap Storage
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(numbers)):
            rem_sum= target- numbers[i]
            if rem_sum in hashmap:
                return hashmap[rem_sum] +1, i+1
            else:
                hashmap[numbers[i]]= i

'''

# Java Code 
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            int rem_sum = target - numbers[i];
            if (hashmap.containsKey(rem_sum)) {
                return new int[] {hashmap.get(rem_sum) + 1, i + 1};
            } else {
                hashmap.put(numbers[i], i);
            }
        }
        return new int[0];
    }
}


# C++ Code
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> hashmap;
        for (int i = 0; i < numbers.size(); i++) {
            int rem_sum = target - numbers[i];
            if (hashmap.find(rem_sum) != hashmap.end()) {
                return {hashmap[rem_sum] + 1, i + 1};
            } else {
                hashmap[numbers[i]] = i;
            }
        }
        return {};
    }
};

'''

# 2nd method : using two pointer (this q was mainly given because of this)
# vvi basic logic: hmko pointer ko aisa jagah rakhna h jisse hm sure dekh paye ki kis side move karna h.
# Aisa Q like closest pair, minDiff of pairs etc  sbka yhi logic h.

# isliye phle pointer sochna h.
# simpler way to find index of pointers: just keep one pointer at index where you can get the min number 
# and one at index where you can get the maximum number.
# time: O(n), space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        start, end= 0, n-1
        while start < end:  #  start can't be equal to end as we can't use the same ele twice
            
            # in this case our ans will lie before end since array is sorted so incr start will incr the more 
            if numbers[start] + numbers[end] > target:
                    end-= 1
            # in this case our ans will lie after start since array is sorted
            elif numbers[start]+ numbers[end] < target:
                start+= 1
            else:  # we found the target
                return start+1, end+1

'''
C++ Code
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0, end = numbers.size() - 1;
        while (start < end) {
            if (numbers[start] + numbers[end] > target) {
                end--;
            } else if (numbers[start] + numbers[end] < target) {
                start++;
            } else {
                return {start + 1, end + 1};
            }
        }
        return {};
    }
};

Java Code
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0, end = numbers.length - 1;
        while (start < end) {
            if (numbers[start] + numbers[end] > target) {
                end--;
            } else if (numbers[start] + numbers[end] < target) {
                start++;
            } else {
                return new int[] {start + 1, end + 1};
            }
        }
        return new int[0];
    }
}

'''

# Extension: 
# If asked to find the no of such pairs then:
# a) No duplicate element


def count_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0 # # To store the number of valid pairs
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target: # if one pair found 
            count += 1
            left += 1
            right -= 1
        elif current_sum < target: # if pair not found
            left += 1 # target value is greater so increment the left by one because the list is sorted
        else:
            right -= 1 # target value is smaller so decrement the right by one because the list is sorted
    
    return count # return the no of valid pair found 

'''
C++ Code :
int countPairsWithSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1, count = 0;
    while (left < right) {
        int current_sum = arr[left] + arr[right];
        if (current_sum == target) {
            count++;
            left++;
            right--;
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return count;
}

Java Code : 
public int countPairsWithSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1, count = 0;
    while (left < right) {
        int current_sum = arr[left] + arr[right];
        if (current_sum == target) {
            count++;
            left++;
            right--;
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return count;
}

'''

# b) Duplicate allowed

def count_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0 # To store the number of valid pairs
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            if arr[left] == arr[right]:
                # If both pointers are at the same element, count combinations
                num_elements = right - left + 1 # Total elements between left and right
                count += (num_elements * (num_elements - 1)) // 2   # comb(n, 2)
                break # All remaining pairs are already counted, so exit loop
            else:
                # Count occurrences of arr[left] and arr[right]
                left_count = 1
                right_count = 1
                # Count how many times arr[left] is repeated
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left += 1
                    left_count += 1
                #Count how many times arr[right] is repeated    
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right -= 1
                    right_count += 1
                # Total pairs formed by these repeated values
                count += left_count * right_count   # (m*n)
                left += 1 
                right -= 1
        elif current_sum < target:
            left += 1 # target value is greater so increment the left by one because the list is sorted
        else:
            right -= 1 # target value is smaller so decrement the right by one because the list is sorted
    
    return count # return the no of valid pair found 

'''
# C++ Code
int countPairsWithSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1, count = 0;

    while (left < right) {
        int current_sum = arr[left] + arr[right];
        
        if (current_sum == target) {
            if (arr[left] == arr[right]) {
                int num_elements = right - left + 1;
                count += (num_elements * (num_elements - 1)) / 2;
                break;
            } else {
                int left_count = 1, right_count = 1;
                while (left + 1 < right && arr[left] == arr[left + 1]) {
                    left++;
                    left_count++;
                }
                while (right - 1 > left && arr[right] == arr[right - 1]) {
                    right--;
                    right_count++;
                }
                count += left_count * right_count;
                left++;
                right--;
            }
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

# Java Code

public int countPairsWithSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1, count = 0;

    while (left < right) {
        int current_sum = arr[left] + arr[right];

        if (current_sum == target) {
            if (arr[left] == arr[right]) {
                int num_elements = right - left + 1;
                count += (num_elements * (num_elements - 1)) / 2;
                break;
            } else {
                int left_count = 1, right_count = 1;
                while (left + 1 < right && arr[left] == arr[left + 1]) {
                    left++;
                    left_count++;
                }
                while (right - 1 > left && arr[right] == arr[right - 1]) {
                    right--;
                    right_count++;
                }
                count += left_count * right_count;
                left++;
                right--;
            }
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

'''

# c) Given two strictly sorted arrays in ascending order and a target.
# count no of pairs whose sum = target such that one ele is taken from arr1 and other is from arr2.
# Note: strictly sorted => no duplicates

def count_pairs_with_sum(arr1, arr2, target):
    left = 0 #this pointer starts from the starting point of the arr1
    right = len(arr2) - 1 # this pointer starts from the last index of arr2
    count = 0 # To store the number of valid pairs
    
    while left < len(arr1) and right >= 0:
        current_sum = arr1[left] + arr2[right]
        
        if current_sum == target: # if one pair found 
            count += 1
            left += 1
            right -= 1
        elif current_sum < target: 
            left += 1 # target value is greater so increment the left by one because the list is sorted
        else:
            right -= 1 # target value is smaller so decrement the right by one because the list is sorted
    
    return count # return the no of valid pair found 


'''
C++ Code 
int countPairsWithSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1, count = 0;

    while (left < right) {
        int current_sum = arr[left] + arr[right];
        
        if (current_sum == target) {
            if (arr[left] == arr[right]) {
                int num_elements = right - left + 1;
                count += (num_elements * (num_elements - 1)) / 2;
                break;
            } else {
                int left_count = 1, right_count = 1;
                while (left + 1 < right && arr[left] == arr[left + 1]) {
                    left++;
                    left_count++;
                }
                while (right - 1 > left && arr[right] == arr[right - 1]) {
                    right--;
                    right_count++;
                }
                count += left_count * right_count;
                left++;
                right--;
            }
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

Java Code
public int countPairsWithSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1, count = 0;

    while (left < right) {
        int current_sum = arr[left] + arr[right];

        if (current_sum == target) {
            if (arr[left] == arr[right]) {
                int num_elements = right - left + 1;
                count += (num_elements * (num_elements - 1)) / 2;
                break;
            } else {
                int left_count = 1, right_count = 1;
                while (left + 1 < right && arr[left] == arr[left + 1]) {
                    left++;
                    left_count++;
                }
                while (right - 1 > left && arr[right] == arr[right - 1]) {
                    right--;
                    right_count++;
                }
                count += left_count * right_count;
                left++;
                right--;
            }
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

'''

# d) If arrays are sorted but not strictly means duplicate are allowed
def count_pairs_with_sum(arr1, arr2, target):
    left = 0 #this pointer starts from the starting point of the arr1
    right = len(arr2) - 1 # this pointer starts from the last index of arr2
    count = 0 # To store the number of valid pairs
    
    while left < len(arr1) and right >= 0:
        current_sum = arr1[left] + arr2[right]
        
        if current_sum == target: # if one valid pair found
            left_val = arr1[left]
            right_val = arr2[right]
            
            left_count = 0
            right_count = 0
            
            # Count occurrences of the current element in arr1
            while left < len(arr1) and arr1[left] == left_val:
                left_count += 1
                left += 1
            
            # Count occurrences of the current element in arr2
            while right >= 0 and arr2[right] == right_val:
                right_count += 1
                right -= 1
            
            count += left_count * right_count # Total pairs formed by these repeated values
        
        elif current_sum < target: 
            left += 1 # target value is greater so increment the left by one because the list is sorted
        else:
            right -= 1 # target value is smaller so decrement the right by one because the list is sorted
    
    return count # return the no of valid pair found 
'''
C++ Code
int countPairsWithSum(vector<int>& arr1, vector<int>& arr2, int target) {
    int left = 0, right = arr2.size() - 1, count = 0;

    while (left < arr1.size() && right >= 0) {
        int current_sum = arr1[left] + arr2[right];

        if (current_sum == target) {
            int left_val = arr1[left], right_val = arr2[right];
            int left_count = 0, right_count = 0;

            while (left < arr1.size() && arr1[left] == left_val) {
                left_count++;
                left++;
            }
            while (right >= 0 && arr2[right] == right_val) {
                right_count++;
                right--;
            }

            count += left_count * right_count;
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

Java Code
public int countPairsWithSum(int[] arr1, int[] arr2, int target) {
    int left = 0, right = arr2.length - 1, count = 0;

    while (left < arr1.length && right >= 0) {
        int current_sum = arr1[left] + arr2[right];

        if (current_sum == target) {
            int left_val = arr1[left], right_val = arr2[right];
            int left_count = 0, right_count = 0;

            while (left < arr1.length && arr1[left] == left_val) {
                left_count++;
                left++;
            }
            while (right >= 0 && arr2[right] == right_val) {
                right_count++;
                right--;
            }

            count += left_count * right_count;
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return count;
}

'''

# Note vvi: whenever you get this type of Q then try to fix one ele somehow 
# and find the other two ele using "Two sum" for sorted/unsorted array.
# Just try to reduce into "two sum" problem.
# e.g: "15. 3Sum", "18. 4Sum", "Count Triplets"


# Note: where to use "Two pointer"?
# 1) where you see array is sorted then once must think about "Two Pointer" or "Binary Search".
# 2) when you have to solve in-place , then think if we can do by "Two Pointer".
# vvi: For in-place, mostly a) Think about swapping elements b) Think of "Two Pointer". 
# these two method work in most of the cases where we are asked to do in-place.

