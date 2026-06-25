class ToolkitError(Exception):
    pass


class ProviderError(ToolkitError):
    pass


class ResolveError(ToolkitError):
    pass