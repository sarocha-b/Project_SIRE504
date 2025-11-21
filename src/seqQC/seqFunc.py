from Data import seqData
from Calculation import seqCal
from Filter import seqFilter
from Distribution import seqDist

def filter_seq(file, min_length, qscore):
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
    seqFilter.countRead()

    return "Filtering complete. Check output files for results."

def dist_seq(file, column):

    seqData.data_group_barcode(file)
    data = seqData.assess_data()
    df = seqData.convert_df(data)

    data_stat = seqCal.cal_fastq_stat(file)
    df_seqStat = seqCal.df_merge_stat(df, data_stat)

    seqDist.plot_bc_dist(df_seqStat, column)
    return "Distribution plot generated."

if __name__ == "__main__":
    # filter_seq('/mnt/c/Users/jitpr/SIRE504_programming/project504/example/fastq/barcode01/ont.reads.bc01.fastq.gz')
    dist_seq('/Users/sarocha/SIRE504_programming/project_files_test/all_read.fastq.gz', 'mean_qscore')