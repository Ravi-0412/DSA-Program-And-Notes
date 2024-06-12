class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)
        freq = Counter(arr1)
        notPresent = []
        for num in arr1:
            if num not in arr2:
                notPresent.append(num)
        ans = []
        for num in arr2:
            ans += [num]*freq[num]
        ans += sorted(notPresent)
        return ans


# Method 2: Countimng sort
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0] * 1001
        for n in arr1:
            cnt[n] += 1
        
        i = 0
        for n in arr2:
            while cnt[n] > 0:
                arr1[i] = n
                i += 1
                cnt[n] -= 1
        
        for n in range(len(cnt)):
            while cnt[n] > 0:
                arr1[i] = n
                i += 1
                cnt[n] -= 1
        
        return arr1


# java
""""
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] cnt = new int[1001];
        for(int n : arr1) cnt[n]++;
        int i = 0;
        for(int n : arr2) {
            while(cnt[n]-- > 0) {
                arr1[i++] = n;
            }
        }
        for(int n = 0; n < cnt.length; n++) {
            while(cnt[n]-- > 0) {
                arr1[i++] = n;
            }
        }
        return arr1;
    }
}
"""