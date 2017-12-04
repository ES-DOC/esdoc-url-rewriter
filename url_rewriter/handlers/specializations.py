# -*- coding: utf-8 -*-

"""
.. module:: handlers.rewrite.specializations.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Rewrites documentation URL's.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado



# Set of supported projects.
PROJECTS = {
    'cmip6': {
        'aerosol',
        'atmos',
        'atmoschem',
        'land',
        'landice',
        'ocean',
        'ocnbgchem',
        'seaice',
        'toplevel'
    }
}

# Map of target URL's.
_URLS = {
    'prod': 'https://view-specializations.es-doc.org',
    'test': 'https://test-view-specializations.es-doc.org',
    'dev': 'https://view-specializations.es-doc.org',
}

# Map of target URL's params.
_URL_PARAMS = '/?target={0}&client={1}'

# Query parameter names.
_PARAM_CLIENT_ID = 'client'


class SpecializationsRewriteRequestHandler(tornado.web.RequestHandler):
    """Rewrites viewer URL requests.

    """
    def get(self, project, topic=None):
        """HTTP GET handler.

        """
        # Validate prior to processing.
        _validate_request(self)

        # Parse input parameters.
        project, topic = _reformat_inputs(project, topic)

        # Calculate new url.
        url = _get_redirect_url(self, project, topic)

        # Redirect.
        self.redirect(url, permanent=False)


def _validate_request(handler):
    """Validates request prior to processing.

    """
    # TODO: validate headers
    # TODO: validate body
    # TODO: validate parameters
    # TODO: validate attachments
    pass


def _reformat_inputs(project, topic):
    """Reforms request parameters.

    """
    def _reformat(source):
        if source is not None:
            source = unicode(source).strip().lower()
            if len(source) == 0:
                source = None
        return source

    return _reformat(project), \
           _reformat(topic)


def _get_redirect_url(handler, project, topic):
    """Gets redirect url.

    """
    # Set specialization targets.
    targets = [i for i in [project, topic] if i is not None]

    # Set URL host type.
    if 'localhost' in handler.request.host:
        url_host_type = "dev"
    elif 'test' in handler.request.host:
        url_host_type = "test"
    else:
        url_host_type = "prod"

    # Set URL params.
    url_params = _URL_PARAMS.format(
        ".".join(targets),
        handler.get_query_argument(_PARAM_CLIENT_ID, "esdoc-url-rewrite")
        )

    return "{}{}".format(_URLS[url_host_type], url_params)
