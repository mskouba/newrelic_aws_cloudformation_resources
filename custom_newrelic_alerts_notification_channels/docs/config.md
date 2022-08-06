# NewRelic::Alerts::NotificationChannel Config

Configuration items for notification channel such as API keys, integration URLs, etc.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emails" title="Emails">Emails</a>" : <i>[ String, ... ]</i>,
    "<a href="#includejson" title="IncludeJson">IncludeJson</a>" : <i>Boolean</i>,
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
    "<a href="#datacenterregion" title="DataCenterRegion">DataCenterRegion</a>" : <i>String</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#teams" title="Teams">Teams</a>" : <i>[ String, ... ]</i>,
    "<a href="#teamchannel" title="TeamChannel">TeamChannel</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#routekey" title="RouteKey">RouteKey</a>" : <i>String</i>,
    "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
    "<a href="#basicauth" title="BasicAuth">BasicAuth</a>" : <i><a href="config.md">Config</a></i>,
    "<a href="#customhttpheaders" title="CustomHttpHeaders">CustomHttpHeaders</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
    "<a href="#custompayloadbody" title="CustomPayloadBody">CustomPayloadBody</a>" : <i>String</i>,
    "<a href="#custompayloadtype" title="CustomPayloadType">CustomPayloadType</a>" : <i>String</i>,
    "<a href="#integrationurl" title="IntegrationUrl">IntegrationUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#emails" title="Emails">Emails</a>: <i>
      - String</i>
<a href="#includejson" title="IncludeJson">IncludeJson</a>: <i>Boolean</i>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
<a href="#datacenterregion" title="DataCenterRegion">DataCenterRegion</a>: <i>String</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#teams" title="Teams">Teams</a>: <i>
      - String</i>
<a href="#teamchannel" title="TeamChannel">TeamChannel</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#routekey" title="RouteKey">RouteKey</a>: <i>String</i>
<a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
<a href="#basicauth" title="BasicAuth">BasicAuth</a>: <i><a href="config.md">Config</a></i>
<a href="#customhttpheaders" title="CustomHttpHeaders">CustomHttpHeaders</a>: <i>
      - <a href="config.md">Config</a></i>
<a href="#custompayloadbody" title="CustomPayloadBody">CustomPayloadBody</a>: <i>String</i>
<a href="#custompayloadtype" title="CustomPayloadType">CustomPayloadType</a>: <i>String</i>
<a href="#integrationurl" title="IntegrationUrl">IntegrationUrl</a>: <i>String</i>
</pre>

## Properties

#### Emails

List of email recipients

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeJson

Setting to determine whether payload JSON will be sent in email

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

API Key for OpsGenie and PagerDuty notification channel types

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataCenterRegion

OpsGenie Data Center

_Required_: No

_Type_: String

_Allowed Values_: <code>EU</code> | <code>US</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

List of email recipients for OpsGenie Notification Channels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags for OpsGenie Notification Channels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

Teams for OpsGenie Notification Channels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamChannel

Slack channel name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Slack channel URL

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

VictorOps Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteKey

VictorOps route key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseUrl

Webhook base URL

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicAuth

_Required_: No

_Type_: <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHttpHeaders

Custom HTTP headers

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPayloadBody

Custom Payload body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPayloadType

Webhook custom payload type

_Required_: No

_Type_: String

_Allowed Values_: <code>FORM</code> | <code>JSON</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationUrl

xMatters integration URL

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

