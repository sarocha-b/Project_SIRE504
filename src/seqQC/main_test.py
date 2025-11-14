#!/usr/bin/env python3

from cli import *
from Data.seqData import *
from Filter.seqFilter import *
from Calculation.seqCal import *
from main import *

def main_test():
    parser = argparserlocal()
    args = parser.parse_args()
    
    file = args.file
    min_length = args.mins
    qscore = args.qual
    
    if args.command == 'main':
        if args.file == None or args.mins == None or args.qual == None:
            parser.parse_args(['main','-h'])
        print("Input",args.file,"\nStatus:", main(file, min_length, qscore))  
        print("Minimum length:", args.mins)
        print("Minimum average quality score:", args.qual)
           

if __name__ == "__main__":
    main_test() 