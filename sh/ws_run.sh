#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
    log "WEB-SERVICE : running ..."

    source $ESDOC_URL_REWRITER_HOME/venv/bin/activate
	python $ESDOC_URL_REWRITER_HOME/sh/ws_run.py
}

# Invoke entry point.
main
