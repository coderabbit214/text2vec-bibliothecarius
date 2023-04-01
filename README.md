#  text2vec-bibliothecarius

> This project is used for local vector computation of [bibliothecarius](https://github.com/coderabbit214/bibliothecarius)

## Quick Start

### [Download Model](https://huggingface.co/shibing624/text2vec-base-chinese/tree/main)

After downloading the model, place it in the `./text2vec-base-chinese` folder.

File list `ls -l text2vec-base-chinese/`

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

### Use Docker

```bash
docker-compose up -d
```

### Perform Test

```bash
curl --location --request POST 'http://127.0.0.1:8001/vector' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input":"你好"
}'
```

## Reference

- https://github.com/shibing624/text2vec
