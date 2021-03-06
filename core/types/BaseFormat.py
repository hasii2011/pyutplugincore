
from core.types.PluginDataTypes import PluginDescription
from core.types.PluginDataTypes import PluginExtension
from core.types.PluginDataTypes import FormatName

from core.exceptions.InvalidPluginExtensionException import InvalidPluginExtensionException
from core.exceptions.InvalidPluginNameException import InvalidPluginNameException

DOT:                str = '.'
SPECIAL_CHARACTERS: str = '!@#$%^&*_+-=[]{};:,.<>?/|\'\"'


class BaseFormat:
    """
    Provides the basic capabilities;  Should not be directly instantiated;
    TODO:  Figure out how to prevent that
    """
    def __init__(self, formatName: FormatName, extension: PluginExtension, description: PluginDescription):

        if self.__containsSpecialCharacters(formatName):  # TODO Must be a better way
            raise InvalidPluginNameException(f'{formatName}')

        if DOT in extension:             # TODO when internet back up do not this method
            raise InvalidPluginExtensionException(f'{extension}')

        self._name:        FormatName        = formatName
        self._extension:   PluginExtension   = extension
        self._description: PluginDescription = description

    @property
    def formatName(self) -> FormatName:
        """
        No special characters allowed

        Returns: The Plugin's name
        """
        return self._name

    @property
    def extension(self) -> PluginExtension:
        """
        Returns: The file name extension (w/o the leading dot '.')
        """
        return self._extension

    @property
    def description(self) -> PluginDescription:
        """
        Returns: The textual description of the plugin format
        """
        return self._description

    def __containsSpecialCharacters(self, name: FormatName) -> bool:
        for special in SPECIAL_CHARACTERS:
            if special in name:
                return True
        return False
