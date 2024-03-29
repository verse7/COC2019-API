import boto3
from flask_wtf.csrf import generate_csrf
from functools import wraps
from flask import request
from .model.User import User

def form_errors(form):
  error_messages = []
  for field, errors in form.errors.items():
    for error in errors:
      message = u"Error in the %s field - %s" % (
              getattr(form, field).label.text,
              error
          )
      error_messages.append(message)

  return error_messages


def gives_user(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    email = request.headers.get('email')
    if not email:
      return generate_api_response(40, "error", ['Email header not present'], {}, 200)

    user = User.query.filter_by(email=email).first()

    if not user:
      return generate_api_response(40, "error", ["User doesn't exist"], {}, 200)
    # print(f'user recieved {user}')
    return f(user, *args, **kwargs)
  return decorated


def generate_api_response(code, status, msg, data, http_status):
  # always generate a new csrf token on each response for xss protection
  data['csrf_token'] = generate_csrf()
  return {'code': code,'status': status, 'message': msg, 'data': data,}, http_status


class CDNManager():
  def __init__(self):
    self.__space_name = 'ecoyaad' # change to use an environment variable
    self.__url = 'https://coc2019v7.sfo2.digitaloceanspaces.com'
    self.__session = boto3.session.Session()
    self.__client = self.__session.client('s3',
                          region_name='sfo2',
                          endpoint_url= self.__url,
                          aws_secret_access_key='NSb+a2QHVIar5Ri4JjIRxYRsx54RZ7Z574gDFF5scQg',
                          aws_access_key_id='IFN5OP24AQXP5EK26RPP')

  def upload(self, local_file, filename):
    try:
      self.__client.upload_fileobj(
        local_file, self.__space_name, filename,
        ExtraArgs={
          'ACL': 'public-read',
          'ContentType': 'image/jpeg'
        }
      )
    except ClientError as e:
      print(f"There was an error uploading the file.\n {e}")
      return False
    return True

  def get_file_url(self, filename):
    return f'{self.__url}/{self.__space_name}/{filename}'
