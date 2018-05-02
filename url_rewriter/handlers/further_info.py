# -*- coding: utf-8 -*-

"""
.. module:: handlers.rewrite.further_info.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Rewrites further information URL's.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

import tornado

from url_rewriter.utils import config



# Example redirect.
# http://localhost:8000/?target=cmip6.ipsl.ipsl-cm6a-lr.dcppa-hindcast-niff.s2000.r1

# Query parameter names.
_PARAM_CLIENT_ID = 'client'

# Map of target host's.
_HOSTS = {
    "prod": "https://view-furtherinfo.es-doc.org",
    "test": "https://test-view-furtherinfo.es-doc.org",
    "dev": "http://localhost:8000"
}


class FurtherInfoRewriteRequestHandler(tornado.web.RequestHandler):
    """Rewrites viewer URL requests.

    """
    def get(self, _):
        """HTTP GET handler.

        """
        # Destructure url.
        url = self.request.path[1:]
        mip_era = url.split('.')[0].lower()

        # Validate prior to processing.
        _validate_request(self, mip_era, url)

        # Redirect.
        redirect_url = '{}?target={}'.format(_HOSTS[config.mode], url)
        self.redirect(redirect_url, permanent=False)


def _validate_request(handler, mip_era, url):
    """Validates request prior to processing.

    """
    # TODO: validate headers
    # TODO: validate body
    # TODO: validate parameters
    # TODO: validate attachments
    return True
