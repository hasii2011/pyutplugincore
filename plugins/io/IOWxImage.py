
from typing import cast

from logging import Logger
from logging import getLogger

# noinspection PyProtectedMember
from wx._core import BitmapType

from wx import Bitmap
from wx import ClientDC
from wx import Image
from wx import MemoryDC
from wx import NullBitmap
from wx import OK
from wx import ScrolledWindow

from core.IMediator import IMediator
from core.IOPluginInterface import IOPluginInterface

from core.types.InputFormat import InputFormat
from core.types.OutputFormat import OutputFormat
from core.types.PluginDataTypes import FormatName
from core.types.PluginDataTypes import PluginDescription
from core.types.PluginDataTypes import PluginExtension
from core.types.PluginDataTypes import PluginName

from plugins.common.Types import OglObjects
from plugins.io.wximage.DlgWxImageOptions import DlgWxImageOptions

from plugins.io.wximage.WxImageFormat import WxImageFormat

FORMAT_NAME:        FormatName = FormatName('Wx Image')
PLUGIN_EXTENSION:   PluginExtension = PluginExtension('png')
PLUGIN_DESCRIPTION: PluginDescription = PluginDescription('png, bmp, gif, or jpg')


class IOWxImage(IOPluginInterface):

    def __init__(self, mediator: IMediator):
        """

        Args:
            mediator:   A class that implements IMediator
        """
        super().__init__(mediator=mediator)

        self.logger: Logger = getLogger(__name__)

        self._name    = PluginName('Wx Image')
        self._author  = 'Humberto A. Sanchez II'
        self._version = '0.9c'

        self._inputFormat  = cast(InputFormat, None)
        self._outputFormat = OutputFormat(formatName=FORMAT_NAME, extension=PLUGIN_EXTENSION, description=PLUGIN_DESCRIPTION)

    def setImportOptions(self) -> bool:
        return False

    def setExportOptions(self) -> bool:
        """
        Popup the options dialog

        Returns:
            if False, the export will be cancelled.
        """
        with DlgWxImageOptions(self._mediator.umlFrame) as dlg:
            if dlg.ShowModal() == OK:
                self.logger.warning(f'{dlg.imageFormat=} {dlg.outputFileName=}')
                self._imageFormat:    WxImageFormat = dlg.imageFormat
                self._outputFileName: str           = dlg.outputFileName

            else:
                self.logger.warning(f'Cancelled')
                return False

        return True

    def read(self) -> bool:
        pass

    def write(self, oglObjects: OglObjects):

        """
        Write data

        Args:
            oglObjects:     list of exported objects
        """

        mediator: IMediator = self._mediator
        mediator.deselectAllOglObjects()

        imageType: BitmapType     = WxImageFormat.toWxBitMapType(self._imageFormat)

        window:    ScrolledWindow = self._mediator.umlFrame
        context:   ClientDC       = ClientDC(window)
        memory:    MemoryDC       = MemoryDC()

        x, y = window.GetSize()
        emptyBitmap: Bitmap = Bitmap(x, y, -1)

        memory.SelectObject(emptyBitmap)
        memory.Blit(source=context, xsrc=0, height=y, xdest=0, ydest=0, ysrc=0, width=x)
        memory.SelectObject(NullBitmap)

        img:       Image = emptyBitmap.ConvertToImage()
        extension: str   = self._imageFormat.__str__()

        filename: str   = f'{self._outputFileName}.{extension}'
        status:   bool  = img.SaveFile(filename, imageType)
        if status is False:
            self.logger.error(f'Error on image write to {filename}')
