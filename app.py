# import os
# import json
# import sys
# import boto3

# print("imported successfully...")

# prompt="""
#     You are a smart assistant, so please let me know what is machine learning in smartest way
# """

# bedrock= boto3.client(
#     service_name="bedrock-runtime",
#     region_name="ap-south-1"  # Use your specific region
# )

# payload={
#     "prompt": "[INST]"+prompt+"[/INST]",
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p": 0.9
# }

# body=json.dumps(payload) 
# model_id= "meta.llama2-70b-instruct-v1"


# response=bedrock.invoke_model(
#     body=body,
#     model_id=model_id,
#     accept="application/json",
#     content_type="application/json"
# )

# response_body=json.loads(response.get("body").read())
# response_text=response_body["generation"]
# print(response_text)

import os
import json
import sys
import boto3

# Initialize Bedrock client with region
bedrock = boto3.client(
    service_name="bedrock-runtime", 
    region_name="ap-south-1"  # Use your specific region
)
print("imported successfully...")

prompt = """
    You are a smart assistant, so please let me know what is machine learning in the smartest way.
"""

# Prepare the payload
payload = {
    "prompt": "[INST]" + prompt + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9
}

# Convert payload to JSON
body = json.dumps(payload)

# Set the model ID (with the correct parameter name 'modelId')
model_id = "meta.llama3-70b-instruct-v1"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    model_id=model_id,  # Corrected parameter name
    accept="application/json",
    content_type="application/json"  # Corrected parameter name
)

# Process the response
response_body = json.loads(response.get("body").read())
response_text = response_body["generation"]

print(response_text)
