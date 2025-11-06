import gzip
from Bio import SeqIO
import re
import pandas as pd

def cal_fastq_stat(file):
    with gzip.open(file, "rt") as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        tsv_stat = []
        for idx, rec in enumerate(record_iterator):
            total = 0
            seq_id = rec.id
            meanQ = sum(rec.letter_annotations['phred_quality'])/len(rec)
            for k,l in rec.letter_annotations.items():
                for t in l:
                    if t >= 20:
                        total += 1
            pctQ20 = (total/len(rec))*100
        
            tsv_stat.append([seq_id, meanQ, pctQ20])
            if idx == 9:
                break

def df_merge_stat(tsv_stat):
    df_stat = pd.DataFrame(tsv_stat[0:], columns=['seq_id', 'meanQ', 'pctQ20'])
    df_seqData = pd.read_table('group_data.tsv')
    df_seqStat = pd.merge(df_seqData, df_stat, on='seq_id', how='inner')