# rootchecker
Simple tool to check if android device is rooted


## Install
```
pip install rootchecker
```

## How to use

```python
>>> from rootchecker import rootchecker

>>> rootchecker.check_root()
{'magisk': True, 'root': True, 'su_binary': True}
```

## Example

```python
from rootchecker import rootchecker

client = rootchecker.check_root()

if client["root"] == True:
   print("Your device is rooted!")
else:
   print("Your device is not rooted.")
