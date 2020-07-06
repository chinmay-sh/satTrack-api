echo "### SatTrack API Docker Build ###"
versionTag=$1
if [ -z "$versionTag" ]; then
  echo "Need a version tag to build: For example ./buildDocker.sh v0.0.1"
  exit
fi
echo "Building SatTrack API for version: " $versionTag
docker build https://github.com/the-redlord/satTrack-api.git#$versionTag --tag sattrackapi:$versionTag
echo "Done building satTrack:$versionTag"
echo "Uploading to ECR"
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 605517810339.dkr.ecr.ap-south-1.amazonaws.com
docker tag sattrackapi:$versionTag 605517810339.dkr.ecr.ap-south-1.amazonaws.com/sattrack-api
docker push 605517810339.dkr.ecr.ap-south-1.amazonaws.com/sattrack-api
echo "Pushed to ECR with tag : " sattrackapi:$versionTag
