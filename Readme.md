# Fluent Example
Fluentd forwarder aggregator example

[![CodeQL](https://github.com/appuv/fluent_example/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/appuv/fluent_example/actions/workflows/github-code-scanning/codeql)  [![License](https://img.shields.io/github/license/appuv/fluent_example)](https://github.com/appuv/fluent_example/blob/main/LICENSE) [![GitHub top language](https://img.shields.io/github/languages/top/appuv/fluent_example)]([https://github.com/appuv/fluent_example](https://img.shields.io/github/languages/top/appuv/fluent_example))

# Architecture
![Architecture](images/fluentd_forward_agg_approach.png)

## Prerequisite
1. [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
2. [Docker](https://www.docker.com/)   

## Setup
Configure the following files

```
forwarder/Configuration/fluent_tail.conf
datagen.py
```

Start the docker of forwarder and aggregator and run the datagen.

## Further Reading
[Medium](https://medium.com/@masterappu/data-transfer-in-edge-2245a49d95d)

