import gzip
from Bio import SeqIO
import pandas as pd

def cal_fastq_stat(file):
    with gzip.open(file, "rt") as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        data_stat = []
        for rec in record_iterator:
            seq_id = rec.id
            meanq = sum(rec.letter_annotations['phred_quality'])/len(rec)
            
            data_stat.append([seq_id, meanq])
    
    return data_stat          

def df_merge_stat(df, data_stat):
    df_stat = pd.DataFrame(data_stat[0:], columns=['seq_id', 'mean_qscore'])
    df_seqStat = pd.merge(df, df_stat, on='seq_id', how='inner')
    
    print("calculation done")
    return df_seqStat
    


if __name__ == "__main__":
    data_stat = cal_fastq_stat('/mnt/c/Users/jitpr/SIRE504_programming/project504/ont_reads.project.fastq.gz')
    df_merge_stat(df, data_stat)