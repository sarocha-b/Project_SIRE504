from Bio import SeqIO
import json
import re
import gzip
from Bio.SeqRecord import SeqRecord
import csv



def data_group_barcode(file): # Data table grouping by barcode
    dict_group = {}

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

    # write into TSV
    with open("group_data.tsv", "w") as output_tsv:
        writer = csv.writer(output_tsv, delimiter="\t")
        writer.writerow(["barcode", "seq_id", "total_phred_score", "seq_length"])

        for barcode, records in dict_group.items():
            for rec in records:
                row_data = [
                    barcode,
                    rec.id,
                    sum(rec.letter_annotations["phred_quality"]),
                    len(rec.seq)
                ]
                writer.writerow(row_data)

    print("save as tsv")



if __name__ == "__main__":
    data_group_barcode('../../Desktop/ont_reads.project.fastq.gz')
    # data_group_barcode('../term_project/raw_data/try_seq.fastq')


