#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: hw4_improved_induction.sh <treebank_filename> <output_PCFG_file>"
else
	/opt/python-3.6/bin/python3 improved_topcfg.py $1 $2
	#python3 improved_topcfg.py $1 $2
fi
