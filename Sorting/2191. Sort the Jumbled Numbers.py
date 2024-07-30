# Method 1: 
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def translate_integer(num: int) -> int:
            digits = list(str(num))
            for i in range(len(digits)):
                digits[i] = str(mapping[int(digits[i])])
            return int("".join(digits))

        number_mapping = collections.defaultdict(int)
        for num in nums:
            number_mapping[num] = translate_integer(num)
        nums.sort(key = lambda val: number_mapping[val])

        return nums

# java
"""
import java.util.*;

class Solution {

    // Helper function to translate a number based on the mapping
    private int translateInteger(int num, int[] mapping) {
        StringBuilder translated = new StringBuilder();
        String numStr = String.valueOf(num);
        for (char digit : numStr.toCharArray()) {
            translated.append(mapping[digit - '0']);
        }
        return Integer.parseInt(translated.toString());
    }

    public int[] sortJumbled(int[] mapping, int[] nums) {
        // Create a map to store the translated values for each number
        Map<Integer, Integer> numberMapping = new HashMap<>();
        for (int num : nums) {
            numberMapping.put(num, translateInteger(num, mapping));
        }

        // Sort the nums array based on the translated values
        // first convert 'nums' into custom class type from 'int' to 'Integer' then only custom sorting will work.
        Integer[] numsArray = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(numsArray, (a, b) -> numberMapping.get(a) - numberMapping.get(b));

        // Convert the sorted Integer array back to int array
        return Arrays.stream(numsArray).mapToInt(Integer::intValue).toArray();
    }
}
"""

# Method 2: 
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def translate_integer(num: int) -> int:
            if num == 0:  # edge case, we don't want return 0 but mapping value
                return mapping[0]
            res: int = 0
            cur_mult: int = 1  # to construct number we need every time multiple new digit
            while num > 0:
                digit = num % 10
                num //= 10
                res = mapping[digit] * cur_mult + res
                cur_mult *= 10

            return res

        number_mapping: dict[int, int] = {}
        for num in nums:
            number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums