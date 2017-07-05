# -*- coding: utf-8 -*-

"""
.. module:: handlers.rewrite.documentation_url.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Rewrites further information URL's.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado



# Set of supported projects.
PROJECTS = {
    "cmip6",
}

# Query parameter names.
_PARAM_CLIENT_ID = 'client'

# Map of target host's.
_HOSTS = {
    "prod": "http://documentation.es-doc.org",
    "test": "http://test.documentation.es-doc.org",
    "dev": "http://documentation.es-doc.org",
}


class FurtherInfoURLRewriteRequestHandler(tornado.web.RequestHandler):
    """Rewrites viewer URL requests.

    """
    def get(self, mip_era, further_info):
        """HTTP GET handler.

        """
        # Validate prior to processing.
        _validate_request(self, mip_era, further_info)

        # Parse input parameters.
        mip_era, further_info = _reformat_inputs(mip_era, further_info)
        institution_id, source_id, experiment_id, variant_label = further_info.split('.')

        # Calculate new url.
        url = _get_redirect_url(
            self,
            mip_era,
            institution_id,
            source_id,
            experiment_id,
            variant_label
            )

        # Redirect.
        self.redirect(url, permanent=False)


def _validate_request(handler, mip_era, further_info):
    """Validates request prior to processing.

    """
    # TODO: validate headers
    # TODO: validate body
    # TODO: validate parameters
    # TODO: validate attachments
    # TODO: validate mip_era is supported
    # TODO: validate further_info format
    return True


def _reformat_inputs(mip_era, further_info):
    """Reforms request parameters.

    """
    mip_era = unicode(mip_era).strip().lower()
    if len(mip_era) == 0:
        mip_era = None

    further_info = unicode(further_info).strip().lower()
    if len(further_info) == 0:
        further_info = None

    return mip_era, further_info


def _get_redirect_url(
    handler,
    mip_era,
    institution_id,
    source_id,
    experiment_id,
    variant_label
    ):
    """Gets redirect url.

    """
    # Set URL host type.
    if 'localhost' in handler.request.host:
        host = _HOSTS['dev']
    elif 'test' in handler.request.host:
        host = _HOSTS['test']
    else:
        host = _HOSTS['prod']

    return "{}/{}/experiments/{}".format(host, mip_era, experiment_id)
