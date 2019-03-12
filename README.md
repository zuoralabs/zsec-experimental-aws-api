# An alternate AWS API that has code completion

**WARNING: experimental code!**

Generates request types with explicit type-annotated params. This lets the
editor's static analysis, pick up parameters and their type annotations for
code completion.


# Use

I have been using this alternate API for quick, small prototypes. The code
completion helps a lot. 

However, I recommend using boto3 directly when shipping, because there is no
guarantee this repo will be maintained or that future changes will be backwards
compatible.
