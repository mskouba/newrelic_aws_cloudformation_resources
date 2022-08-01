# NewRelic::Alerts::Condition Term

critical and warning term for the condition.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#thresholdduration" title="ThresholdDuration">ThresholdDuration</a>" : <i>Integer</i>,
    "<a href="#thresholdoccurrences" title="ThresholdOccurrences">ThresholdOccurrences</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#thresholdduration" title="ThresholdDuration">ThresholdDuration</a>: <i>Integer</i>
<a href="#thresholdoccurrences" title="ThresholdOccurrences">ThresholdOccurrences</a>: <i>String</i>
</pre>

## Properties

#### Operator

Operator used to compare against the threshold.

_Required_: No

_Type_: String

_Allowed Values_: <code>ABOVE</code> | <code>ABOVE_OR_EQUALS</code> | <code>BELOW</code> | <code>BELOW_OR_EQUALS</code> | <code>EQUALS</code> | <code>NOT_EQUALS</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority determines whether notifications will be sent for violations or not.

_Required_: No

_Type_: String

_Allowed Values_: <code>CRITICAL</code> | <code>WARNING</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Value that triggers a violation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdDuration

The duration, in seconds, that the threshold must violate for in order to create a violation. This value must be within 60-7200 seconds and must be a multiple of the aggregation window.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdOccurrences

How many data points must be in violation for the specified thresholdDuration.

_Required_: No

_Type_: String

_Allowed Values_: <code>ALL</code> | <code>AT_LEAST_ONCE</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

