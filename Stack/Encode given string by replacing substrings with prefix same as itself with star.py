def compress(s: str) -> str:
    # Stack to store parts of the string that will be replaced by '*'
    st = []

    # Length of the input string
    N = len(s)

    # Initialize pointers: i for the start of the string, and j for the midpoint
    i = 0
    j = N // 2  # Start j at the half length of the string

    # Loop until j (midpoint) reaches 0
    while j > 0:
        # Set the midpoint
        mid = j

        # Reset i to 0 to compare from the start of the string
        i = 0
        
        # Compare the first half of the string with the second half
        # Continue while characters match and i is within the first half (mid)
        while i < mid and s[i] == s[j]:
            i += 1
            j += 1

        # If we found a matching substring (i == mid),
        # compress the string by reducing it to the matching prefix
        if i == mid:
            # Push the remaining unmatched part of the string onto the stack
            st.append(s[j:N])

            # Update the string to only the matching prefix
            s = s[0:i]

            # Update the length of the string to the length of the matching prefix
            N = mid

            # Set j to the midpoint of the new (shortened) string
            j = N // 2
        else:
            # If the substrings did not match, decrease j to try a smaller substring
            j = mid - 1

    # Reconstruct the compressed string using the stack
    # Pop elements from the stack, prepend '*' to them, and append to the result string
    while len(st) != 0:
        # Concatenate the current string with '*' and the last element from the stack
        s = s + '*' + st.pop()

    return s

str1 = "zzzzzzz"
print(compress(str1))  # Expected output: "z*z*z"

str2 = "ababcababcd"
print(compress(str2))  # Expected output: "ab*c*d"


# Java
"""
import java.util.Stack;

public class StringCompressor {

    public static String compress(String str) {
        // Stack to store parts of the string that will be replaced by '*'
        Stack<String> st = new Stack<>();

        // Length of the input string
        int N = str.length();

        // Initialize pointers: i for the start of the string, and j for the midpoint
        int i = 0;
        int j = N / 2;  // Start j at the half length of the string

        // Loop until j (midpoint) reaches 0
        while (j > 0) {
            // Set the midpoint
            int mid = j;

            // Reset i to 0 to compare from the start of the string
            i = 0;

            // Compare the first half of the string with the second half
            // Continue while characters match and i is within the first half (mid)
            while (i < mid && str.charAt(i) == str.charAt(j)) {
                i++;
                j++;
            }

            // If we found a matching substring (i == mid),
            // compress the string by reducing it to the matching prefix
            if (i == mid) {
                // Push the remaining unmatched part of the string onto the stack
                st.push(str.substring(j, N));

                // Update the string to only the matching prefix
                str = str.substring(0, i);

                // Update the length of the string to the length of the matching prefix
                N = mid;

                // Set j to the midpoint of the new (shortened) string
                j = N / 2;
            } else {
                // If the substrings did not match, decrease j to try a smaller substring
                j = mid - 1;
            }
        }

        // Reconstruct the compressed string using the stack
        // Pop elements from the stack, prepend '*' to them, and append to the result string
        while (!st.isEmpty()) {
            // Concatenate the current string with '*' and the last element from the stack
            str = str + "*" + st.pop();
        }

        return str;
    }

    public static void main(String[] args) {
        String str1 = "zzzzzzz";
        System.out.println(compress(str1));  // Expected output: "z*z*z"

        String str2 = "ababcababcd";
        System.out.println(compress(str2));  // Expected output: "ab*c*d"
    }
}
"""

