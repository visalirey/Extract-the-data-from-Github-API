# Extract-the-data-from-Github-API
Extract the data From website
Extract the data from URL using python code. In This project Extract the data from Github url to get user details.

How to run the code

download the below source code and save into your local machine. preferably use idle/pycharm/visual studio code editor

Run the code you get output like csv format

During run the program some other time you got this type of error

Traceback (most recent call last): File "C:\Users\adminpc\Documents\apton\github.py", line 14, in UserID=i['id'] TypeError: string indices must be integers

This error like Rate limit issue. Github allow only 60 API calls per hour so that issue occur.

the same time you check your url link 'https://api.github.com/users' you got the following message from your browser.

'''{"message":"API rate limit exceeded for 106.76.45.181. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)","documentation_url":"https://developer.github.com/v3/#rate-limiting"}'''

possible way to avoid this issue:

1.if you got rate limit error alternatively use your internet connection like use different wifi hotspots/ modem connection. or 2. download the data from url to save your local machine and run the program.
