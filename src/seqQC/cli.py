from argparse import ArgumentParser
from Data.seqData import *


def argparserlocal():
    parser = ArgumentParser(prog='seqQC', description='Filter nanopore sequence')

    subparsers = parser.add_subparsers(title='commands', description='Please choose command below:',dest='command')
    subparsers.required=True

    filter_command = subparsers.add_parser('main', help='Filter pass read')
    filter_command.add_argument("-f", "--file", type=str, default=None, 
                                help="provide fastq file") 
    filter_command.add_argument("-m", "--mins", action="store_true",
                            help="Minimum read length")
    filter_command.add_argument("-M", "--max", action="store_true",
                            help="Maximum read length")
    filter_command.add_argument("-q", "--qual", action="store_true",
                                help="Minimum quality score")
    filter_command.add_argument("-w", "--high", action="store_true",
                                help="Maximum quality score")

    return parser

def main():
    parser = argparserlocal()
    args = parser.parse_args()

    # parser = argparserlocal()
    # try:
    #     args = parser.parse_args(argv)
    # except SystemExit as e:
    #     # Help (or parse error) triggered an exit; don't kill the process in this test.
    #     # argparse has already printed the help/usage text.
    #     print("============================\n")

    # if args.file == None:
    #     exit("------\nError: You do not provide -f or --file\n------\n")
    # else:
    #     file = args.file

    if args.command == 'data_group_barcode':
        if args.file == None:
            parser.parse_args(['data_group_barcode','-h'])
        file = args.file
        data_group_barcode(file)

    # if args.command == 'data_group_barcode':
    #     if args.min == None:
    #         parser.parse_args(['data_group_barcode','-h'])
    #     print("Input",args.min,"\ngroup=", data_group_barcode(file) )

if __name__ == "__main__":
    # main(['-h'])
    main()