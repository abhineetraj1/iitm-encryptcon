# IIT Madras: Shaastra Ecryptcon 24hour hackathon

| Name | Content |
|--|:---:|
| Problem Statement | Digital Identity Solutions for Secure and Sustainable Banking |
| Track | Digital Identity Assurance |
| Challenge | Develop a self-sovereign digital identity solution that empowers customers to have more control over their personal data and identity verification processes within the banking ecosystem. |

## Installation
*	Download python3.11
*	Install required libraries
```
pip3 install flask
```
## Execution
*	Download the source code:-
```
git clone https://github.com/abhineetraj1/iitm-encryptcon
cd flask-web-hosting
```
*	Open terminal and run flask server
```
flask run -h localhost -p 5000
```
*	Open your default browser and navigate to localhost:5000 in that browser


## Features

*	Multi-factor authentication: Users verify their identity using customer ID, passcode, password, and date of birth.
*	During account setup, users establish a visual password by selecting a personal image. Upon subsequent logins, they'll be presented with a visual lineup of 10 images, including their chosen image. Successful identification of their image grants access to their dashboard, while incorrect choices trigger a security alert and redirect to the login screen.
*	Temporary ban for incorrect credentials: Mitigates security risks by imposing a 12-hour ban on user IDs after unsuccessful login attempts.
*	Inactivity timeout: Automatically expires inactive sessions to safeguard sensitive information (since this is a prototype we have set timer to 15 seconds).


## Languages and Tools:
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Authors
*	[Abhineet Raj](https://github.com/abhineetraj1) (Created prototype)
*	[Himanshu Singh](https://github.com/Himanshu040604) (Research and Development)