from Bio import SeqIO
import json
import re
import gzip
# from Bio.SeqRecord import SeqRecord
# import csv
import pandas as pd

dict_group = {}

def data_group_barcode(file): # Data table grouping by barcode

    # read gzip file
    with gzip.open(file,"rt") as input_file:
    # with open(file,"r") as input_file:
        for data in SeqIO.parse(input_file, 'fastq'):
            filter_barcode = re.finditer(f'barcode[0-9]+', data.description)
            
            # group each barcode
            for barcode in filter_barcode:
                each_barcode = barcode.group() 
                # add to dict
                dict_group.setdefault(each_barcode,[]).append(data)

    print("grouping done")

    
def assess_data(dict):
    pre_convert_data = []
    for barcode, records in dict.items():
        for rec in records:
            data = [
                barcode,
                rec.id,
                sum(rec.letter_annotations["phred_quality"]),
                len(rec.seq)
            ]
            pre_convert_data.append(data)
    
    return pre_convert_data


def convert_df(data):
    df = pd.DataFrame(data, columns=["barcode", "seq_id", "total_phred_score", "seq_length"])
    print("converting done")
    return df


def preprocess_data(file):
    data_group_barcode(file)
    pre_convert_data = assess_data(dict_group)
    convert_df(pre_convert_data)
    print("preprocessing done")


if __name__ == "__main__":
    preprocess_data('../term_project/raw_data/ont_reads.project.fastq.gz')
    # preprocess_data('../term_project/raw_data/try_seq.fastq')


