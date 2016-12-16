#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
    log "URL-REWRITER-TESTS : running ..."

    nosetests -v -s $ESDOC_URL_REWRITER_HOME/tests

    log "URL-REWRITER-TESTS : complete ..."
}

# Invoke entry point.
main
