#!/bin/sh

echo "Beginning Policy Test"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

template=$( cat $SCRIPT_DIR/policy-test-template.yml )
stack_arn=$( aws cloudformation create-stack --stack-name "policy-test-template" \
--template-body $template \
--parameters ParameterKey=NewRelicAccountId,ParameterValue=$NewRelicAccountId ParameterKey=NewRelicApiKey,ParameterValue=$NewRelicApiKey \
--output text )

echo $stack_arn
echo "Waiting for Cloudformation stack to complete"

if aws cloudformation wait stack-create-complete --stack-name $stack_arn ; then
  echo "Stack created successfully"
else
  echo "Stack creation failed"
fi
