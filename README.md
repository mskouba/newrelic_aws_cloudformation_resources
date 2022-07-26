# New Relic AWS CloudFormation Resources

![CodeBuild Testing Suite](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiSkYxMnFVWWVGcE1QNEtqQzZyMzh1b2tYbUltbUJUcVBib2d3MEZDaGRYckZTMUxNR0NKbUtsS2ZSMGRIZFNBZnQ5ZnBBaFVMN1k1cC9ha0VRVEJ4ckJFPSIsIml2UGFyYW1ldGVyU3BlYyI6InhOWHZoWVBUVWY1M0F5R1YiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

### Custom AWS Cloudformation Resources for implementing alert infrastructure as code in New Relic

This repository is home to various custom resources for use in AWS CloudFormation templates. These can be used to manage new Relic alerting configurations such as policies, NRQL conditions, and notification channels via cloudformation.

### Requirements

- AWS CLI 
- SAM CLI
- Docker

### Installation

Step 1: Install Cloudformation CLI with the below command:

    pip3 install cloudformation-cli cloudformation-cli-python-plugin
    
Note that if cfn is not in path it will need to be added for the rest of the installation to work properly.


Step 2: Clone the repository with the below command:

    git clone https://github.com/mskouba/newrelic_aws_cloudformation_resources
    
Step 3: Enter the main directory and run the register_all.sh script

    cd newrelic_aws_cloudformation_resources
    source register_all.sh

To only install specific resources, navigate into the main folder for that resource and run the below command to submit it to your Cloudformation registry:

    cfn submit --set-default

Once this completes, you should see this resource in the resource registry by filtering to registered queries.


### Usage

In order to use these resources, simply define each resource in your template as you would any other resource. Detailed information on resource schema can be found in the README in each resource directory.

An example of a template featuring a sample policy, condition, and notification channel can be found below


    Resources:
        TestPolicy:
            Type: "NewRelic::Alerts::Policy"
            Properties:
                AccountId: <ADD NEW RELIC ACCOUNT ID HERE>
                ApiKey: <ADD NEW RELIC CREDENTIALS HERE>
                Policy:
                    Name: “Test Policy
                    IncidentPreference: "PER_CONDITION"
                    NotificationChannels: 
                        - !Ref TestChannel
        TestChannel:
            Type: "NewRelic::Alerts::NotificationChannel"
            Properties:
                AccountId: <ADD NEW RELIC ACCOUNT ID HERE>
                ApiKey: <ADD NEW RELIC CREDENTIALS HERE>
                NotificationChannel:
                    Name: “Test Notification Channel”
                    Type: "EMAIL"
                    Config:
                        Emails:
                            - “test@test.com"
                        IncludeJson: false
        TestCondition:
            Type: "NewRelic::Alerts::Condition"
            Properties:
                AccountId: <ADD NEW RELIC ACCOUNT ID HERE>
                ApiKey: <ADD NEW RELIC CREDENTIALS HERE>
                Condition:
                    Name: “Test Condition”
                    PolicyId: !Ref TestPolicy
                    Type: "STATIC"
                    Enabled: true
                    Nrql:
                        Query: "SELECT count(*) FROM Transaction"
                    Expiration:
                        CloseViolationsOnExpiration: true
                        ExpirationDuration: 600
                    Signal:
                        AggregationMethod: "EVENT_FLOW"
                        AggregationDelay: 120
                        AggregationWindow: 120
                    Terms:
                        - Operator: "ABOVE"
                          Priority: "WARNING"
                          Threshold: 2
                          ThresholdDuration: 360
                          ThresholdOccurrences: "ALL"
                        - Operator: "ABOVE"
                          Priority: "CRITICAL"
                          Threshold: 5
                          ThresholdDuration: 360
                          ThresholdOccurrences: "ALL"
                    ViolationTimeLimitSeconds: 3600









