#!/bin/bash

# ###############################################################
# SECTION: HELPER FUNCTIONS
# ###############################################################

# Wraps standard echo by adding ESDOC prefix.
log()
{
	declare now=`date +%Y-%m-%dT%H:%M:%S`
	declare tabs=''
	if [ "$1" ]; then
		if [ "$2" ]; then
			for ((i=0; i<$2; i++))
			do
				declare tabs+='\t'
			done
	    	echo -e $now" [INFO] :: URL-REWRITER > "$tabs$1
	    else
	    	echo -e $now" [INFO] :: URL-REWRITER > "$1
	    fi
	else
	    echo -e $now" [INFO] :: URL-REWRITER > "
	fi
}

# ###############################################################
# SECTION: INITIALIZE VARS
# ###############################################################

# Set of ops sub-directories.
declare -a ESDOC_URL_REWRITER_OPS_DIRS=(
	$ESDOC_URL_REWRITER_HOME/ops
)

# ###############################################################
# SECTION: Initialise file system
# ###############################################################

# Ensure ops paths exist.
for ops_dir in "${ESDOC_URL_REWRITER_OPS_DIRS[@]}"
do
	mkdir -p $ops_dir
done
