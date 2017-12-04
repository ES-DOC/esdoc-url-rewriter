from url_rewriter.factory import documentation
from url_rewriter.factory import further_info
from url_rewriter.factory import specializations
from url_rewriter.utils import constants



# Map of rewrite targets to url factories.
_FACTORIES = {
    constants.REWRITER_TYPE_DOCUMENTATION: documentation,
    constants.REWRITER_TYPE_FURTHER_INFO: further_info,
    constants.REWRITER_TYPE_SPECIALIZATIONS: specializations
}


def yield_urls(target):
	"""Yields supported URL patterns.

	"""
	return _FACTORIES[target].yield_urls()
