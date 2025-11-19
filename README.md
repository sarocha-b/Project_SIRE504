# SeqQC
Command-line helpers for filter DNA sequences based on quality and length

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
seqQC <command> [option]
```

Common flags:

- `-f/ --file FILENAME` - input fastq.gz file
- `-m/ --mins INT` - minimum read length
- `-q/ --qual INT` - minimum average quality score

## Command
`seqQC`

- Add `-h/ --help` after command to see its specific usage.

## Developer Notes
- Source lives in `src/seqQC`.

