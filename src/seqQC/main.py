#!/usr/bin/env python3

from cli import *
from seqFunc import *

def main():
    parser = argparserlocal()
    args = parser.parse_args()
    
    file = args.file
    
    if args.command == 'seqQC':
        min_length = args.mins
        qscore = args.qual
        if args.file == None or args.mins == None or args.qual == None:
            parser.parse_args(['seqQC','-h'])
        print("Input:",args.file,"\nStatus:", filter_seq(file, min_length, qscore))  
        print("Minimum length:", args.mins)
        print("Minimum average quality score:", args.qual)

    elif args.command == 'seqDist':
        column = args.column
        if args.file == None or args.column == None:
            parser.parse_args(['seqDist','-h'])
        print("Input:",args.file,"\nStatus:", dist_seq(file, column))  
        print("Column for distribution plot:", args.column)
           

if __name__ == "__main__":
    main() 