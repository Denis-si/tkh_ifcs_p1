# Session 07 Reflection

## Why Lists Beat Variables at Scale

Managing 100 IP addresses as individual variables (e.g., ip1, ip2, ... ip100) is technically possible, but it’s a recipe for what developers call "spaghetti code." Moving them into a List (or Array) transforms that chaotic pile of data into a structured, manageable tool.

Here is why a List wins every time:

1. Scalability and Maintenance
If you use separate variables, adding a 101st IP address requires you to manually create a new variable, update your logic, and potentially rewrite functions. With a List, you simply .append() or .add() the new data. The rest of your code stays exactly the same.

2. The Power of Iteration (Loops)
This is the "killer feature" of Lists. If you want to ping all 100 IP addresses, a List allows you to use a simple loop.

With Variables: You would have to write 100 lines of code—one for each variable.

With a List: You write two lines of code.

3. Native Sorting and Searching
Lists come with built-in "superpowers." If you need to find a specific IP, check for duplicates, or sort them numerically, Lists have methods to do this instantly (like .sort() or .contains()). Performing these tasks on 100 independent variables would require a massive, complex web of if-else statements.

4. Code Readability and Passing Data
Functions (methods) prefer Lists.

The Messy Way: A function that needs all IPs would require 100 different parameters: checkStatus(ip1, ip2, ip3...).

The Clean Way: You pass one single object: checkStatus(myIpList). This makes your code much easier for other humans (and your future self) to read and understand.
