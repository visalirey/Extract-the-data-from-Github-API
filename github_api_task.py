import requests
import lxml.html
import sys, json


html = requests.get('https://api.github.com/users')
##doc = lxml.html.fromstring(html.content)
json_data = json.loads(html.text)


filee=open('CSVdata_output.csv', 'a')
filee.write('User Id,User Login,User Name,Follower ID,Follower Login\n')    
CsvData_list=[]
for i in json_data:
    UserID=i['id']
    if int(UserID) % 5 == 0:
       
        UserLogin=i['login']
        UserName=i['login']
        FollowUrl=i['followers_url']
        Furl = requests.get(FollowUrl)
        url_data = json.loads(Furl.text)
        followersID=[]
        followersLogin=[]
        try:
            for url in url_data:
   
               
                followersID.append(str(url['id']))
                followersLogin.append(str(url['login']))
                break
        except:
            pass
           
        followersID=''.join(followersID)
        followersLogin=''.join(followersLogin)
        filee.write(str(UserID)+ ',' + str(UserLogin) + ',' + str(UserName) + ',' + followersID + ',' + followersLogin + '\n')
##        CsvData_list.append(data)
##        print(str(UserID)+ ',' + str(UserLogin) + ',' + str(UserName) + ',' + followersID + ',' + followersLogin)


filee.close()

