# ------------------------------------------------------------------------------
# Check for missing parameters
# ------------------------------------------------------------------------------
[[ "$1" == "" ]] && echo "Missing 'Folder' Parameter" \
                 && echo "Usage: $(basename $0) sam-app-<number>" && exit

# ------------------------------------------------------------------------------
# Move to subfolder
# ------------------------------------------------------------------------------
cd $1

# ------------------------------------------------------------------------------
# Create S3 Bucket
# ------------------------------------------------------------------------------
ACCOUNT_NUMBER=$(aws sts get-caller-identity --query "Account" --output text)
DEPLOYMENT_BUCKET_NAME="cloud9-$ACCOUNT_NUMBER-sam-deployments-eu-west-1"
aws s3 mb s3://$DEPLOYMENT_BUCKET_NAME

# ------------------------------------------------------------------------------
# Package SAM template
# ------------------------------------------------------------------------------
sam package \
    --template-file template.sam.yaml \
    --s3-bucket $DEPLOYMENT_BUCKET_NAME \
    --output-template-file /tmp/packaged.yaml

[ $? != 0 ] && exit # exit if template cannot be packaged

# ------------------------------------------------------------------------------
# Deploy packaged SAM template
# ------------------------------------------------------------------------------
TEMPLATE_NAME="simple-sam-app"
sam deploy \
    --template-file /tmp/packaged.yaml \
    --stack-name $TEMPLATE_NAME \
    --capabilities CAPABILITY_IAM