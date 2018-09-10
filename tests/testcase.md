## Count Unique

| Test case           | Case   | Return |
| ---                 | ---    | ---      |
| None    | None | TypeError |
| Empty list | [ ]  | 0  |
| Multiple items, many times  |  ['a', 'b', 'b', 'b', 'a', 'c', 'c']  | 3 |
| Add none in list  | ['a', 'a', 'a', 'a', None] | 2 |

## Binary Search

| Test case           | Case   | Return |
| ---                 | ---    | ---      |
| None    |  [None] search "None" | TypeError |
| Empty | [' ', 'e', 'f', 'u', 'l', 't'] search ' ' | 0  |
| Character | ['d', 'e', 'f', 'u', 'l', 't'] search "f" | 2 |
| Incorrect binary search | ['d', 'e', 'f', 'u', 'l', 't']  search "a" | -1 |
| Numbers | [7, 3, 8, 1, 5] search 3 | 1 |
