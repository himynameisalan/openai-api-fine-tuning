
# Fine-tuning ChatGPT model

How to customize a model for your application.

## Introduction

Fine-tuning lets you get more out of the models available through the API by providing:

    1. Higher quality results than prompt design
    2. Ability to train on more examples than can fit in a prompt
    3. Token savings due to shorter prompts
    4. Lower latency requests
 
At a high level, fine-tuning involves the following steps:

    1. Prepare and upload training data
    2. Train a new fine-tuned model
    3. Use your fine-tuned model

## What models can be fine-tuned?

    1. davinci
    2. curie
    3. babbage
    4. ada

## Installation

```cmd
pip install --upgrade openai
```

##  Prepare training data

Your data must be a JSONL document, where each line is a prompt-completion pair corresponding to a training example. You can use our CLI data preparation tool to easily convert your data into this file format.

```json
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
...
```

## Create a fine-tuned model

Start your fine-tuning job using the OpenAI CLI:

```cmd
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
```

Running the above command does several things:

    1. Uploads the file using the files API (or uses an already-uploaded file)
    2. Creates a fine-tune job
    3. Streams events until the job is done (this often takes minutes, but can take hours if there are many jobs in the queue or your dataset is large)

After you've started a fine-tune job, it may take some time to complete. Your job may be queued behind other jobs on our system, and training our model can take minutes or hours depending on the model and dataset size. If the event stream is interrupted for any reason, you can resume it by running:

```cmd
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```

When the job is done, it should display the name of the fine-tuned model.

In addition to creating a fine-tune job, you can also list existing jobs, retrieve the status of a job, or cancel a job.

```cmd
# List all created fine-tunes
openai api fine_tunes.list

# Retrieve the state of a fine-tune. The resulting object includes
# job status (which can be one of pending, running, succeeded, or failed)
# and other information
openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>

# Cancel a job
openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>
```

## Use a fine-tuned model
When a job has succeeded, the fine_tuned_model field will be populated with the name of the model. You may now specify this model as a parameter to our Completions API.

```cmd
openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
```
