<a name="br1"></a> 

**Automated AWS Lambda EBS Volume Type**

**Conversion Triggered by CloudWatch Events**

**Summary:**

This AWS Lambda function facilitates the seamless conversion of Amazon Elastic Block

Store (EBS) volumes from the "gp2" type to "gp3" type. Triggered by CloudWatch Events, the

Lambda handler extracts volume ARNs, employs a custom function for ARN separation, and

utilizes the AWS Boto3 SDK to modify the volume type. The solution ensures efficiency in

managing EBS volumes, responding dynamically to specified CloudWatch Events, and

optimizing storage costs by transitioning to the high-performance "gp3" volume type. The

implementation includes error handling, making it a reliable and automated tool for EBS volume

management in AWS environments.

**Task:**

**AWS Credentials:**

●

Ensure that your AWS credentials are properly configured on the environment where the Lambda

function will run.

**Lambda Function:**

●

●

●

Create a new Lambda function in the AWS Management Console.

Upload the provided Python code or copy-paste it directly.

Configure the function settings, including memory, timeout, and execution role.

**CloudWatch Events:**

●

●

Set up a CloudWatch Events rule to trigger the Lambda function.

Define the event pattern to capture the desired events that should trigger the EBS volume type

conversion.

**Functionality**

**arn\_separation(volume\_arn)**

This function separates the volume ID from an EBS volume ARN. It assumes that the volume ID is the

last part of the ARN after the last '/' character.



<a name="br2"></a> 

**lambda\_handler(event, context)**

The main Lambda handler function:

●

●

●

Extracts the volume ARN from the incoming CloudWatch Event.

Utilizes arn\_separation to obtain the volume ID.

Uses the EC2 client from Boto3 to modify the volume type to 'gp3'.

**Conclusion**

This solution streamlines EBS volume management, offering an automated and cost-effective

approach to transitioning volumes to the high-performance 'gp3' type in response to CloudWatch

Events.

