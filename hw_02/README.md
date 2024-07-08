# Homework 2

## Q1. Running Ollama in Docker

What's the version of the Ollama client?

```
0.1.48
```

## Q2. Downloading the LLM

What's the content of the file related to Gemma?

```
{"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"sha256:887433b89a901c156f7e6944442f3c9e57f3c55d6ed52042cbb7303aea994290","size":483},"layers":[{"mediaType":"application/vnd.ollama.image.model","digest":"sha256:c1864a5eb19305c40519da12cc543519e48a0697ecd30e15d5ac228644957d12","size":1678447520},{"mediaType":"application/vnd.ollama.image.license","digest":"sha256:097a36493f718248845233af1d3fefe7a303f864fae13bc31a3a9704229378ca","size":8433},{"mediaType":"application/vnd.ollama.image.template","digest":"sha256:109037bec39c0becc8221222ae23557559bc594290945a2c4221ab4f303b8871","size":136},{"mediaType":"application/vnd.ollama.image.params","digest":"sha256:22a838ceb7fb22755a3b0ae9b4eadde629d19be1f651f73efb8c6b4e2cd0eea0","size":84}]}
```

## Q3. Running the LLM

The answer to the prompt "10 * 10" is:

```
Sure, here's a safe answer to the question:

10 x 10 = 100.
```

## Q4. Downloading the weights

What's the size of the ollama_files/models folder?

- [] 0.6G
- [] 1.2G
- [X] 1.7G
- [] 2.2G

## Q5. Adding the weights

The dockerfile is on [Dockerfile.gemma](./Dockerfile.gemma):

```
COPY ./ollama_files ./root/.ollama
```

## Q6. Serving it

You need to run `python serving.py`. How many completion tokens did you get in response?

- [X] 304
- [] 604
- [] 904
- [] 1204
