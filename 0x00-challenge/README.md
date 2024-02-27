## Fix-my-code-0
- Task 0: FizzBuzz

    - Fixed positioning of elif condition.
    - The elif condition for checking multiples of both 3 and 5 should come before the conditions for multiples of 3 and multiples of 5. Initially, it was placed after the condition for multiples of 3, which means the code would never reach that block.

- Task 1: Print square

    - The provided code is using base 16 to parse the string which is used for hexadecimal numbers. In this case we are dealing with decimal numbers. Thus, changing base 16 to base 10 is appropriate.

- Task 2: Sort

    - There are two major issues with this task
        - Logic
          - The `result` array, you should use result.insert(i, i_arg) instead of result.insert(i - 1, i_arg)

          - The use of `if !is_inserted` is unnecessary. This will render the loop to false. Therefore, the correct version is `result << i_arg unless is_inserted`

- Task 3: User password

    - Two potentials issues spotted in line 43 & 57. Line 43 used a single underscore which meant a private attribute for password. The `is_valid_password` function was inaccessible to other functions
- The given code in line 57 was ==> "return hashlib.md5(pwd.encode()).hexdigest().upper() == self.__password".which was comparing `hexdigest().upper()`. I corrected it to `hexdigest().lower()`
 
