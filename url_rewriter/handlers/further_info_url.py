# -*- coding: utf-8 -*-

"""
.. module:: handlers.rewrite.documentation_url.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: Rewrites further information URL's.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from url_rewriter.utils.http import log_error
from url_rewriter.utils.http import write_error



# Set of supported projects.
PROJECTS = {
    "cmip6",
}

# Query parameter names.
_PARAM_CLIENT_ID = 'client'


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

        # TEMPORARY: simply return something to browser.
        self.write({
            'message': "TODO: resolve metadata and render view",
            'experiment_id': experiment_id,
            'institution_id': institution_id,
            'mip_era': mip_era,
            'source_id': source_id,
            'variant_label': variant_label,
            })
        self.set_header("Content-Type", "application/json; charset=utf-8")
        return

        # Redirect.
        url = _get_redirect_url(
            self,
            mip_era,
            institution_id,
            source_id,
            experiment_id,
            variant_label
            )
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

    # Reroute cmip6 to cmip6-draft.
    if mip_era == u"cmip6":
        mip_era = "cmip6-draft"

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
        url_host_type = "dev"
    elif 'test' in handler.request.host:
        url_host_type = "test"
    else:
        url_host_type = "prod"

    raise NotImplementedError()
