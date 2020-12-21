#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "running ..."

    pushd $REWRITER_WS_HOME
	pipenv run python $REWRITER_WS_HOME/sh/app_run.py
    popd
}

# Invoke entry point.
main
