import boto3
from PyPDF2  import PdfFileReader
import constants as c

# Function to get text from PDF
def text_extractor(file):
    with open(file, "rb") as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(0)
        text = page.extractText()
    return text

# AWS Connection
client = boto3.client(
    'polly',
    region_name = "us-west-2",
    aws_access_key_id = c.ACCESS_KEY_ID,
    aws_secret_access_key = c.SECRET_ACCESS_KEY
)

# Grab text from sample document
f = text_extractor("sample.pdf")

# Pass contents to Polly
response = client.synthesize_speech(VoiceId='Joanna',
    OutputFormat = 'mp3',
    Text = f,
    Engine = 'neural')

# Create mp3 file containing Polly's speech
with open('speech.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())
