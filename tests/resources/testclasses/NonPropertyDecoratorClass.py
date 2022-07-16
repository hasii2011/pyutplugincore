
from typing import Any

from abc import ABCMeta
from abc import abstractmethod

from logging import Logger
from logging import getLogger
from typing import List

UmlLineDefinition = List[str]


class NonPropertyDecoratorClass(metaclass=ABCMeta):

    clsLogger: Logger = getLogger(__name__)

    def __init__(self, docMaker: Any):
        self._docMaker:       Any = docMaker

    @abstractmethod
    def draw(self, lineDefinition: UmlLineDefinition):
        pass
