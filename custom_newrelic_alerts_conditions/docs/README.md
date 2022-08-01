# NewRelic::Alerts::Condition

Resource that manages New Relic Alert Condition object.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "NewRelic::Alerts::Condition",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Integer</i>,
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i><a href="condition.md">Condition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: NewRelic::Alerts::Condition
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Integer</i>
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#condition" title="Condition">Condition</a>: <i><a href="condition.md">Condition</a></i>
</pre>

## Properties

#### AccountId

New Relic Account ID.

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

New Relic API Key with permissions for NerdGraph

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

New Relic Condition object

_Required_: Yes

_Type_: <a href="condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Id

Returns the <code>Id</code> value.

