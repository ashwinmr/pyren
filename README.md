# pyren
Program for renaming files

# Description
pyren takes a regex pattern for filenames and a regex pattern for new filenames and renames the files

# Install
```
git clone git@github.com:ashwinmr/pyren.git
cd pyren
sudo -H pip install -r requirements.txt
sudo -H python setup.py install
```

# Usage
```
pyren <"old_filename_pattern"> <"new_filename_pattern"> [ -d <path/to/directory>]
```
The following flags are supported:
- -i - ignore case
- -y - Don't ask for confirmation

## Examples
Example 1: Basic rename
```
pyren "old.txt" "new.txt"
```

Example 2: Rename keeping extension
```
pyren "old(.*)" "new\\1"
```
The `\` is needed to escape the `\` sign.