Project Title: Zeachable Enrollment Feature
Project Description: This repository contains a scalable regression suite for the Zeachable Enrollment feature. It
tests the quality of the sign up feature for "My Awesome Course".

How to Install: 
1. set up your IDE, then git clone the repository to your local
2. pip install requirements.txt
3. download the latest chromedrive and store in /webdrivers
4. set the PATH to your chromedriver
   1. Note: if you are on a Mac, you will want to sudo chmod 755 the /webdrivers folder and also the executables inside 
   (chromedriver etc)
5. activate your virtual env
6. cd to a test suite, such as ~/zeachable/Features/Enrollment/test_signup_regression.py
7. in Terminal run the command: pytest test_signup_regression.py, this will run all the tests in the suite

Automation Architecture:

The test input data resides in the Constants.py and each test constant is a set of use cases, e.g, TEST_01_ENROLLMENT 
contains 6 test cases that run in 1 pytest test method.





