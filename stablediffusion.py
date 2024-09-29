# import boto3
# import json
# import base64
# import os

# prompt= "provide me one 4k hd image of person who is swimming in the river."

# prompt_template= [{"text":prompt,"weight":1}]
# bedrock= boto3.client(service_name= "bedrock-runtime")
# payload={
#     "text_prompts":prompt_template,
#     "cfg_scale":10,
#     "seed":0,
#     "steps":50,
#     "width":512,
#     "height":512

# }
# body= json.dumps(payload)
# model_id= "amazon.titan-image-generator-v2:0"

# response= bedrock.invoke_model(
#     body=body,
#     modelId=model_id,
#     accept="application/json",
#     contentType="application/json"
# )

# response_body= json.loads(response.get("body").read())
# print(response_body)

# artifacts=response_body.get("artifacts")[0]
# image_encoded=artifacts.get("base64").encode('utf-8')
# image_bytes=base64.b64decode(image_encoded)

# output_dir= "output"
# os.makedirs(output_dir, exist_ok= True)
# file_name= f"{output_dir}/generated-img.png"
# with open(file_name,"wb") as f:
#     f.write(image_bytes)


import boto3
import json
import base64
import os

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="ap-south-1")

# Define the prompt
prompt = "Generate a 4K HD image of a beautiful river landscape."

# Prepare the payload
# payload = {
#     "text_prompts": [{"text": prompt, "weight": 1}],
#     "cfg_scale": 10,
#     "seed": 123,  # Use non-zero seed
#     "steps": 50,
#     "width": 512,
#     "height": 512
# }

payload={
    "taskType":"TEXT_IMAGE",
    "textToImageParams":{
        "text":prompt
    },
    "imageGenerationConfig":{
        "numberOfImages":1,
        "height":512,
        "width":512,
        "cfgScale":10,
        "seed":0
    }
}



# Convert payload to JSON
body = json.dumps(payload)

# Set the correct model ID for Titan Image Generator
model_id = "amazon.titan-image-generator-v1"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Process the response
response_body = json.loads(response['body'].read().decode('utf-8'))
print("Full Response:", response_body)

# Extract the image data
artifacts = response_body.get("artifacts", [])[0]
image_encoded = artifacts.get("base64", "").encode('utf-8')

# Decode the image and save it as a PNG file
image_bytes = base64.b64decode(image_encoded)
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-image.png"

with open(file_name, "wb") as f:
    f.write(image_bytes)

print(f"Image saved successfully at {file_name}")