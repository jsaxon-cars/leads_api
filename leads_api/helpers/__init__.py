"""
Helper functions
"""


def get_pyramid_settings(request, prefix=""):
    """Get all settings or a subset of all settings based on a prefix

    :param request:
    :param prefix:
    :return:
    """
    return {k: v for k, v in request.registry.settings.items() if k.startswith(prefix + ".")}
