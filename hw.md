# Python Sets – Homework Set Group Operations

Solve at least 1 question 

## Part A 

For each question: **What is the missing operation (`?`)**

Example:

`{1, 2} ? {3, 4} = {1, 2, 3, 4}`

Answer: `|` , because-  | unifies both sets to one 

`{1, 2} | {3, 4} = {1, 2, 3, 4}`

**Solve:**  

1. `{1, 2} ? {3, 4} = {1, 2, 3, 4}` ----> '|': unifies two sets

2. `{1, 2, 3} ? {3, 4} = {3}`-----------> '&': shows which element aears in both sets

3. `{1, 2, 3, 4} ? {3, 4} = {1, 2}`-----> '-': removes elements that apear in both first and second set

4. `{1, 2, 3} ? {3, 4} = {1, 2, 4}`-----> '^': unifies sets and removes repetetive elements (apeared in both sets)

5. `{1, 2, 3, 4} ? {1, 2} = True`-------> '>=': superset- is {1,2,3,4} a superset of {1,2}? true, because all elements from second set apear in first set 

6. `{1, 2} ? {1, 2, 3, 4} = True`-------> '<=': subset- true because all elements from first set exist in second

7. `{5, 6} ? {6, 7} = {5, 6, 7}`--------> '|': unifies sets, no repetition of elements

8. `{10, 11, 12} ? {12, 13} = {10, 11}`-> '-': removes repetative elements from first set.

## Part B - Bonus

For each question: **What are the two missing operations (`? ?`)**

Example:

`{1, 2} ? {3, 4} ? {2} = {1, 3, 4}`

Answer: `|  -`  , because-  

`{1, 2} | {3, 4} - {2} = {1, 3, 4}`

### You can also add brackets 

Example:  

`{1 2 3} ? {3 4} ? { 2 } = { 2 }`  

Answer: 

`( {1 2 3} - {3 4} ) & { 2 } = { 2 }`    

**Solve:**  

1. `{1, 2} ? {3, 4} ? {2} = {1, 3, 4}`-------------> `{1, 2} ^ {3, 4} ^ {2} = {1, 3, 4}`

2. `{1, 2, 3, 4} ? {3, 4} ? {1, 2} = {1, 2, 3, 4}`-> `{1, 2, 3, 4} | {3, 4} | {1, 2} = {1, 2, 3, 4}` 

3. `{1, 2, 3} ? {2, 3} ? {1, 4} = {2, 3. 4}`-------> `{1, 2, 3} | {2, 3} ^ {1, 4} = {2, 3, 4}`

4. `{1, 2, 3, 4, 5} ? {2, 4} ? {1, 2, 3} = {4, 5}`-> `{1, 2, 3, 4, 5} | {2, 4} - {1, 2, 3} = {4, 5}`

5. `{1, 2, 3, 4} ? {2, 4, 6} ? {2} = {2}`----------> `({1, 2, 3, 4} | {2, 4, 6}) & {2} = {2}`

6. `{1, 2, 3, 4} ? {3, 4, 5} ? {1, 5} = {2, 3, 4}`-> `({1, 2, 3, 4} | {3, 4, 5}) - {1, 5} = {2, 3, 4}`

7. `{1, 2, 3} ^ ({3, 4, 5} | {1, 2, 4}) = {4, 5}` **ETGAR**


**Submission email:** [pythonai211225+pythonx3set2@gmail.com](mailto:pythonai211225+pythonx3set2@gmail.com)
