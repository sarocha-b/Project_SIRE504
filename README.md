# SeqQC
Command-line helpers for filter nanopore DNA sequences based on quality and length

## Installation
Create conda environment
```bash
conda env create -f project.yml
```
Activating an environment
```bash
conda activate seqQC
```

## Usage
```bash
main.py <command> [option]
```

Common flags:

- `-f/ --file FILENAME` - input fastq.gz file.
- `-h/ --help` after command to see its specific usage.

## Command
`seqQC`

Filter pass read

- `-m/ --mins INT` - minimum read length.
- `-q/ --qual INT` - minimum average quality score.

`seqDist`

Create distribution plot

- `-c/ --column COLUMN NAME` - select column for distribution plot.

## Developer Notes
- Source lives in `src/seqQC`.

