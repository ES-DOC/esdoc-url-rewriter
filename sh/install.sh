#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
    log "install starts ..."

	source $REWRITER_WS_HOME/sh/install_config.sh
	source $REWRITER_WS_HOME/sh/install_venv.sh

    log "install complete"
}

# Invoke entry point.
main
