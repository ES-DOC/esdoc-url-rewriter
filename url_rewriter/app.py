# -*- coding: utf-8 -*-
"""

.. module:: app.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - web-service entry point.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado.web

from url_rewriter import factory
from url_rewriter import handlers
from url_rewriter.utils import config
from url_rewriter.utils import constants
from url_rewriter.utils.logger import log_web as log



# Map of rewriter types ot handlers.
_REWRITER_HANDLERS = {
    constants.REWRITER_TYPE_DOCUMENTATION: handlers.DocumentationRewriteRequestHandler,
    constants.REWRITER_TYPE_FURTHER_INFO: handlers.FurtherInfoRewriteRequestHandler,
    constants.REWRITER_TYPE_SPECIALIZATIONS: handlers.SpecializationsRewriteRequestHandler
}


def _get_app_endpoints():
    """Returns map of application endpoints to handlers.

    """
    result = set()
    handler = _REWRITER_HANDLERS[config.rewriteTarget]
    for url in factory.yield_urls(config.rewriteTarget):
        result.add((url, handler))

    return result


def _get_app_settings():
    """Returns app settings.

    """
    return {
        "cookie_secret": config.cookie_secret,
        "compress_response": True
    }


def _get_app():
    """Returns application instance.

    """
    endpoints = _get_app_endpoints()
    log("Endpoint to handler mappings:")
    for url, handler in sorted(endpoints, key=lambda i: i[0]):
        log("{0} ---> {1}".format(url, str(handler).split(".")[-1][0:-2]))

    return tornado.web.Application(endpoints, debug=True, **_get_app_settings())


def run():
    """Runs web service.

    """
    # Validate rewrite target.
    if config.rewriteTarget not in constants.REWRITER_TYPE:
        raise ValueError('Rewrite target is invalid.  Suported = {}'.format(constants.REWRITER_TYPE))

    # Initialize application.
    log("Initializing")
    app = _get_app()

    # Open port.
    app.listen(config.port)
    log("Ready")

    # Start processing requests.
    tornado.ioloop.IOLoop.instance().start()


def stop():
    """Stops web service.

    """
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(lambda x: x.stop(), ioloop)
