# logic :1)we can append any special value say '#' after each char.
# But this will not work in case, this special char is also a part of string.

# 2) we can add the length of each word with special symbol for encoding.
# this only we did . 
# we can use any encoding method or symbol.

# Note: Given in Q
# 1)strs[i] contains any possible characters out of 256 valid ASCII characters.
#  2)Could you write a generalized algorithm to work on any possible set of characters?

class Codec:
    def encode(self, strs: List[str]) -> str:
        res= ""
        for s in strs:   # adding the len(word) + special symbol + s.
            res+= str(len(s)) + '#' + s
        return res
        

    def decode(self, s: str) -> List[str]:
        res= []
        i= 0  # when we will start searching to the next word
        while i < len(s):
            j= i   # find the number before '#'
            while s[j] != '#':
                j+= 1
            # now we have found one word.
            length= int(s[i:j])   # will give the length of curr word .
            res.append(s[j+1: j+1+length])   # curr word will lie between these.
            i= j + 1 + length    # searching for next word will start from here.
        return res


# My mistake: 
# I tried doing like this:
# Won't work because ":" is also allowed.
# e.g: input => ["tP","8f_f@^","w{=dT(0@:",""]
# output: ["tP","8f_f@^","w{=dT(0@",":"]       != expected(original one)
class Codec:
    def encode(self, strs: List[str]) -> str:
        return "::".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("::")
    

# Javs: Same method
"""
public class Codec {
	// Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s : strs) {
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> ret = new ArrayList<String>();
        int i = 0;
        while(i < s.length()) {
            int slash = s.indexOf('#', i);
            int size = Integer.valueOf(s.substring(i, slash));   # converting string from 'i' to 'slash -1' to integer to find the length pf cur word.
            i = slash + size + 1;
            ret.add(s.substring(slash + 1, i));
        }
        return ret;
    }
}
"""