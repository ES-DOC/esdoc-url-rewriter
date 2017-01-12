#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "installing virtual environment ..."

    $REWRITER_WS_PIP install --upgrade pip
    $REWRITER_WS_PIP install --upgrade virtualenv
    virtualenv $REWRITER_WS_HOME/ops/venv
    source $REWRITER_WS_HOME/sh/activate_venv.sh
    $REWRITER_WS_PIP install --upgrade pip
    $REWRITER_WS_PIP install --upgrade --no-cache-dir -I -r $REWRITER_WS_HOME/resources/requirements.txt
    deactivate
}

# Invoke entry point.
main
