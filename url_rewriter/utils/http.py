# -*- coding: utf-8 -*-
"""
.. module:: utils.http.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: HTTP utility functions, particulary process_request.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from url_rewriter.utils import logger



# Request validation error HTTP response code.
_HTTP_RESPONSE_INVALID_REQUEST_ERROR = 400

# Processing error HTTP response code.
_HTTP_RESPONSE_SERVER_ERROR = 500


def _can_return_debug_info(handler):
    """Gets flag indicating whether the application can retrun debug information.

    """
    return handler.application.settings.get('debug', False)


def log(handler, msg, is_error=False):
    """Logs an error response.

    """
    msg = "[{}]: --> {}".format(id(handler), msg)
    if is_error:
        logger.log_web_error(msg)
    else:
        logger.log_web(msg)


def log_error(handler, error):
    """Logs an error response.

    """
    _log(handler, "error --> {} --> {}".format(handler, error), True)


def write_error(handler, error):
    """Writes processing error to response stream.

    """
    # Reset handler output.
    handler.clear()

    # Set reason code (exception shielding when not in PROD).
    reason = str(error) if _can_return_debug_info(handler) else None

    # Set response code.
    try:
        response_code = error.response_code
    except AttributeError:
        response_code = _HTTP_RESPONSE_SERVER_ERROR

    # Return error.
    handler.send_error(response_code, reason=reason.replace("\n", ""))

