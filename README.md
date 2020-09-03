# transcription_aws

this is a summary of the use of aws-transcribe
We tested 11 speakers with a variety in their speech features. The speakers read a text that resembles a scrum meeting. We took the recordings and "clean" them with pyAudioAnalysis (See https://github.com/cbanuelosintek/audiopreprocess).


The files have to be in wav format, if this is not the case, this can be converted to wav format (audiopreprocess).

In aws save the file to be transcribe in a S3 bucket.

Make a transcription Job, there are 3 ways

Important Note: TranscriptionJobName must be unique 

1) command line

        > aws transcribe start-transcription-job ^
        > --region us-east-1 ^
        > --cli-input-json file://my_file.json


2) command line + json file

    json file example:
        {
    "TranscriptionJobName": "test-multiple-5speakers-vocab-ig-json", 
    "LanguageCode": "en-US", 
    "MediaFormat": "wav", 
    "Media": {
        "MediaFileUri": "s3://test-scribe-ig-1/right.wav"
             },
    "Settings":{
        "MaxSpeakerLabels": 5,
        "ShowSpeakerLabels": true
                },
    "VocabularyFileUri": "my_vocab.txt",
    "VocabularyName": "my_vocab"
    }

    In command line;
        > aws transcribe start-transcription-job ^
        > --region us-east-1 ^
        > --cli-input-json file://my_file.json


3) via python script 
    see transcribe.py

How to get the results?

In order to improve the transcriptions we tried a series of cleaning techniques in the recordings:
normalization, cleaning, etc

No improvement was observed.

How to improve transcription?
   
- Add vocabulary

    --list : add a list (or table) with important key words. In 
      order to use this option a list with the vocabulary must
      be created. "Depending on your use case, you may have 
      domain-specific terminology that doesn’t transcribe properly"
    --Aws transcribe will recognize more easily these words.
    --Drawbacks: transcription tends to be inclined to use 
      these words sometimes incorrectly. 
    -- It also helps if you want a given word to be transribed 
      in certain way, for instance a technical word that you want 
      to appear as "Java" in the transcription. By including the 
      word "Java" in the vocabulary all the appeareances of "java" 
      will appear as "Java" in the transcription.

    --table : this is a more elaborated way to introduce a vocabulary.
      It has to include pronunciation (IPA Chart With Sounds, 
      English to IPA Translator not currently working)

    --Example output without vocabulary:

    
        "because I know Well I don't know But the the vegetable years 
        transcribe can tell different speakers right So in my date our in my
         and my date I I have label for each speaker..." 
    
    --Example output vocabulary: Add vocab with word "data
    
        "because I know Well I don't know but the the data billionaires transcribe can tell different speakers right So in my data our in my and my data I I have label for each speaker ..."
  
    In the firs transcription we get  "vegetable years" and when using a 
    vocabulary we get "data billionaires". The transcription was incorrect 
    with and without vocabulary, this is an example of bias towards the 
    words in the vocabulary.
    A positive outcome is seen in the phrase "in my date" which after
    using the vocabulary got transcribed as "in my data"

    Observations
    -when introducing a simple vocab improvment is not noticeble in good quality audio

- Custom language models

 Train a model with context and tuning data

-context: Information related to the topics in the audio

-tuning: transcriptions of audios with events similar to what you want to transcribe

aws suggests:

    -We recommend using at least 100k and at most 10M words of running text.
    -We recommend each plain text file contain 200,000 words or more, but not exceeding 1GB in overall file size. 
    -The text should be in UTF-8, and use one sentence per line. 
    -Each sentence should contain punctuation.


Steps to create custom language model

-Save context and tuning (data) in s3 bucket in different folders.

-Create the custom model in the graphic interface.
            -specify tuning and training data locations
            -minimum suggested for tuning data ~ 10 000 words
            -minimum suggested for trainning data ~ 100 000 words
            -can take about 7 hours



For context we used wikipedia information with the following topics: "Functional programing", "Programing paradigm",
"Computer code",  "computer program", "debugging",
"Object Oriented Programming",
"NLP ML",
"NER nlp",
"apache spark",
"algorithm",
"java program",
"Typescript", "HTML5", "CSS", "IDE software", "VSCode",
"Linter software" , "Performance (Big O notation)",
"node javascript",
"react JS",
"big data",
"udemy",
"video",
"problem",
"online learning course",
"method test",
"vocabulary",
"aws services",
"aws transcribe",
"aws deploymnet",
"sql",
"back-end front-end",
"scala programming language",
"hadoop",
"machine learning",
"chatbot", 
"cluster analysis",
"embedding",
"technology",
"artificial intelligence",
"test cased code benchmarks",
"scrum meeting deadline schedule",
"data",
"matrix factorization",
"lemmatization",
"spacy nlp",
"supervised unsupervised learning",
"word-to-vec",
"coding programming exercise",
"update progress coding project weekly status",
"vacations days off", "sick days going to doctor",
"car parking", "office supplies", "Visa process appointments",
"academic degree college university transcripts"

As tuning data we used transcriptions of videos from youtube that resemble weekly meetings from different teams in a tech company. This is no exactly the kinf if interaction we are trying to transcribe but it has real interactions beteen team members and a leader.


RESULTS

