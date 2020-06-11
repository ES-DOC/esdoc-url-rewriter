#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "update starts ..."

    _update_src
	_update_config
    _update_venv	

    log "update complete"
}

_update_config()
{
	cp $REWRITER_WS_HOME/ops/config/supervisord.conf $REWRITER_WS_HOME/ops/config/supervisord-backup.conf
	cp $REWRITER_WS_HOME/ops/config/ws.conf $REWRITER_WS_HOME/ops/config/ws-backup.conf
	cp $REWRITER_WS_HOME/resources/*.conf $REWRITER_WS_HOME/ops/config
}

_update_src()
{
    pushd $REWRITER_WS_HOME
	git pull
}

_update_venv()
{
    pushd $REWRITER_WS_HOME
    pipenv install
}

# Invoke entry point.
main
