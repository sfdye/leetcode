# My leetcode solutions

## Workflow

Using [leetcode-cli](https://skygragon.github.io/leetcode-cli/)

### Random pick problem and generate the source file

```bash
$ leetcode show -q eL -g -l python3
```

### Submit

```bash
$ leetcode submit ./two-sum.cpp

  ✔ Accepted
  ✔ 16/16 cases passed (12 ms)
  ✔ Your runtime beats 49.89 % of cpp submissions
```

### Run tests

```bash
$ leetcode test ./two-sum.cpp -t '[3,2,4]\n7'

Input data:
[3,2,4]
7

Actual
    ✔ runtime: 0 ms
    ✘ answer: [1,2]
    ✔ output:

Expected
    ✔ runtime: 0 ms
    ✔ answer: [0,2]
    ✔ output:
```
