#!/bin/bash
#
# Script to easily install all custom resources in one command 
# Conditions
cd custom_newrelic_alerts_conditions &&
cfn submit --set-default &&
cd .. 
# Policies
cd custom_newrelic_alerts_policies &&
cfn submit --set-default &&
cd .. 
# Notification Channels
cd custom_newrelic_alerts_notification_channels &&
cfn submit --set-default &&
cd .. 
