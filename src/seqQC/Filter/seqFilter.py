import pandas as pd

def filterSeq(file):

    seqtsv = pd.read_csv(file, delimiter='\t')

    seqtsv['FT_Mean'] = seqtsv['%Mean'] >= 70 
    seqtsv['FT_Quartile'] = seqtsv['Quartile'] >= 30


    seqtsv.to_csv(file, sep='\t', index=False )
    
    print(f"Finish")

if __name__ == "__main__":
    filterSeq('../project_test/stat_data.tsv')