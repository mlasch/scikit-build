"""
This module defines exceptions commonly used in scikit-build.
"""


class SKBuildError(RuntimeError):
    """Exception raised when an error occurs while configuring or building a
    project.
    """
    pass


class SKBuildGeneratorNotFoundError(SKBuildError):
    """Exception raised when no suitable generator is found for the current
    platform.
    """
    pass


class PythonLibraryNotFound(SKBuildError):
    """Exception raised when no shared Python library was found on the system.
    """
    pass
