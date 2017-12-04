# -*- coding: utf-8 -*-

"""
.. module:: handlers.rewrite.further_info.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Rewrites further information URL's.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado



# Query parameter names.
_PARAM_CLIENT_ID = 'client'

# Map of target host's.
_HOSTS = {
    "prod": "http://documentation.es-doc.org",
    "test": "http://test-documentation.es-doc.org",
    "dev": "http://documentation.es-doc.org"
}


class FurtherInfoRewriteRequestHandler(tornado.web.RequestHandler):
    """Rewrites viewer URL requests.

    """
    def get(self):
        """HTTP GET handler.

        """
        # Destructure url.
        url = self.request.path[1:]
        mip_era = url.split('.')[0]

        # Validate prior to processing.
        _validate_request(self, mip_era, url)

        # Set redirect host.
        if 'localhost' in self.request.host:
            host = _HOSTS['dev']
        elif 'test' in self.request.host:
            host = _HOSTS['test']
        else:
            host = _HOSTS['prod']

        # Redirect.
        redirect_url = _REDIRECT_GETTERS[mip_era](host, url)
        self.redirect(redirect_url, permanent=False)


def _get_cmip6_redirect(host, url):
    """Returns a further info url redirect.

    """
    experiment_id = url.split('.')[3]

    # TODO: redirect to CMIP6 further info URL homepage.
    return "{}/cmip6/experiments/{}".format(host, experiment_id)


# Map of redirect getters to project/mip-era.
_REDIRECT_GETTERS = {
    'cmip6': _get_cmip6_redirect
}


def _validate_request(handler, mip_era, url):
    """Validates request prior to processing.

    """
    # TODO: validate headers
    # TODO: validate body
    # TODO: validate parameters
    # TODO: validate attachments
    return True
