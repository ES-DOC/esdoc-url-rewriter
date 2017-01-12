#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "TESTS : running ..."

    source $REWRITER_WS_HOME/sh/activate_venv.sh
    nosetests -v -s $REWRITER_WS_HOME/tests

    log "TESTS : complete ..."
}

# Invoke entry point.
main
