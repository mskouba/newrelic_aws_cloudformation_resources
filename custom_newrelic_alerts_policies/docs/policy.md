# NewRelic::Alerts::Policy Policy

New Relic Policy object

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#incidentpreference" title="IncidentPreference">IncidentPreference</a>" : <i>String</i>,
    "<a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>" : <i>[ Integer, ... ]</i>,
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#incidentpreference" title="IncidentPreference">IncidentPreference</a>: <i>String</i>
<a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>: <i>
      - Integer</i>
</pre>

## Properties

#### Name

Description of the policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentPreference

Determines how incidents are created for critical violations of the conditions contained in the policy.

_Required_: No

_Type_: String

_Allowed Values_: <code>PER_POLICY</code> | <code>PER_CONDITION</code> | <code>PER_CONDITION_AND_TARGET</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationChannels

Notification Channels attached to the policy

_Required_: No

_Type_: List of Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

