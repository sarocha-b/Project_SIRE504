import pandas as pd
from Bio import SeqIO
import gzip

def filterData(df_seqStat):

    #condition
    df_seqStat['length_filter'] = df_seqStat['seq_length'] >= 200 
    df_seqStat['meanQscore_filter'] = df_seqStat['meanQ'] >= 7

    # save as tsv
    df_seqStat.to_csv('total_read.tsv', index=None, sep="\t")
    
    print(f"Save data as a tsv file")


def filtered():

    SeqTsv = pd.read_csv('total_read.tsv', delimiter='\t')

    # add new col with 2 condition
    SeqTsv["passes_filtering"] = SeqTsv['length_filter'] & SeqTsv['meanQscore_filter'] # & operator : return True or False

    passed = SeqTsv[SeqTsv['passes_filtering']] #return only column[passes_filtering] is True
    passed.to_csv('pass_read.tsv', sep='\t', index=False ) #save to new tsv

    print('save the filtered data')


def DataToFastq(file):
    df_Pass = pd.read_table('pass_read.tsv')
        
    record = ''
    with gzip.open(file, 'rt') as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        for rec in record_iterator:
            for i in df_Pass['seq_id']:
                if rec.id == i:
                    record += rec.format('fastq')
                    

    with open('filtered_seq.fastq', 'w') as output:
        output.write(record)
                
    print('save as fastq')


def countRead():
    total_data = pd.read_table('total_read.tsv')
    pass_data = pd.read_table("pass_read.tsv")


    total_read = total_data.shape[0]
    pass_read = pass_data.shape[0]


    print(f'The total number of reads is: {total_read}') 
    print(f'The number of pass reads is: {pass_read}') 
    print(f'The number of fail reads is: {total_read - pass_read}')


if __name__ == "__main__":
    # filterData('../../project_test/sequence_stat.tsv')
    # filtered('../../project_test/sequence_stat.tsv')
    DataToFastq('../../project_test/test_seq.fastq')

