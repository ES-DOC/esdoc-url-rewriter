#!/bin/bash

# Import utils.
source $REWRITER_WS_HOME/sh/utils.sh

# Main entry point.
main()
{
	export PYTHONPATH=$PYTHONPATH:$REWRITER_WS_HOME
	source $REWRITER_WS_HOME/ops/venv/bin/activate
}

# Invoke entry point.
main
