![](./img/img1.jpg)

yamerge
=======

###### Group merge script for Yammer... *sort of*.

In a nutshell, this little Python script allows a Yammer Group Administrator to add users from another group.

The caveat is that Yammer's API doesn't allow you to remove the member from the **old** group so that part will require manual intervention, which is a good thing... I guess.

In any event, the script is dead simple:
- Clone this repository
- Fire up a Python 3.6 virtual environment (you are using one, right?)
  - pip users: ```pip install -r requirements.txt```
  - pipenv users: ```pipenv install -r requirements.txt```
- [Get your Yammer Developer's token][token-link]
- [Get the Group IDs][group-link] from your Master (**source**) Group and Slave (**destination**) group
- Run this script and enjoy yams

```
  _   _  __ _ _ __ ___   ___ _ __ __ _  ___ 
 | | | |/ _` | '_ ` _ \ / _ \ '__/ _` |/ _ \
 | |_| | (_| | | | | | |  __/ | | (_| |  __/
  \__, |\__,_|_| |_| |_|\___|_|  \__, |\___|
  |___/                          |___/      

usage: run.py [-h] -dt DEV_TOKEN -mgid MASTER_GROUP_ID -sgid SLAVE_GROUP_ID

Yammer Group Merge Utility

optional arguments:
  -h, --help            show this help message and exit
  -dt DEV_TOKEN, --dev-token DEV_TOKEN
                        Yammer Developer's Token
  -mgid MASTER_GROUP_ID, --master-group-id MASTER_GROUP_ID
                        Group that contains the unique users that do not
                        belong to the Slave Group
  -sgid SLAVE_GROUP_ID, --slave-group-id SLAVE_GROUP_ID
                        Group that will receive the unique users from the
                        Master group
```

[token-link]:https://developer.yammer.com/docs/test-token
[group-link]:https://support.office.com/en-us/article/how-do-i-find-a-yammer-group-s-feedid-b0e49b2c-ca30-4025-b3bc-7bd764c3e2ec