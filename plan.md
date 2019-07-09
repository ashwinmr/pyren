# Overview

pyren should be a general tool for renaming files.
It should use regex to get the files of interest and a regex pattern to determine their new name.

# Features

pyren shall have a command line interface

pyren should show the expected result without execution and ask for confirmation before actual renaming.


## Examples

Add postfix to files

```
pyren "test(.*).yaml" "test$1_fc.yaml"
```
