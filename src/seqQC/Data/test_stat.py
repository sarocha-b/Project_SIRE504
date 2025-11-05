from seqData import *
import pandas as pd

# data_group_barcode('../../Desktop/ont_reads.project.fastq.gz')

def statseq(file):
    # with open(file, 'w') as input:
    # tsv_stat = pd.read_csv(file, delimiter='\t')
    # writer = csv.writer(input, delimiter="\t")
    # summary_stat = tsv_stat.groupby('barcode').agg({"Mean": ['mean','mode']})
    # writer.writerow(summary_stat)
    # tsv_stat["mean"] = tsv_stat.groupby('barcode').agg({"Mean": ['mean','mode']})
    # tsv_stat.to_csv(file, sep='\t', index=False)
    

    df = pd.read_csv(file, sep="\t")   # or delimiter="\t"
    # print(df.head())     # show first few rows
    # stat = df.loc[:5['barcode','total_phred_score','seq_length']]

    mean_stat = df.groupby('barcode').agg({"total_phred_score": ['mean','median'],
                                             'seq_length':['mean']})
    
    # df = df.merge(file,mean_stat, on='barcode', how='left')
    
    # df.to_csv(file, sep='\t', index=False )

    print(mean_stat)
    return mean_stat


    # print("saved")

if __name__ == "__main__":
    statseq('../Project/group_data.tsv')
