## Q1. Getting the embeddings model

Now, get the embeddings model `multi-qa-mpnet-base-dot-v1` from
[the Sentence Transformer library](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#model-overview)

> Note: this is not the same model as in HW3

```bash
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer(model_name)
```

Create the embeddings for the first LLM answer:

```python
answer_llm = df.iloc[0].answer_llm
```

What's the first value of the resulting vector?

* [X] -0.42
* [ ] -0.22
* [ ] -0.02
* [ ] 0.21

## Q2. Computing the dot product

Now for each answer pair, let's create embeddings and compute dot product between them

We will put the results (scores) into the `evaluations` list

What's the 75% percentile of the score?

* [ ] 21.67
* [X] 31.67
* [ ] 41.67
* [ ] 51.67

## Q3. Computing the cosine

From Q2, we can see that the results are not within the [0, 1] range. It's because the vectors coming from this model are not normalized.

So we need to normalize them.

To do it, we

* Compute the norm of a vector
* Divide each element by this norm

So, for vector `v`, it'll be `v / ||v||`

In numpy, this is how you do it:

```python
norm = np.sqrt((v * v).sum())
v_norm = v / norm
```

Let's put it into a function and then compute dot product
between normalized vectors. This will give us cosine similarity

What's the 75% cosine in the scores?

* [ ] 0.63
* [ ] 0.73
* [X] 0.83
* [ ] 0.93

## Q4. Rouge

Now we will explore an alternative metric - the ROUGE score.  

This is a set of metrics that compares two answers based on the overlap of n-grams, word sequences, and word pairs.

It can give a more nuanced view of text similarity than just cosine similarity alone.

We don't need to implement it ourselves, there's a python package for it:

```bash
pip install rouge
```

(The latest version at the moment of writing is `1.0.1`)

Let's compute the ROUGE score between the answers at the index 10 of our dataframe (`doc_id=5170565b`)

```
from rouge import Rouge
rouge_scorer = Rouge()

scores = rouge_scorer.get_scores(r['answer_llm'], r['answer_orig'])[0]
```

There are three scores: `rouge-1`, `rouge-2` and `rouge-l`, and precision, recall and F1 score for each.

* `rouge-1` - the overlap of unigrams,
* `rouge-2` - bigrams,
* `rouge-l` - the longest common subsequence

What's the F score for `rouge-1`?

* [ ] 0.35
* [X] 0.45
* [ ] 0.55
* [ ] 0.65

## Q5. Average rouge score

Let's compute the average F-score between `rouge-1`, `rouge-2` and `rouge-l` for the same record from Q4

* [X] 0.35
* [ ] 0.45
* [ ] 0.55
* [ ] 0.65

## Q6. Average rouge score for all the data points

Now let's compute the F-score for all the records and create a dataframe from them.

What's the average F-score in `rouge_2` across all the records?

* [ ] 0.10
* [X] 0.20
* [ ] 0.30
* [ ] 0.40
