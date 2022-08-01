# NewRelic::Alerts::Condition Expiration

Settings for how violations are opened or closed when a signal expires.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#closeviolationsonexpiration" title="CloseViolationsOnExpiration">CloseViolationsOnExpiration</a>" : <i>Boolean</i>,
    "<a href="#expirationduration" title="ExpirationDuration">ExpirationDuration</a>" : <i>Integer</i>,
    "<a href="#openviolationsonexpiration" title="OpenViolationsOnExpiration">OpenViolationsOnExpiration</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#closeviolationsonexpiration" title="CloseViolationsOnExpiration">CloseViolationsOnExpiration</a>: <i>Boolean</i>
<a href="#expirationduration" title="ExpirationDuration">ExpirationDuration</a>: <i>Integer</i>
<a href="#openviolationsonexpiration" title="OpenViolationsOnExpiration">OpenViolationsOnExpiration</a>: <i>Boolean</i>
</pre>

## Properties

#### CloseViolationsOnExpiration

Whether to close all open violations when the signal expires. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationDuration

The amount of time (in seconds) to wait before considering if the signal has been lost. Max value of 172800 (48 hours).

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenViolationsOnExpiration

Whether to create a new lost signal violation to capture that the signal expired. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

