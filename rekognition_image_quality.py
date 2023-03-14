import boto3

rek_client = boto3.client('rekognition')

image_file = 'images/combi-10-blur.jpg'
with open(image_file, 'rb') as image:
    # https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html
    response = rek_client.detect_labels(Image={'Bytes': image.read()}, Features=["GENERAL_LABELS", "IMAGE_PROPERTIES"])
    #img_quality = rek_client.image_quality(Image={'Bytes': image.read()})
#print(img_quality)
print(response["ImageProperties"]["Quality"])

labels = response['Labels']
print(f'Found {len(labels)} labels in the image:')
for label in labels:
    name = label['Name']
    confidence = label['Confidence']
    print(f'> Label "{name}" with confidence {confidence:.2f}')

# images/combi-sharp.jpg
# {'Brightness': 51.078861236572266, 'Sharpness': 80.0966796875, 'Contrast': 82.39337921142578}
# Found 15 labels in the image:
# > Label "Caravan" with confidence 100.00
# > Label "Transportation" with confidence 100.00
# > Label "Van" with confidence 100.00
# > Label "Vehicle" with confidence 100.00
# > Label "Car" with confidence 98.14
# > Label "Bus" with confidence 90.10
# > Label "Machine" with confidence 76.35
# > Label "Wheel" with confidence 76.35
# > Label "Person" with confidence 57.88
# > Label "Outdoors" with confidence 56.36
# > Label "Spoke" with confidence 56.27
# > Label "Minibus" with confidence 56.23
# > Label "Alloy Wheel" with confidence 55.61
# > Label "Car Wheel" with confidence 55.61
# > Label "Tire" with confidence 55.61

# {'Brightness': 51.911590576171875, 'Sharpness': 34.53408432006836, 'Contrast': 81.10663604736328}
# Found 14 labels in the image:
# > Label "Caravan" with confidence 100.00
# > Label "Transportation" with confidence 100.00
# > Label "Van" with confidence 100.00
# > Label "Vehicle" with confidence 100.00
# > Label "Car" with confidence 99.58
# > Label "Machine" with confidence 89.24
# > Label "Wheel" with confidence 89.24
# > Label "Bus" with confidence 57.55
# > Label "Alloy Wheel" with confidence 57.31
# > Label "Car Wheel" with confidence 57.31
# > Label "Spoke" with confidence 57.31
# > Label "Tire" with confidence 57.31
# > Label "Minibus" with confidence 57.22
# > Label "Outdoors" with confidence 55.41