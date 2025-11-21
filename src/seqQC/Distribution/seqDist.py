import matplotlib.pyplot as plt
import seaborn as sns
# from Data.seqData import preprocess_data

def plot_bc_dist(df_seqStat,column):
    sns.displot(df_seqStat, x=column, kind="kde", hue="barcode")
    plt.title("Barcode Distribution")
    plt.show()
    return


if __name__ == "__main__":
    # df = preprocess_data('/Users/sarocha/SIRE504_programming/project_files_test/all_read.fastq.gz')
    plot_bc_dist(df, 'seq_length')