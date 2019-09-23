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

# Base URL of ES-DOC explorer web application.
EXPLORER_URL = r'https://explore.es-doc.org/{}/further-info?target={}'

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
        redirect_url = EXPLORER_URL.format(mip_era, url)
        self.redirect(redirect_url, permanent=False)


def _validate_request(handler, mip_era, url):
    """Validates request prior to processing.

    """
    # TODO: validate headers
    # TODO: validate body
    # TODO: validate parameters
    # TODO: validate attachments
    return True


def _validate_cmip6_request(handler, url):
    """Validates a CMIP6 request prior to processing.

    """
    return True
