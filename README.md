# BERT-Syntax

Assesing the syntactic abilities of BERT.

## What

Evaluate Google's BERT-Base and BERT-Large models on the syntactic agreement datasets from [Linzen, Goldberg and Dupoux 2016](https://arxiv.org/abs/1611.01368) and [Marvin and Linzen 2018](https://arxiv.org/abs/1808.09031) and [Gulordava et al 2018](http://aclweb.org/anthology/N18-1108).

This is quite messy, as I hacked it together between things here and there. But I also believe it is accurate. This lists the data files and shows how to run the evaluation. For more details and results, see the [arxiv report](https://arxiv.org/abs/TBD).

## Data Files

Data taken from the github repos of [Linzen, Goldberg and Dupoux](https://github.com/TalLinzen/rnn_agreement) (LGD), [Marvin and Linzen](https://github.com/BeckyMarvin/LM_syneval) (ML), and [Gulordava et al](https://github.com/facebookresearch/colorlessgreenRNNs).

| File | Description |
|---|---|
| `marvin_linzen_dataset.tsv` |  stimuli from Marvin and Linzen. I dumped it from the pickle files of ML |
| `wiki.vocab`                  | from LGD, used for verb inflections ([wiki.vocab](https://github.com/TalLinzen/rnn_agreement/raw/master/data/wiki.vocab)) |
| `lgd_dataset.tsv`             | processed data from LGD |
| `generated.tab`               | data from Gulordava et al ([generated.tab](https://github.com/facebookresearch/colorlessgreenRNNs/raw/master/data/agreement/English/generated.tab)) |

`lgd_dataset.tsv` is created by 
```bash
wget http://tallinzen.net/media/rnn_agreement/agr_50_mostcommon_10K.tsv.gz
gunzip agr_50_mostcommon_10K.tsv.gz
python make_linzen_goldberg_testset.py > lgd_dataset.tsv
```

## Obtaining the results

```bash
pip install pytorch_pretrained_bert

python eval_bert.py > results/lgd_results_large.txt
python eval_bert.py base > results/lgd_results_base.txt
python eval_bert.py marvin > results/marvin_results_large.txt
python eval_bert.py marvin base > results/marvin_results_base.txt
python eval_bert.py gul > results/gulordava_results_large.txt
python eval_bert.py gul base > results/gulordava_results_base.txt
```

## Generating tables (for the PDF)

```bash
python gen_marvin_tbl.py 
python gen_lgd_tbl.py
python gen_gul_tbl.py
```

