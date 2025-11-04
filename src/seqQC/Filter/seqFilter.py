import pandas as pd

def filterSeq(file):

    seqtsv = pd.read_csv('stat_data.tsv', delimiter='\t')

    seqtsv['FT_Mean'] = seqtsv['%Mean'] >= 70 
    seqtsv['FT_Quartile'] = seqtsv['Quartile'] >= 30


    seqtsv.to_csv(file, sep='\t', index=False )
    
    print(f"Finish")

if __name__ == "__main__":
    filterSeq('stat_data.tsv')