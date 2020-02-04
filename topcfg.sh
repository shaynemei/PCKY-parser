#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: hw4_topcfg.sh <treebank_filename> <output_PCFG_file>"
else
	/opt/python-3.6/bin/python3 topcfg.py $1 $2
	#python3 topcfg.py $1 $2
fi
