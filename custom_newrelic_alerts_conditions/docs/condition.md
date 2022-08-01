# NewRelic::Alerts::Condition Condition

New Relic Condition object

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Integer</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#baselinedirection" title="BaselineDirection">BaselineDirection</a>" : <i>String</i>,
    "<a href="#nrql" title="Nrql">Nrql</a>" : <i><a href="nrql.md">Nrql</a></i>,
    "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#terms" title="Terms">Terms</a>" : <i>[ <a href="term.md">Term</a>, ... ]</i>,
    "<a href="#signal" title="Signal">Signal</a>" : <i><a href="signal.md">Signal</a></i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i><a href="expiration.md">Expiration</a></i>,
    "<a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>" : <i>Integer</i>
}
</pre>

### YAML

<pre>
<a href="#policyid" title="PolicyId">PolicyId</a>: <i>Integer</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#baselinedirection" title="BaselineDirection">BaselineDirection</a>: <i>String</i>
<a href="#nrql" title="Nrql">Nrql</a>: <i><a href="nrql.md">Nrql</a></i>
<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#terms" title="Terms">Terms</a>: <i>
      - <a href="term.md">Term</a></i>
<a href="#signal" title="Signal">Signal</a>: <i><a href="signal.md">Signal</a></i>
<a href="#expiration" title="Expiration">Expiration</a>: <i><a href="expiration.md">Expiration</a></i>
<a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>: <i>Integer</i>
</pre>

## Properties

#### PolicyId

Policy ID for the condition.

_Required_: No

_Type_: Integer

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Enabled

Whether the NRQL condition is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the NRQL condition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of condition.

_Required_: No

_Type_: String

_Allowed Values_: <code>STATIC</code> | <code>BASELINE</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### BaselineDirection

Direction in which the baseline is set on condition.

_Required_: No

_Type_: String

_Allowed Values_: <code>LOWER_ONLY</code> | <code>UPPER_ONLY</code> | <code>UPPER_AND_LOWER</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

The NRQL query that defines the signal for the condition.

_Required_: No

_Type_: <a href="nrql.md">Nrql</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The custom violation description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Terms

List of critical and warning terms for the condition.

_Required_: No

_Type_: List of <a href="term.md">Term</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signal

Configuration that defines the signal that the NRQL condition will use to evaluate.

_Required_: No

_Type_: <a href="signal.md">Signal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

Settings for how violations are opened or closed when a signal expires.

_Required_: No

_Type_: <a href="expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTimeLimitSeconds

Duration after which a violation automatically closes in seconds. Accepts values between 300 seconds (5 minutes) and 2592000 seconds (30 days). Default is 3 days (259200 seconds).

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

