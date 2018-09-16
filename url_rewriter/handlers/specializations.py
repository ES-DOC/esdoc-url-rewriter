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
        url = '{}://{}/static/index.html?target={}&client={}'.format(
            self.request.protocol,
            self.request.host,
            ".".join([i for i in [project, topic] if i is not None]),
            self.get_query_argument(_PARAM_CLIENT_ID, "esdoc-url-rewrite")
            )

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
