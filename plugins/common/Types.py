
from typing import cast
from typing import Dict
from typing import List
from typing import NewType

from dataclasses import dataclass

from ogl.OglClass import OglClass
from pyutmodel.PyutClass import PyutClass
from pyutmodel.PyutLink import PyutLink

from plugins.common.ElementTreeData import ElementTreeData

ClassTree = NewType('ClassTree', Dict[str, ElementTreeData])    # string is ClassName
PyutLinks = NewType('PyutLinks', List[PyutLink])


@dataclass
class ClassPair:

    pyutClass: PyutClass = None
    oglClass:  OglClass  = cast(OglClass, None)