
## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature


```python

def grammmar_checker(text):
    """verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
    Params: string
    Returns: true or false. 
    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a sentence with that begins with a capitalised word and ends with a full stop, the function returns True
"""
 grammmar_checker("Hello world.") => True

"""
Given a sentence with that DOES NOT begins with a capitalised word but ends with a full stop, the function returns False
"""
 grammmar_checker("hello world.") => False

"""
Given a sentence with that begins with a capitalised word but DOES NOT ends with a full stop, the function returns False
"""
 grammmar_checker("Hello world") => False

"""
Given a sentence with that begins with a capitalised word and ends with an exclamation mark (sentence-ending punctuation), the function returns True
"""
 grammmar_checker("Hello world!") => True

"""
Given a sentence with that begins with a capitalised word and ends with a question mark (sentence-ending punctuation), the function returns True
"""
 grammmar_checker("Hello world?") => True

"""
Given a sentence with that begins with a capitalised word and ends with a comma ( non sentence-ending punctuation), the function returns False
"""
 grammmar_checker("Hello world,") => False

"""
Given an empty string, the function returns True
"""
 grammmar_checker("") => False

"""
Given a None value
It throws an error
"""
grammer_checker(None) throws an error
```

