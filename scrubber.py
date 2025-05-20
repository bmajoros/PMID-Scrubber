#!/usr/bin/env python3                                                          
#=========================================================================      
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public               
# License (GPL) version 3, as described at www.opensource.org.                  
# Author: William H. Majoros (bmajoros@alumni.duke.edu)                         
#=========================================================================      
from __future__ import (absolute_import, division, print_function,
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
# The above imports should allow this program to run in both Python 2 and       
# Python 3.  You might need to update your version of module "future".          
import sys
import re

#=========================================================================      
# main()                                                                        
#=========================================================================      
if(len(sys.argv)!=2):
    exit("scrubber.py <pmids.txt>\n")
(infile,)=sys.argv[1:]

found=0
query=""
unique=set()
with open(infile,"rt") as IN:
    for line in IN:
	while(True):
            match=re.search("(.*)PMID:\s*([^\)]+\s*)(.*)",line)
            if(match is None): break
            left=match.group(1); hit=match.group(2); right=match.group(3)
            elems=re.split("[,\s]",hit)
            for elem in elems:
		if(not re.search("\\d",elem)): continue
		term=elem+"[PMID]"
		unique.add(term)
            line=left+" "+right
query=" OR ".join(unique)
print(query)
print(len(unique),"found")

