#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "running ..."

    source $REWRITER_WS_HOME/sh/activate_venv.sh
	python $REWRITER_WS_HOME/sh/app_run.py
}

# Invoke entry point.
main
