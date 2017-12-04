#!/bin/bash

# Set home path.
declare REWRITER_WS_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $REWRITER_WS_HOME

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "REWRITER-TESTS : execution starts ..."

    source $REWRITER_WS_HOME/sh/activate_venv.sh

    nosetests -v -s $REWRITER_WS_HOME/tests
    # nosetests -v -s $ERRATA_WS_HOME/tests/test_config.py
    # nosetests -v -s $ERRATA_WS_HOME/tests/test_ops.py
    # nosetests -v -s $ERRATA_WS_HOME/tests/test_search.py
    # nosetests -v -s $ERRATA_WS_HOME/tests/test_publishing.py
    # nosetests -v -s $ERRATA_WS_HOME/tests/test_publishing_negative.py

    log "REWRITER-TESTS : execution complete ..."
}

# Invoke entry point.
main
