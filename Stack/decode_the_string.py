"""Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
Note: The test cases are generated so that the length of the output string will never exceed 105 ."""

class Solution:
    def decodeString(s: str) -> str:
        st = []
    
        # Traverse the input string
        for i in range(len(s)):
            # Push characters into the stack until ']' is encountered
            if s[i] != ']':
                st.append(s[i])
            # Decode when ']' is found
            else:
                temp = []
            
                # Pop characters until '[' is found
                while st and st[-1] != '[':
                    temp.append(st.pop())
                temp.reverse()  # Reverse extracted string
                # Remove '[' from the stack
                st.pop()

                num = []
                # Extract the number (repetition count) from the stack
                while st and st[-1].isdigit():
                    num.insert(0, st.pop())

                # Convert extracted number to integer
                number = int("".join(num))
                repeat = "".join(temp) * number  # Repeat the extracted string 'number' times
            
                # Push the expanded string back onto the stack
                st.extend(repeat)

        # Pop all characters from stack to form the final result
        return "".join(st)