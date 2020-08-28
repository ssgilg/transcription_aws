from __future__ import print_function
import time
import boto3
import requests



def make_transcription_job(speaker_key, conversation_):

    transcribe = boto3.client('transcribe')
    job_name = "scribe-python-test3-custom-language2-speaker-"+str(speaker_key)+"_conv_"+str(conversation_)
    #job_uri = "s3://test-scribe-ig-1/"+str(n_speaker)+"-conversation_"+str(conversation)+".wav"
    job_uri = "s3://test-scribe-ig-1/"+str(speaker_key)+"_conversation_"+str(conversation_)+".wav"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media       = {'MediaFileUri': job_uri},
        MediaFormat ='wav',
        LanguageCode='en-US',
        #Settings = {"MaxSpeakerLabels":2,
        #           "ShowSpeakerLabels": True},
        #           "VocabularyName" : "vocab_test_081020"},
        ModelSettings = {"LanguageModelName": "test2-custom-model-wide"},
        JobExecutionSettings = {"AllowDeferredExecution": True,
                                 "DataAccessRoleArn": "arn:aws:iam::121503602521:role/service-role/AmazonTranscribeServiceRole-custom-train"}
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    print(status)
    # print(status['TranscriptionJob']['Transcript'])
    # print(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])

    url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    r = requests.get(url, allow_redirects=True)
    #open('output-'+str(n_speaker)+'-conversation-'+str(conversation)+'.json', 'wb').write(r.content)
    open('output-'+str(speaker_key)+'-conversation-'+str(conversation_)+'.json', 'wb').write(r.content)


n_speaker = "EJ"
conversation =  ['1','2','3','4','5','6']

for conv in conversation:
    print("START  conversation: ", conv )
    make_transcription_job(n_speaker,conv)
    print("finish  conversation: ", conv)
    print("\n")
