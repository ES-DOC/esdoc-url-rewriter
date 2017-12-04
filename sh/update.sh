#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "update starts ..."

	cd $REWRITER_WS_HOME
	git pull
    log "shell updated"
	source $REWRITER_WS_HOME/sh/update_config.sh
	source $REWRITER_WS_HOME/sh/update_venv.sh

    log "update complete"
}

# Invoke entry point.
main
