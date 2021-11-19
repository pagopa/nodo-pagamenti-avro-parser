# Avro Parser for `Nodo dei Pagamenti`
This is a tool for parse the `.avro` files stored by the [Azure Event Hub](https://portal.azure.com/?l=en.en-us#@pagopa.it/resource/subscriptions/26abc801-0d8f-4a6e-ac5f-8e81bcc09112/resourceGroups/pagopa-u-msg-rg/providers/Microsoft.EventHub/namespaces/pagopa-u-evh-ns01/eventhubs/nodo-dei-pagamenti-re/capture) 

# Prerequisites
- python3
- java

# Usage

You can find the `.avro` files in the [Azure Blob Storage](https://portal.azure.com/?l=en.en-us#blade/Microsoft_Azure_Storage/ContainerMenuBlade/overview/storageAccountId/%2Fsubscriptions%2F26abc801-0d8f-4a6e-ac5f-8e81bcc09112%2FresourceGroups%2Fpagopa-u-msg-rg%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Fnododeipagamentiresauat/path/eventireblob/etag/%220x8D9AB4090CC765A%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride//defaultId//publicAccessVal/None)

```
usage: main.py [-h] [--iuv [IUV]] [--dominio [ID DOMINIO]] [--pretty] FILE

Parse an .avro file

positional arguments:
  FILE                  .avro file path to parse

optional arguments:
  -h, --help            show this help message and exit
  --iuv [IUV]           filter by iuv
  --dominio [ID DOMINIO]
                        filter by ID Dominio
  --pretty              prettyprint the json output

```

Example: 

`python3 main.py 33.avro --iuv 02005513436500922 --dominio 77777777777  `