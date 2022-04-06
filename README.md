# DangBot -- 好怪哦，再来一句

> **卡群怪话bot，powered by [GPT2 for Chinese chitchat](https://github.com/yangjianxin1/GPT2-chitchat)**

## Training

Example:
```
python train.py --lr 5e-2 --epochs 30 --max_len 300 --batch_size 8 --device 0 --pretrained_model model/model_epoch40_50w --num_workers 8 --val_num 300 --train_path data/train.pkl
```

## Interact

Example
```
python interact.py --device 0 --model_path model/model_epoch40_50w
```

## Pretrained Weights

[**model_epoch40_50w**](https://drive.google.com/drive/folders/1fJ6VuBp4wA1LSMpZgpe7Hgm9dbZT5bHS) (from GPT2 for Chinese chitchat)