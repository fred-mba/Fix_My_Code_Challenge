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

    - Two potentials issues spotted at line 43 & 57. At line 43, use of a single underscore would mean a private attribute for password. This would otherwise prevent reuse of stored values of password in this `is_valid_password` function
- At line 57, this was provided ==> "return hashlib.md5(pwd.encode()).hexdigest().upper() == self.__password".
- Here the method currently compares `hexdigest().upper()` which should be `hexdigest().lower()`.
 
