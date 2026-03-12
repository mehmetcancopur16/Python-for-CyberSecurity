# Step 5: Data Structures - Lists & Tuples

When you are scanning a network, you rarely have just one target. You have hundreds. We need data structures to hold multiple items.



## Lists `[]`
Lists are ordered, changeable (mutable), and allow duplicate values. You can add, remove, and modify items after the list is created.
* *Use Case:* Storing a dynamic list of discovered IP addresses or open ports.

## Tuples `()`
Tuples are ordered but **unchangeable (immutable)**. Once you create a tuple, you cannot modify it.
* *Use Case:* Storing fixed configurations that should never be altered accidentally by your script (e.g., target server coordinates: IP and Port).
