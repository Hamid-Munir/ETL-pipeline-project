# This is group project I did during Data engineering program with two other members

## What is this project 

This project involves creating an ETL pipeline for a cafe chain, getting their raw data in CSV straight to an s3 bucket and using the lambda function to perform ETL which loads straight to Redshift.

After which we used ec2 to install docker and load grafana image, next step was connecting grafana to redshift which allowed us to make a live interactive dashboard filled with info about different key elements of cafe chains. 

We used serverless framework and GitHub actions to deploy this and make changes to the pipeline as required. 



</br>
</br>

## To use this program
you need [Python](https://www.python.org/downloads/) 3.8 +

you need aws set up with all the passwords and keys in github secrets to deploy this pipleline 

### Future plans

I will try to make some changes and play around bit more as long as I have AWS access