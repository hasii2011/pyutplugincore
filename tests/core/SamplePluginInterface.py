
from logging import Logger
from logging import getLogger

from core.PluginInterface import PluginInterface

from core.types.PluginDataTypes import PluginDescription
from core.types.PluginDataTypes import PluginExtension
from core.types.PluginDataTypes import FormatName

from core.IMediator import IMediator
from core.types.InputFormat import InputFormat
from core.types.OutputFormat import OutputFormat
from core.types.PluginDataTypes import PluginName


SAMPLE_PLUGIN_NAME: PluginName        = PluginName('Sample Plugin')
SAMPLE_FORMAT_NAME: FormatName        = FormatName('Unspecified Plugin Name')
SAMPLE_EXTENSION:   PluginExtension   = PluginExtension('sample')
SAMPLE_DESCRIPTION: PluginDescription = PluginDescription('Unspecified Plugin Description')


class SamplePluginInterface(PluginInterface):
    """
    TODO make this a Sample Tool Plugin
    """

    def __init__(self, mediator: IMediator):

        super().__init__(mediator)

        self.logger: Logger = getLogger(__name__)

        self._name         = SAMPLE_PLUGIN_NAME
        self._author       = 'Ozzee D. Gato'
        self._version      = '1.0'
        self._inputFormat  = InputFormat(formatName=SAMPLE_FORMAT_NAME, extension=SAMPLE_EXTENSION, description=SAMPLE_DESCRIPTION)
        self._outputFormat = OutputFormat(formatName=SAMPLE_FORMAT_NAME, extension=SAMPLE_EXTENSION, description=SAMPLE_DESCRIPTION)
