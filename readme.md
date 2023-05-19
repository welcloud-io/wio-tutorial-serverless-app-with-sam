# Building a simple serverless app with AWS SAM

This is a very simple tutorial to learn how to build a very simple web application wit SAM (Serverless Application Model)

#### Application architecture

![](images/simple-serverless-app-architecture.png)

#### Tutorial overview

- First we create the landing page (API Gateway + Lambda) 
- Second we create the click counter (API Gateway + Lambda + DynamoDB)
- Third we create the feedback feature ((API Gateway + Lambda + SNS)

#### Setup:

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

#### Tutorial steps

##### Prepare for deployment
* Go to the 'wio-tutorial-serverless-app-with-sam' folder on the left in cloud9
* Open _deploy.sh
* Click on 'Run'
* You should see a new tab opening, with an error message 
starting with *Missing 'Folder' Parameter*, which is normal

##### Deploy "hello" landing page (samp-app-00)
* Go to the 'wio-tutorial-serverless-app-with-sam/sam-app-00' folder
* Open template.sam.yaml file
* Explore the template file
* Open the landing page function that will be deployed 'landing-page-function/landing_page_function.py'
* Add 'sam-app-00' in the Command of the _deploy.sh tab that was opened previously
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

#### Upate the landing page with a Button to click on
* Explore 'sam-app-02/landing-page-function' folder
* Add 'sam-app-02' in the Command of the _deploy.sh tab that was opened previously
* Click the 'Run' button at the top left of this tab
* You should see the app deploying with messages in the tab (updating the previous stack) 
* When done refresh the page containing the landing page (or re-execute the previous test paragraph)






