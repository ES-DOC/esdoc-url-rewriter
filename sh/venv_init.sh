#!/bin/bash

# Import utils.
source $ESDOC_URL_REWRITER_HOME/sh/init.sh

# Main entry point.
main()
{
    log "SH : installing virtual environment ..."

    pip install --upgrade pip
    pip install --upgrade virtualenv
    virtualenv $ESDOC_URL_REWRITER_HOME/venv
    source $ESDOC_URL_REWRITER_HOME/venv/bin/activate
    pip install --upgrade pip
    pip install --upgrade --no-cache-dir -I -r $ESDOC_URL_REWRITER_HOME/requirements.txt
    deactivate
}

# Invoke entry point.
main
