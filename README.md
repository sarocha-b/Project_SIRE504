# SeqQC
Command-line helpers for filter DNA sequences based on quality and length

## Installation
```
# Create conda environment
conda env create -f project.yml
```

## Usage
```
seqQC <command> [option]
```

Common flags:

`-f/ --file FILENAME` - input fastq.gz file
`-m/ --mins INT` - minimum read length
`-q/ --qual INT` - minimum average quality score

## Command
`seqQC` 
Add `-h/ --help` after command to see its specific usage.

