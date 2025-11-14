#!/usr/bin/env python3

from cli import *
from Data.seqData import *

def main_test():
    parser = argparser()
    args = parser.parse_args()
    
    if args.file == None:
        file = "test_data/test_data.fastq"
    else:
        file = args.file


    if args.command == 'data_group_barcode':
        if args.file == None:
            parser.parse_args(['data_group_barcode','-h'])
        print("Input",args.file,"\nfilter=", data_group_barcode(file))


if __name__ == "__main__":
    main_test() 