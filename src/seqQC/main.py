from Data import seqData
from Calculation import seqCal
from Filter import seqFilter
from argparse import ArgumentParser

def main(file, min_length, qscore):
    # Step 1: Preprocess data to create DataFrame
    seqData.data_group_barcode(file)
    data = seqData.assess_data()
    df = seqData.convert_df(data)
    
    # Step 2: Calculate sequence statistics
    data_stat = seqCal.cal_fastq_stat(file)
    df_seqStat = seqCal.df_merge_stat(df, data_stat)
    
    # Step 3: Filter sequences based on quality and length
    seqFilter.filterData(df_seqStat, min_length, qscore)
    seqFilter.filtered()
    seqFilter.DataToFastq(file)

    return "Filtering complete. Check output files for results."

if __name__ == "__main__":
    main('/mnt/c/Users/jitpr/SIRE504_programming/project504/example/fastq/barcode01/ont.reads.bc01.fastq.gz')