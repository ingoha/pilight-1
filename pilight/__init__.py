# http://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError
else:
    # Fallback für uralte Python-Versionen (< 3.8) via external package
    from importlib_metadata import version, PackageNotFoundError

__project__ = 'pilight'
__version__ = None  # required for initial installation

try:
    __version__ = version(__project__)
except PackageNotFoundError:
    VERSION = __project__ + '-' + '(local)'
else:
    VERSION = __project__ + '-' + __version__
