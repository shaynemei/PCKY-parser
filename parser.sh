#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: hw4_parser.sh <grammar_filename> <test_sentence_filename> <output_filename>"
else
	/opt/python-3.6/bin/python3 parser.py $1 $2 $3
	#python3 parser.py $1 $2 $3
fi
