- import flask,boto3
-Creating Routes
  -creating / route
    - return render_template will render that html file
  - creating ec2 
    - create an create.html in which a form is there for input
    - set the action of form to /create_ec2
    - get the data from form in create_ec2 function and fetch the parameters
      - imageId -> imageId of AMI
      - Mincount -> Minimum number of EC2 instances to create
      - Maxcount -> Maximum number of EC2 instances to create
      - InstanceType -> type of instance

-Docker
  - Dockerfile
    - FROM python
    - COPY . /app
    - WORKDIR /app
    - RUN pip install -r requirements.txt
    - ENTRYPOINT [ "python" ]
    - CMD ["boto_api.py" ]

  
  - docker build -t my_app .
  - docker run -it -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION image-name
  - docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
  - sudo docker run -e Access_Key='' -e Access_secret='3' -e Region='us-east-1' -p 5000:5000 --name flask1 antima915/aws_flask:1.0
  -aws configure set aws_access_key_id "$Access_Key" && aws configure set  aws_secret_access_key "$Access_secret"  && aws configure set region "$Region"  && aws configure set output "none" 
  - https://docs.google.com/forms/d/e/1FAIpQLScxztDvO4LRZ90UksdHD3TiAOCAcxYu9NsaYXvz82X8BTv4AQ/viewform

  sudo docker run -it -e Access_Key='' -e Access_secret='' -e Region='us-east-1' -p 5001:5001 --name ec2 deepanshuinnovaccer/myec2:latest

 
