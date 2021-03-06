from typing import Union

from miniogl.DiagramFrame import DiagramFrame
from ogl.OglLink import OglLink

from ogl.OglObject import OglObject

from plugins.common.Types import OglClasses


class IMediator:
    """
    This the interface specification that allows the plugins to manipulate the Pyut UML Frame
    The Pyut application must implement this
    """
    def __init__(self, currentDirectory: str, umlFrame: DiagramFrame):

        self._umlFrame:         DiagramFrame = umlFrame
        self._currentDirectory: str          = currentDirectory

    @property
    def currentDirectory(self) -> str:
        return self._currentDirectory

    @currentDirectory.setter
    def currentDirectory(self, theNewValue: str):
        self._currentDirectory = theNewValue

    @property
    def umlFrame(self) -> DiagramFrame:
        return self._umlFrame

    @property
    def selectedOglObjects(self) -> OglClasses:
        return self._umlFrame.GetSelectedShapes()

    def refreshFrame(self):
        self._umlFrame.Refresh()

    def selectAllOglObjects(self):
        pass

    def deselectAllOglObjects(self):
        self._umlFrame.DeselectAllShapes()

    def addShape(self, shape: Union[OglObject, OglLink]):

        diagram = self._umlFrame.GetDiagram()
        diagram.AddShape(shape)
