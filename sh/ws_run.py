# -*- coding: utf-8 -*-

"""
.. module:: run_web_service.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runs the url-rewriter web-service.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import sys
import url_rewriter


def _main():
    """Main entry point.

    """
    # Run web service.
    try:
        url_rewriter.run()

    # Handle unexpected exceptions.
    except Exception as err:
        # Simple log to stdout.
        print err

        # Ensure that web-service is stopped.
        try:
            url_rewriter.stop()
        except:
            pass

    # Signal exit.
    finally:
        sys.exit()


# Main entry point.
if __name__ == '__main__':
    _main()
