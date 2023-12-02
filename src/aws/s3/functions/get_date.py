from src.utils.format_date import format_date
from src.aws.s3.s3_client import s3
from src.models.error_model import APIError


def get_date(bucket_name, image_name):

    try:
        response = s3.get_object(Bucket=bucket_name, Key=image_name)

        last_modified_date = response["LastModified"]
        date_str = str(last_modified_date)

        date = format_date(date_str)

        return date

    except s3.exceptions.NoSuchKey:
        raise APIError(status_code=404, message='Object not found')

    except s3.exceptions.InvalidObjectState:
        raise APIError(status_code=410, message='Object not available')

    except Exception as err:
        raise APIError(status_code=500, message=f"unexpected error: {str(err)}")
