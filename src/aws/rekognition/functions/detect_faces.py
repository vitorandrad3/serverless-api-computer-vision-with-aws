from src.aws.rekognition.rekognition_client import rekognition
from src.models.error_model import APIError


def get_faces_and_emotions(bucket, image_name):
    try:
        response = rekognition.detect_faces(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": image_name,
                }
            },
            Attributes=["EMOTIONS"],
        )
        
        print(response)

        informations_list = []
        
        if response['FaceDetails']:
            for face in response["FaceDetails"]:
                informations = {}
                informations["positon"] = face["BoundingBox"]
                informations["classified_emotion"] = face["Emotions"][0]["Type"]
                informations["classified_emotion_confidence"] = face["Emotions"][0]["Confidence"]
                informations_list.append(informations)
        else:
            informations_list.append({"position":{"Height": None, "Left": None, "Top": None, "Width": None},"classified_emotion": None, "classified_emotion_confidence": None})

        return informations_list
    
    except rekognition.exceptions.InvalidS3ObjectException:
        raise APIError(status_code=404, message='Image not found!')
    except rekognition.exceptions.InvalidParameterException:
        raise APIError(status_code=404,
                       message='Invalid parameter (bucket or image name) type')
    except rekognition.exceptions.AccessDeniedException:
        raise APIError(status_code=401, message='Invalid Credentials')

    except Exception as err:
        raise APIError(status_code=500, message=f'unexpected error: {str(err)}')
