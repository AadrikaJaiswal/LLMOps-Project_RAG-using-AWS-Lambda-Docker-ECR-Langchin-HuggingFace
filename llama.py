
# import os
# import json
# import sys
# import boto3

# # Initialize Bedrock client with region
# bedrock = boto3.client(
#     service_name="bedrock-runtime", 
#     region_name="ap-south-1"  # Use your specific region
# )
# print("imported successfully...")

# prompt = """
#     You are a smart assistant, so please let me know what is machine learning in the smartest way.
# """

# # Prepare the payload
# payload = {
#     "prompt": "[INST]" + prompt + "[/INST]",
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p": 0.9
# }

# # Convert payload to JSON
# body = json.dumps(payload)

# # Set the model ID (with the correct parameter name 'modelId')
# model_id = "meta.llama3-70b-instruct-v1:0"

# # Invoke the model
# response = bedrock.invoke_model(
#     body=body,
#     modelId=model_id,  # Corrected parameter name
#     accept="application/json",
#     contentType="application/json"  # Corrected parameter name
# )

# # Process the response
# response_body = json.loads(response.get("body").read())
# response_text = response_body["generation"]

# print(response_text)


#next code trial

# import os
# import json
# import sys
# import boto3

# # Initialize Bedrock client with region
# bedrock = boto3.client(
#     service_name="bedrock-runtime", 
#     region_name="ap-south-1"  # Use your specific region
# )
# print("imported successfully...")

# prompt = """
#     You are a smart assistant, so please let me know what is machine learning in the smartest way.
# """

# # Prepare the payload
# payload = {
#     "prompt": "[INST]" + prompt + "[/INST]",
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p": 0.9
# }

# # Convert payload to JSON
# body = json.dumps(payload)

# # Set the model ID
# model_id = "meta.llama3-70b-instruct-v1:0"

# # Invoke the model
# response = bedrock.invoke_model(
#     body=body,
#     modelId=model_id,  # Corrected parameter name
#     accept="application/json",
#     contentType="application/json"  # Corrected parameter name
# )

# # Print the full response for debugging
# print("Full Response:", response)

# # Process the response
# if "body" in response:
#     response_body_stream = response["body"]
#     response_body_str = response_body_stream.read().decode("utf-8")  # Read and decode response body
#     response_body = json.loads(response_body_str)  # Parse JSON
#     if "generation" in response_body:
#         response_text = response_body["generation"]
#         print("Generated Text:", response_text)
#     else:
#         print("Error: 'generation' key not found in the response body")
# else:
#     print("Error: 'body' key not found in the response")

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

prompt = "You are a smart assistant. Explain what machine learning is in a simple way."

# Prepare the payload
payload = {
    "prompt": "[INST]" + prompt + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9
}

# Convert payload to JSON
body = json.dumps(payload)

# Set the model ID
model_id = "meta.llama3-70b-instruct-v1:0"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,  # Corrected parameter name
    accept="application/json",
    contentType="application/json"  # Corrected parameter name
)

# Print the full response for debugging
print("Full Response:", response)

# Process the response by reading the body from the StreamingBody object
if "body" in response:
    response_body_stream = response["body"]
    response_body_str = response_body_stream.read().decode("utf-8")  # Read and decode response body
    print("Response Body String:", response_body_str)  # Print the entire response body string for debugging
    response_body = json.loads(response_body_str)  # Parse JSON

    # Print the entire response body to understand its structure
    print("Parsed Response Body:", response_body)

    # Check if 'generation' exists in the response
    if "generation" in response_body:
        response_text = response_body["generation"]
        print("Generated Text:", response_text)
    else:
        print("Error: 'generation' key not found in the response body")
else:
    print("Error: 'body' key not found in the response")
