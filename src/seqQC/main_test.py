#!/usr/bin/env python3

from cli import *
from Data.seqData import *
from Filter.seqFilter import *
from Calculation.seqCal import *
from src.main import main

def main_test():
    parser = argparserlocal()
    args = parser.parse_args()
    
    if args.file == None:
        file = "test_data/test_data.fastq"
    else:
        file = args.file

    if getattr(args, 'min', False) is True:
        min_length = args.mins
    else:
        min_length = 200


    if args.command == 'main':
        if args.file == None:
            parser.parse_args(['main','-h'])
        print("Input",args.file,"\nfilter=", main(file))
    # elif args.command == 'filterData':
    #     if args.min == None:
    #         parser.parse_args(['filterData','-h'])  
    #     print("input",args.mins,"\nMinimum length=", filterData(min_length, args.mins))
    # elif args.command == 'filterData':
    #     if args.max == None:
    #         parser.parse_args(['filterData','-h'])  
    #     print("input",args.max,"\nMaximum length=", filterData(df_seqStat, args.max))
    # elif args.command == 'filterData':
    #     if args.qual == None:
    #         parser.parse_args(['filterData','-h'])  
    #     print("input",args.qual,"\nMinimum quality score=", filterData(df_seqStat, args.qual))
    # elif args.command == 'filterData':
    #     if args.high == None:
    #         parser.parse_args(['filterData','-h'])  
    #     print("input",args.high,"\nMaximum quality score=", filterData(df_seqStat, args.high))
        

if __name__ == "__main__":
    main_test() 