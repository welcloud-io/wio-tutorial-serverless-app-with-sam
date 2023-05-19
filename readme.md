# Building a simple serverless app with AWS SAM

This is a very simple tutorial to learn how to build a very simple web application wit SAM (Serverless Application Model)

## Application architecture

![](images/simple-serverless-app-architecture.png)

## Tutorial overview

- First we create a function that will return a landing page (API Gateway + Lambda) 
- Second we create a function that will record clicks in a table (API Gateway + Lambda + DynamoDB)
- Third we create a function that will record feedback in a table and send a confirmation email (API Gateway + Lambda + DynamoDB + SNS)

## Setup

* Connect to your AWS account
* Create a Cloud9 environment 
    * Open Cloud9 Service
    * Click on 'Create Environment'
        * Name: serverless-app-tutorial
        * Click on 'Create'
        * CLick on 'Open' (Wait for about one minute)
        * Close welcome page and Immediate Tab
        * Delete Readme.txt (.c9 should then disappear)
        
* Clone this repository
    * Go to Cloud9 terminal
    * execute: ```git clone https://github.com/welcloud-io/wio-tutorial-serverless-app-with-sam.git```

## Tutorial steps

##### Prepare for deployment
* Go to the 'wio-tutorial-serverless-app-with-sam' folder on the left in cloud9
* Open _deploy.sh
* Click on 'Run'
* You should see a new tab opening, with an error message 
starting with *Missing 'Folder' Parameter*, which is normal

### *sam-app-00*

##### Deploy "hello" landing page
* Go to the 'wio-tutorial-serverless-app-with-sam/sam-app-00' folder
* Open template.sam.yaml file
* Explore the template file
* Open the landing page function that will be deployed 'landing-page-function/landing_page_function.py'
* Add 'sam-app-00' in the Command field of the _deploy.sh tab that was opened previously
* Click the 'Run' button at the top left of this tab
* You should see the app deploying with messages in the tab
* When done open a new AWS Console (From Cloud9 - AWS Cloud9 [up-left] / Go to your dashboard)
* Open CloudFormation service & Explore simple-sam-app stack

##### Test the "hello" landing page
* Open Api Gateway Service
* Click on 'simple-sam-app' in the list
* Click on the invoke url starting with 'https://...'
* You should se your landing displaying 'hello'

##### View the deployed lambda function
* On the API Gateway service page, in the 'simple-sam-app' page
* Click on integrations
* Click on Get
* Click on 'Manage Integration' button
* Click on the link next to the lambda function & region (this will open the lambda)
* Explore lambda function page

### *sam-app-02*

##### Upate the landing page with a Button you can click on
* Explore files in 'sam-app-02/landing-page-function' folder
* Add 'sam-app-02' in the Command field of the _deploy.sh tab that was opened previously
* Click the 'Run' button at the top left of this tab
* You should see the app deploying with messages in the tab (updating the previous stack) 
* When done refresh the page containing the landing page (or re-execute the previous test paragraph)

### *sam-app-04*

##### Add a table to persist the number of clicks
* Explore files in 'sam-app-04/landing-page-function' folder
* Verify that each time you'll click you will post a query to a /click route of your api endpoint
* Explore files in 'sam-app-04/click-function' folder
* Verify that each time this function is executed, it will update a dynamodb table item
* Explore 'sam-app-04/template.sam.yaml'
* Verify the new Click function is decribed with the appropriate route
* Verify that the templates will create a dynamodb table
* Add 'sam-app-04' to in the Command field of the _deploy.sh tab that was opened previously

##### Test that the number of clicks is persisted into the table
* When deployment is done Refresh the page containing the landing page (or re-execute the previous test paragraph)
* Hit F12 in your web browser to open the developer tools, select network tab to see api calls
* Click on the [CLICK] button of the landing page, you should see the api calls in developer tools
* Go to the aws console
* Go to the dynamodb service
* Click on the simple-sam-app-ClickTable-... Table
* Click on 'Explore table Items'
* Verify the item containing the number of clicks is there
* Click on the [CLICK] button of the landing page
* Verify the table is updated

### *sam-app-06*

#### Persist a feedback in the dynamodb table and send a confirmation email when recorded
* Explore files in 'sam-app-06/landing-page-function' folder 
* Verify we now send a feedback to be persisted into the dynamodb table
* Explore files in 'sam-app-06/send-feedback-function' folder 
* Verify the function will now persist a feedback and send it to an sns topic (associated with an email)
* Explore sam template files
* Verify we create a new table and an sns topic
* IMPORTANT: under Subscription, replace Endpoint value with your Email
* Add 'sam-app-06' to in the Command field of the _deploy.sh tab that was opened previously

##### Test you receive a feedback from the app
* When deployment is done Refresh the page containing the landing page (or re-execute the previous test paragraph)
* IMPORTANT: Go to your mailbox and confirm the subscription you received (click the link in the email)
* Fill in the form in the landing and click on [SEND]
* Check the feed back is recorded in the simple-sam-app-FeedbackTable-.. dynamodb table
* Check that the user receive a confirmation of it's feedback

## Clean things up
* Go to Cloudformation service
* Select 'simple-sam-app', click [Delete] and [Delete] Again
* Go to cloud9 service 
* Select 'serverless-app-tutorial', click [Delete] and type Delete