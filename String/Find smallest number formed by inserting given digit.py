# Logic: The main idea is that if N is a positive insert in such a way that 
# the number formed is minimum whereas if N is negative, 
# then insert in X such as the number formed is maximum, ignoring the negative sign. 

# How to do?

# Initialize two variables, say len = length of string N and position = n + 1.
# If N is negative (N[0] = ‘-‘), traverse the string from (n-1)th index to 1th index and check if  N[i] – ‘0’ < X, if true then update position = i.
# If N is positive, traverse the string from (n-1)th index to 0th index and check if  N[i] – ‘0’ > X, if true then update position = i.
# Insert X at index position in N.
# Finally, return the string N.


def MinValue(N, X):
    
	# Variable to store length
	# of string N
	N = list(N);
	ln = len(N)

	# Variable to denote the position
	# where X must be added
	position = ln + 1

	# If the given string N represent
	# a negative value
	if (N[0] == '-'):
	
		# X must be place at the last
		# index where is greater than N[i]
		for i in range(ln - 1, 0, -1):
			if ((ord(N[i]) - ord('0')) < X):
				position = i

	else:
		# For positive numbers, X must be
		# placed at the last index where
		# it is smaller than N[i]
		for i in range(ln - 1, -1, -1):
			if ((ord(N[i]) - ord('0')) > X):
				position = i

	# Insert X at that position
	c = chr(X + ord('0'))

	N.insert(position, c);


	# Return the string
	return ''.join(N)

# Java Code
"""
class Solution {
    public String MinValue(String N, int X) {
        // Variable to store length of string N
        int ln = N.length();

        // Variable to denote the position where X must be added
        int position = ln + 1;

        // If the given string N represents a negative value
        if (N.charAt(0) == '-') {
            // X must be placed at the last index where it is greater than N[i]
            for (int i = ln - 1; i > 0; i--) {
                if ((N.charAt(i) - '0') < X) {
                    position = i;
                }
            }
        } else {
            // For positive numbers, X must be placed at the last index where it is smaller than N[i]
            for (int i = ln - 1; i >= 0; i--) {
                if ((N.charAt(i) - '0') > X) {
                    position = i;
                }
            }
        }

        // Insert X at that position
        char c = (char) (X + '0');
        StringBuilder sb = new StringBuilder(N);
        sb.insert(position, c);

        // Return the string
        return sb.toString();
    }
}
"""

# C++ Code 
"""
#include <string>

using namespace std;

class Solution {
public:
    string MinValue(string N, int X) {
        // Variable to store length of string N
        int ln = N.size();

        // Variable to denote the position where X must be added
        int position = ln + 1;

        // If the given string N represents a negative value
        if (N[0] == '-') {
            // X must be placed at the last index where it is greater than N[i]
            for (int i = ln - 1; i > 0; i--) {
                if ((N[i] - '0') < X) {
                    position = i;
                }
            }
        } else {
            // For positive numbers, X must be placed at the last index where it is smaller than N[i]
            for (int i = ln - 1; i >= 0; i--) {
                if ((N[i] - '0') > X) {
                    position = i;
                }
            }
        }

        // Insert X at that position
        char c = X + '0';
        N.insert(N.begin() + position, c);

        // Return the string
        return N;
    }
};
"""
# Logic: The main idea is that if N is a positive insert in such a way that 
# the number formed is minimum whereas if N is negative, 
# then insert in X such as the number formed is maximum, ignoring the negative sign. 

# How to do?

# Initialize two variables, say len = length of string N and position = n + 1.
# If N is negative (N[0] = ‘-‘), traverse the string from (n-1)th index to 1th index and check if  N[i] – ‘0’ < X, if true then update position = i.
# If N is positive, traverse the string from (n-1)th index to 0th index and check if  N[i] – ‘0’ > X, if true then update position = i.
# Insert X at index position in N.
# Finally, return the string N.


def MinValue(N, X):
    
	# Variable to store length
	# of string N
	N = list(N);
	ln = len(N)

	# Variable to denote the position
	# where X must be added
	position = ln + 1

	# If the given string N represent
	# a negative value
	if (N[0] == '-'):
	
		# X must be place at the last
		# index where is greater than N[i]
		for i in range(ln - 1, 0, -1):
			if ((ord(N[i]) - ord('0')) < X):
				position = i

	else:
		# For positive numbers, X must be
		# placed at the last index where
		# it is smaller than N[i]
		for i in range(ln - 1, -1, -1):
			if ((ord(N[i]) - ord('0')) > X):
				position = i

	# Insert X at that position
	c = chr(X + ord('0'))

	N.insert(position, c);


	# Return the string
	return ''.join(N)

# Java Code
"""
class Solution {
    public String MinValue(String N, int X) {
        // Variable to store length of string N
        int ln = N.length();

        // Variable to denote the position where X must be added
        int position = ln + 1;

        // If the given string N represents a negative value
        if (N.charAt(0) == '-') {
            // X must be placed at the last index where it is greater than N[i]
            for (int i = ln - 1; i > 0; i--) {
                if ((N.charAt(i) - '0') < X) {
                    position = i;
                }
            }
        } else {
            // For positive numbers, X must be placed at the last index where it is smaller than N[i]
            for (int i = ln - 1; i >= 0; i--) {
                if ((N.charAt(i) - '0') > X) {
                    position = i;
                }
            }
        }

        // Insert X at that position
        char c = (char) (X + '0');
        StringBuilder sb = new StringBuilder(N);
        sb.insert(position, c);

        // Return the string
        return sb.toString();
    }
}
"""

# C++ Code 
"""
#include <string>

using namespace std;

class Solution {
public:
    string MinValue(string N, int X) {
        // Variable to store length of string N
        int ln = N.size();

        // Variable to denote the position where X must be added
        int position = ln + 1;

        // If the given string N represents a negative value
        if (N[0] == '-') {
            // X must be placed at the last index where it is greater than N[i]
            for (int i = ln - 1; i > 0; i--) {
                if ((N[i] - '0') < X) {
                    position = i;
                }
            }
        } else {
            // For positive numbers, X must be placed at the last index where it is smaller than N[i]
            for (int i = ln - 1; i >= 0; i--) {
                if ((N[i] - '0') > X) {
                    position = i;
                }
            }
        }

        // Insert X at that position
        char c = X + '0';
        N.insert(N.begin() + position, c);

        // Return the string
        return N;
    }
};
"""
