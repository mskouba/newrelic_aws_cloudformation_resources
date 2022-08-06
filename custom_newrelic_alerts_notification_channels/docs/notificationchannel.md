# NewRelic::Alerts::NotificationChannel NotificationChannel

New Relic Notification Channel Object

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#config" title="Config">Config</a>" : <i><a href="config.md">Config</a></i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#config" title="Config">Config</a>: <i><a href="config.md">Config</a></i>
</pre>

## Properties

#### Name

Name of the notification channel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the type of notification channel.

_Required_: No

_Type_: String

_Allowed Values_: <code>email</code> | <code>opsGenie</code> | <code>pagerDuty</code> | <code>slack</code> | <code>victorOps</code> | <code>webhook</code> | <code>xMatters</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Config

Configuration items for notification channel such as API keys, integration URLs, etc.

_Required_: No

_Type_: <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

