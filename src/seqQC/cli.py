from argparse import ArgumentParser
from Data.seqData import *


def argparserlocal():
    parser = ArgumentParser(prog='seqQC', description='Filter nanopore sequence')

    subparsers = parser.add_subparsers(title='commands', description='Please choose command below:',dest='command')
    subparsers.required=True

    filter_command = subparsers.add_parser('seqQC', help='Filter pass read')
    filter_command.add_argument("-f", "--file", type=str, default=None, 
                                help="provide fastq.gz file") 
    filter_command.add_argument("-m", "--mins", type=int, default=200,
                            help="minimum read length")
    # filter_command.add_argument("-M", "--max", action="store_true",
    #                         help="Maximum read length")
    filter_command.add_argument("-q", "--qual", type=int, default=7,
                                help="minimum average quality score")
    # filter_command.add_argument("-w", "--high", action="store_true",
    #                             help="Maximum quality score")

    return parser


