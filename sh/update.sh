#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    pushd $REWRITER_WS_HOME

    log "update starts ..."

    git pull
    pipenv install

	cp $REWRITER_WS_HOME/ops/config/supervisord.conf $REWRITER_WS_HOME/ops/config/supervisord-backup.conf
	cp $REWRITER_WS_HOME/ops/config/ws.conf $REWRITER_WS_HOME/ops/config/ws-backup.conf
	cp $REWRITER_WS_HOME/resources/*.conf $REWRITER_WS_HOME/ops/config

    log "update complete"

    popd
}

# Invoke entry point.
main
