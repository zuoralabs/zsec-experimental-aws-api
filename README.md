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


# boto3_nice

A nicer way to use boto3. By using `NewType`, you can do the following:
~~~python
from typing import NewType
try:
    import boto3_nice as boto3
except ImportError:
    import boto3

s3_service_name = NewType('s3_service_name', str)('s3')
s3 = boto3.Session().client(s3_service_name, region_name='us-east-1')
# now you will get code completion for `s3`. Try completing on e.g. `s3.head_`.
~~~
This will run whether or not you actually have `boto3_nice` installed. Of course
the type hinting only works if you have `boto3_nice`.
Type hinting is handled by applying `typing.overload` to `boto3_nice.Session.client`
and using `typing.NewType` in the overloaded type annotations.

If boto3_nice is definitely installed, then the client can be created more simply:
~~~python
import boto3_nice

s3 = boto3_nice.Session().s3_client(region_name='us-east-1')
~~~


## Why not ...?

By using `typing_extensions.Literal`, it would be possible provide `.pyi` files
that would allow type hinting for `boto3` without any additional modification.

However, it looks like `Literal` is not supported in latest IntelliJ
Idea/Pycharm as of 2019/08/29.
