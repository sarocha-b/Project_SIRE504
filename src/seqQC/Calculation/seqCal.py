import gzip
from Bio import SeqIO
import re
import pandas as pd
from functools import partial

def cal_fastq_stat(file):
    with gzip.open(file, "rt") as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        tsv_stat = []
        for rec in record_iterator:
            total = 0
            seq_id = rec.id
            meanQ = sum(rec.letter_annotations['phred_quality'])/len(rec)
            for k,l in rec.letter_annotations.items():
                for t in l:
                    if t >= 20:
                        total += 1
            pctQ20 = (total/len(rec))*100
        
            tsv_stat.append([seq_id, meanQ, pctQ20])
            

def df_merge_stat(tsv_stat):
    df_stat = pd.DataFrame(tsv_stat[0:], columns=['seq_id', 'meanQ', 'pctQ20'])
    df_seqData = pd.read_table('group_data.tsv')
    df_seqStat = pd.merge(df_seqData, df_stat, on='seq_id', how='inner')

def calc_qt(df_seqStat):
    q_30 = partial(pd.Series.quantile, q=0.30)
    q_30.__name__ = "30%"
    df_qt = df_seqStat.groupby('barcode')['meanQ'].agg([q_30])
    df_seqStat = pd.merge(df_seqStat, df_qt, on='barcode', how='inner')

def save_seq_stat(df_seqStat):
    df_seqStat.to_csv('sequence_stat.tsv', sep='\t', index=False)
    print("save as sequence_stat.tsv")
