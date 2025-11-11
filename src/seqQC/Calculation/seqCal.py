import gzip
from Bio import SeqIO
import pandas as pd

def cal_fastq_stat(file):
    with gzip.open(file, "rt") as handle:
        record_iterator = SeqIO.parse(handle, "fastq")
        data_stat = []
        for rec in record_iterator:
            total = 0
            seq_id = rec.id
            meanQ = sum(rec.letter_annotations['phred_quality'])/len(rec)
            # for k,l in rec.letter_annotations.items():
            #     for t in l:
            #         if t >= 20:
            #             total += 1
            # pctQ20 = (total/len(rec))*100
        
            data_stat.append([seq_id, meanQ])

    return data_stat
  
            

def df_merge_stat(df, data_stat):
    df_stat = pd.DataFrame(data_stat[0:], columns=['seq_id', 'meanQ'])
    df_seqStat = pd.merge(df, df_stat, on='seq_id', how='inner')
    return df_seqStat
    

# def calc_qt(df_seqStat):
#     q_30 = partial(pd.Series.quantile, q=0.30)
#     q_30.__name__ = "30%"
#     df_qt = df_seqStat.groupby('barcode')['meanQ'].agg([q_30])
#     df_seqStat = pd.merge(df_seqStat, df_qt, on='barcode', how='inner')
#     return df_seqStat
  
  

if __name__ == "__main__":
    data_stat = cal_fastq_stat('/mnt/c/Users/jitpr/SIRE504_programming/project504/ont_reads.project.fastq.gz')
    df_merge_stat(df, data_stat)