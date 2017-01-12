#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	source $REWRITER_WS_HOME/sh/activate_venv.sh
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $REWRITER_WS_HOME/resources/requirements.txt
    deactivate

    log "virtual environment updated"
}

# Invoke entry point.
main
