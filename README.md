# My leetcode solutions

## Workflow Using [leetcode-cli](https://skygragon.github.io/leetcode-cli/)

### Install leeetcode-cli
```bash
$ npm install -g leetcode-cli
```

### Apply user config
```bash
$ ln -s leetcode/config.json ~/.lc/config.json
```

### Random pick problem

```bash
# pick easy
$ leetcode show -q eL

# pick medium
$ leetcode show -q mL

# pick hard
$ leetcode show -q hL
```

# Generate source file and open in editor

```bash
$ leetcode show [problem] -g -e
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

### Submit

```bash
$ leetcode submit ./two-sum.cpp

  ✔ Accepted
  ✔ 16/16 cases passed (12 ms)
  ✔ Your runtime beats 49.89 % of cpp submissions
```


