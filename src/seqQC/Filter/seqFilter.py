import pandas as pd

def filterData(file):

    seqtsv = pd.read_csv(file, delimiter='\t') # read file

    #condition
    seqtsv['length_filter'] = seqtsv['seq_length'] >= 200 
    seqtsv['meanQscore_filter'] = seqtsv['meanQ'] >= 7

    # save as tsv ???
    seqtsv.to_csv(file, index=None, sep="\t")
    
    print(f"Save data as a tsv file")


def filtered(file):

    SeqTsv = pd.read_csv(file, delimiter='\t')

    # add new col with 2 condition
    SeqTsv["passes_filtering"] = SeqTsv['length_filter'] & SeqTsv['meanQscore_filter'] # & operator : return True or False

    passed = SeqTsv[SeqTsv['passes_filtering']] #return only column[passes_filtering] is True
    passed.to_csv('pass_filter.tsv', sep='\t', index=False ) #save to new tsv

    print('save the filtered data ')


def DataToFastq():
    pass




if __name__ == "__main__":
    filterData('../project_test/stat_data.tsv')