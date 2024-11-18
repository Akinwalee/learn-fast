from typing import Union, Annotated, List, Optional
from typing_extensions import Annotated
from pydantic import BaseModel
from datetime import datetime

"""
Type Hints X FastAPI

FastAPI relies on type hints for a number of reasons.
Firstly, type hints helps Python to:
- Get helpful editor support.
    This is so because once a variable has an aasociated type hint,
    the text editor understand te data type of the variable and gives suggestions
    of helpful function, methods,a nd other things associated with such data type.
    Similarly, if you're trying to perform an operation that is not supported for 
    such data type, you quickly get hints on that too.
- Help with Type checking.
    Once the expected type hint of a variable is specified, Python cheks to ensure
    that the data that is assigned to such variable is of the specified data type.
    If a different data type is assigned, you get editor hints and Python also throws
    a type error.
- Prevents Type errors
    Type hints helps to prevent common programming errors by enforcing static type checks.
    Think what TypeScript does for JavaScript.

Likewise, type hints helps FastAPI to:
- Define requirements
    FastAPI uses type hints to determine the expected parameters and their types from
    request path and query params, headers, bodies, dependencies, and so on.
- Convert data:
    Type hints help FastAPI to automatocally convert request parameters to the required
    data types.
- Validate data
    FastAPI uses type hints to validate the data coming from each request and generates
    automatic errors that is returned to the client when data is invalid.
- Document the API
    FastAPI use variable annotation and type hints to auto-generate the documention of
    the API using OpenAPI, which is then used by the interactive docs UI.


Declaring Types

Types hints can be Simple or Generic. This classification partially follows the primitive 
and non-primitive data types classification. However, beacuse this is Python, we can more
appropriately map the data types classifications as follows:

Simple -> int, float, bool, bytes, str
    These follow this prototype:
    'variable: type' --Example--> name: str
Generic -> List, Tuple, Set, Dict and none-native types: Union, Optional and so on.
    Generic types are special types that act as a container for other types.
    They follow this prototype:
    'variable: Container[other types]' --Example--> names: List[str]
    - Union and Optional are special containers that allows you to declare variable that
        can be of different possible data types.
        Example: item: Union[str, int, bool] 
            ---> This shows that item can either be a str, int or bool
        - Optional helps to declare a variable that is possibly of type None
            Example: name: Optional[str, None] = None
                ---> This declares a variable name that can be a str or None;
                    and initializes it to None.


Classes as Types

You can use a class as the type of a variable. Suppose the expected type of a variable is
the instance of a class, you can use the class name as the type hint for such variable.
Example:
class Vehicle:
    pass

def get_class(v_name: Vehicle):
    pass

# v_name will be of type Vehicle. That is, it is an instance of the Vehicle class.


Pydantic X FastAPI

FastAPI also uses Pydantic for data validation when creating a class. Pydantic helps to
validate the data type of class variables, used in conjuction with type hints.
Example:
from pydantic import BaseModel
class Vehicle(BaseModel):
    id: int
    name: str
    make: Union[str, int, None]


Metadata Annotation X FastAPI

Using the Annotated class of the typing library, you can provide additional metadat for
a variable. FastAPI uses this annotated metadata to provide additional metadata on how the
application behaves.
Example:
from typing import Annotated
name: Annotated[str, "This is a metadata"]
"""

# Applied Examples

class Product(BaseModel):
    """This uses all the discussed types in a single example"""
    id: int
    name: str
    created_at: Union[datetime, None]
    images: List[str] = []
    reviews: Union[List[str], None] = None
    ratings: Union[str, int, None]

    def __init__(self, name: Annotated[str, "This should be the product name to display"]):
        self.name = name


def capitalize_name(name: Optional[str]):
    print(name.capitalize)