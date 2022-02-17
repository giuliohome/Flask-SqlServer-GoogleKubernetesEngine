#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed.
set -e -x

# Download and install required tools.
# pulumi
curl -L https://get.pulumi.com/ | bash
export PATH=$PATH:$HOME/.pulumi/bin

# Restore npm dependencies for our infra app.
yarn install

# Login into pulumi. This will require the PULUMI_ACCESS_TOKEN environment variable.
pulumi login

# Select the appropriate stack.
pulumi stack select giuliohome/gcp-flask-sqlserver/dev

set +o history
pulumi config set gcp:project mypulumi
pulumi config set gcp:zone us-west1-a
pulumi config set clusterPassword --secret $CLUSTER_PSWD
pulumi config set dbUsername dbappadmin
pulumi config set dbPassword --secret $DB_PSWD
pulumi config set dockerUsername giuliohome
pulumi config set dockerPassword --secret $DOCKER_PSWD
pulumi config set masterVersion latest
set -o history

# gcloud needed for deployment by pulumi
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
apt-get install apt-transport-https ca-certificates gnupg curl -y
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
apt-get update && apt-get install google-cloud-sdk -y

pulumi up --yes
