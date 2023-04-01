#  text2vec-bibliothecarius

> 本项目用于[bibliothecarius](https://github.com/coderabbit214/bibliothecarius)向量本地化计算

## 快速开始

### 下载本项目

```bash
git clone git@github.com:coderabbit214/text2vec-bibliothecarius.git
cd text2vec-bibliothecarius
```

### [下载模型](https://huggingface.co/shibing624/text2vec-base-chinese/tree/main)

模型下载后放入`./text2vec-base-chinese`文件夹中

文件列表`ls -l text2vec-base-chinese/`

```bash
total 799408
-rw-r--r--@ 1 coderabbit  staff       4100 Mar 30 15:58 README.md
-rw-r--r--@ 1 coderabbit  staff        856 Mar 30 15:58 config.json
-rw-r--r--@ 1 coderabbit  staff       1175 Mar 30 15:58 gitattributes.txt
-rw-r--r--@ 1 coderabbit  staff        546 Mar 30 15:58 logs.txt
-rw-r--r--@ 1 coderabbit  staff  409154033 Mar 30 15:59 pytorch_model.bin
-rw-r--r--@ 1 coderabbit  staff        112 Mar 30 15:58 special_tokens_map.json
-rw-r--r--@ 1 coderabbit  staff        319 Mar 30 15:58 tokenizer_config.json
-rw-r--r--@ 1 coderabbit  staff     109540 Mar 30 15:59 vocab.txt
```

### 使用Docker

```bash
docker-compose up -d
```

### 进行测试测试

```bash
curl --location --request POST 'http://127.0.0.1:8001/vector' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input":"你好"
}'
```

## 参考

- https://github.com/shibing624/text2vec
