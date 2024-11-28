# Each Python file contains the answer to a specific question.

### Question for test_1.py 

Create ‘accum’ function and return value

Examples:

    accum("abcd") -> "A-Bb-Ccc-Dddd"

    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

    accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a-z and A-Z.


### Question for test_2.py 

Write function for reverse string which parsed in function without using list built-in method

Examples:

    reverse_string("ABCD1234") -> "4321DCBA


### Question for test_3.py 

Write function for reverse number (integer) which parsed in function without convert to string or using list built-in method

Input will always be an integer which greater than 0

Examples:

    reverse_num(1234) -> 4321   # return int
    reverse_num(1) -> 1   # return int
    reverse_num(4444) -> 4444   # return int
    reverse_num(0) -> 0   # return int



### Question for test_4.py 

You will be given an array of strings. The words in the array should mesh together where one or more letters at the end of one word will have the same letters (in the same order) as the next word in the array. But, there are times when all the words won't mesh.

#### Examples of meshed words:

    "apply" and "plywood" (word "ply")

    "apple" and "each"  (word "e")

    "behemoth" and "mother" (word "moth")

#### Examples of words that do not mesh:

    "apply" and "playground"

    "apple" and "peggy"

    "behemoth" and "mathematics"

If all the words in the given array mesh together, then your code should return the meshed letters in a string. 
- You should return the longest common substring. 
- You won't know how many letters the meshed words have in common, but it will be at least one.

If any pair of consecutive words fails to mesh, then return `"failed to mesh"`.

**Input:** An array of strings. There will always be at least two words in the input array.

**Output:** Either a string of letters that mesh the words together or the string "failed to mesh".

#### Example 1:

    ["allow", "lowering", "ringmaster", "terror"] -> "lowringter"

because:
- the letters `"low"` in the first two words mesh together
- the letters `"ring"` in the second and third word mesh together
- the letters `"ter"` in the third and fourth words mesh together.

#### Example 2:
    
    ["kingdom", "dominator", "notorious", "usual", "allegory"] -> "failed to mesh"

Although the words `"dominator"` and `"notorious"` share letters in the same order, the last letters of the first word don't mesh with the first letters of the second word.

