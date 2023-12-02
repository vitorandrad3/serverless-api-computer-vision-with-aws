from src.aws.rekognition.rekognition_client import rekognition
from src.models.error_model import APIError


def detect_labels(bucket, image_name):
    try:
        params = {
            "Image": {"S3Object": {"Bucket": bucket, "Name": image_name}},
            "MaxLabels": 50,
            "MinConfidence": 70,
        }

        data = rekognition.detect_labels(**params)

        print(data)

        labels = []

        for label in data["Labels"]:
            labels.append(
                {"Confidence": label["Confidence"], "Name": label["Name"]})

        return labels

    except rekognition.exceptions.InvalidS3ObjectException:
        raise APIError(status_code=404, message='Image not found!')

    except rekognition.exceptions.InvalidParameterException:
        raise APIError(status_code=406,
                       message='Invalid parameter (bucket or image name) type')

    except rekognition.exceptions.AccessDeniedException:
        raise APIError(status_code=401, message="Invalid Credentials")

    except rekognition.exceptions.InvalidImageFormatException:
        raise APIError(status_code=406, message="Invalid image format")

    except Exception as err:
        raise APIError(status_code=500, message=f"unexpected error: {str(err)}")
