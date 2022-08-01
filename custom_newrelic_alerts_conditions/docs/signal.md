# NewRelic::Alerts::Condition Signal

Configuration that defines the signal that the NRQL condition will use to evaluate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregationdelay" title="AggregationDelay">AggregationDelay</a>" : <i>Integer</i>,
    "<a href="#aggregationmethod" title="AggregationMethod">AggregationMethod</a>" : <i>String</i>,
    "<a href="#aggregationtimer" title="AggregationTimer">AggregationTimer</a>" : <i>Integer</i>,
    "<a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>" : <i>Integer</i>,
    "<a href="#filloption" title="FillOption">FillOption</a>" : <i>String</i>,
    "<a href="#fillvalue" title="FillValue">FillValue</a>" : <i>Integer</i>,
    "<a href="#slideby" title="SlideBy">SlideBy</a>" : <i>Integer</i>
}
</pre>

### YAML

<pre>
<a href="#aggregationdelay" title="AggregationDelay">AggregationDelay</a>: <i>Integer</i>
<a href="#aggregationmethod" title="AggregationMethod">AggregationMethod</a>: <i>String</i>
<a href="#aggregationtimer" title="AggregationTimer">AggregationTimer</a>: <i>Integer</i>
<a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>: <i>Integer</i>
<a href="#filloption" title="FillOption">FillOption</a>: <i>String</i>
<a href="#fillvalue" title="FillValue">FillValue</a>: <i>Integer</i>
<a href="#slideby" title="SlideBy">SlideBy</a>: <i>Integer</i>
</pre>

## Properties

#### AggregationDelay

How long we wait for data that belongs in each aggregation window. Depending on your data, a longer delay may increase accuracy but delay notifications. Use aggregationDelay with the EVENT_FLOW and CADENCE methods. The maximum delay is 1200 seconds (20 minutes) when using EVENT_FLOW and 3600 seconds (60 minutes) when using CADENCE. In both cases, the minimum delay is 0 seconds and the default is 120 seconds. When using aggregationDelay, do not use evaluationOffset.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregationMethod

The method that determines when we consider an aggregation window to be complete so that we can evaluate the signal for violations. Default is EVENT_FLOW. When using any aggregationMethod, do not use evaluationOffset. When using the aggregationMethod with EVENT_TIMER, use aggregationTimer. For EVENT_FLOW and CADENCE, use aggregationDelay.

_Required_: No

_Type_: String

_Allowed Values_: <code>EVENT_FLOW</code> | <code>EVENT_TIMER</code> | <code>CADENCE</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregationTimer

How long we wait after each data point arrives to make sure we've processed the whole batch. Use aggregationTimer with the EVENT_TIMER method. The timer value can range from 5 seconds to 1200 seconds (20 minutes); the default is 60 seconds. When using aggregationTimer, do not use evaluationOffset.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregationWindow

Aggregation window controls the duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillOption

Option that determines the type of value that should be used to fill gaps (empty windows). Defaults to STATIC. Outlier NRQL conditions may only use NONE.

_Required_: No

_Type_: String

_Allowed Values_: <code>LAST_VALUE</code> | <code>NONE</code> | <code>STATIC</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillValue

If using the static fill option, this the value used for filling. Defaults to 0.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlideBy

This setting gathers data in overlapping time windows to smooth the chart line, making it easier to spot trends. The slideBy value is specified in seconds and must be smaller than and a factor of the aggregationWindow.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

