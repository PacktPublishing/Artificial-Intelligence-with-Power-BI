# Import necessary libraries
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Connect to API through subscription key and endpoint
subscription_key = "<your-subscription-key>"
endpoint = "https://<your-cognitive-service>.cognitiveservices.azure.com/"

# Authenticate
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Get image
local_image = open("images/objects6.jpeg", "rb")

# Call API
detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image)

# Return the result
print("Detected objects in image:")
if len(detect_objects_results_local.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results_local.objects:
        print(object.object_property, object.confidence)
print()