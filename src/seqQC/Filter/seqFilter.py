import pandas as pd
from Bio import SeqIO
import gzip

def filterData(df_seqStat, min_length, qscore):

    #condition
    df_seqStat['length_filter'] = df_seqStat['seq_length'] >= min_length 
    df_seqStat['mean_qscore_filter'] = df_seqStat['mean_qscore'] >= qscore


    # save as tsv
    df_seqStat.to_csv('total_read.tsv', index=None, sep="\t")
    
    print(f"save as tsv file")


def filtered():

    SeqTsv = pd.read_csv('total_read.tsv', delimiter='\t')

    # add new col with 2 condition
    SeqTsv["passes_filter"] = SeqTsv['length_filter'] & SeqTsv['mean_qscore_filter'] # & operator : return True or False

    passed = SeqTsv[SeqTsv['passes_filter']] #return only column[passes_filter] is True
    passed.to_csv('pass_read.tsv', sep='\t', index=False ) #save to new tsv

    print('save as filtered data')


def DataToFastq(file):
    df_Pass = pd.read_table('pass_read.tsv')
        
    record = ''
    with gzip.open(file, 'rt') as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        for rec in record_iterator:
            for i in df_Pass['seq_id']:
                if rec.id == i:
                    record += rec.format('fastq')
                    

    with gzip.open('filtered_seq.fastq.gz', 'wt') as output:
        output.write(record)
                
    print('save as fastq.gz')
    print("-" * 40)


def countRead():
    total_data = pd.read_table('total_read.tsv')
    pass_data = pd.read_table("pass_read.tsv")


    total_read = total_data.shape[0]
    pass_read = pass_data.shape[0]


    print(f'The total number of reads is: {total_read}') 
    print(f'The number of pass reads is: {pass_read}') 
    print(f'The number of fail reads is: {total_read - pass_read}')
    print("-" * 40)


if __name__ == "__main__":
    # filterData('../../project_test/sequence_stat.tsv')
    # filtered('../../project_test/sequence_stat.tsv')
    DataToFastq('../../project_test/test_seq.fastq')

