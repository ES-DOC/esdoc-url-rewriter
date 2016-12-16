# -*- coding: utf-8 -*-
"""

.. module:: app.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC Errata - web-service entry point.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado.web

from url_rewriter import handlers
from url_rewriter.utils import config
from url_rewriter.utils.logger import log_web as log



def _get_app_endpoints():
    """Returns map of application endpoints to handlers.

    """
    result = {
        # (r'/', handlers.ops.HeartbeatRequestHandler),
    }

    result = set()

    # Documentation URL.
    if config.rewriteTarget == "doc":
        for project, doc_types in handlers.documentation_url.DOC_TYPES.items():
            result.add((
                r'/({0})'.format(project),
                handlers.DocumentationURLRewriteRequestHandler
                ))
            for doc_type in doc_types:
                result.add((
                    r'/({0})/({1})'.format(project, doc_type),
                    handlers.DocumentationURLRewriteRequestHandler
                    ))
                result.add((
                    r'/({0})/({1})/(.*)'.format(project, doc_type),
                    handlers.DocumentationURLRewriteRequestHandler
                    ))

    # Further info URL.
    elif config.rewriteTarget == "fi":
        for project in handlers.further_info_url.PROJECTS:
            result.add((
                r'/({0})/(.*)'.format(project),
                handlers.FurtherInfoURLRewriteRequestHandler
                ))


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


    return tornado.web.Application(endpoints,
                                   debug=True,
                                   **_get_app_settings())


def run():
    """Runs web service.

    """
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
