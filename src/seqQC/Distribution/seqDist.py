import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import LogFormatter
# from Data.seqData import preprocess_data

def plot_bc_dist(df_seqStat,column):
    ax = sns.histplot(df_seqStat, x=column, hue="barcode", bins=100, log_scale=True, element='poly')
    ax.xaxis.set_major_formatter(LogFormatter(base=10, labelOnlyBase=False))
    plt.title("Barcode Distribution")
    plt.show()
    return


if __name__ == "__main__":
    # df = preprocess_data('/Users/sarocha/SIRE504_programming/project_files_test/all_read.fastq.gz')
    plot_bc_dist(df, 'seq_length')