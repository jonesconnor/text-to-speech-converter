import boto3
import constants as c

client = boto3.client(
    'polly',
    region_name = "us-west-2",
    aws_access_key_id = c.ACCESS_KEY_ID,
    aws_secret_access_key = c.SECRET_ACCESS_KEY
)

response = client.synthesize_speech(VoiceId='Joanna',
    OutputFormat = 'mp3',
    Text = 'Hi my name is Connor and I like air conditioning',
    Engine = 'neural')

with open('speech.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())
