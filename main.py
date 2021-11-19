import jenkins
from jenkins import Jenkins

conn = Jenkins(url="https://3c003a52d93b4cb98f4c4abe9364fb04.vfs.cloud9.us-east-1.amazonaws.com/", username="admin", password="112e06657ed8f5888207e76ca29ff970c4")
#Note: password is token generated in jenkins
conn.get_info()



