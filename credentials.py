class Credentials:
    # Class that generates new instances of credentials.
   
    def __init__(self,account,password):

        self.account = account
        self.password = password
       
    credentials_list = [] # Empty credentials list
   
    def save_credential(self):
        # save_user method saves credentials objects into user_list
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        method that displays a list of user credentials.
        """
        return cls.credentials_list

    def delete_credentials(self):
        #function to delete users savd credentials
        Credentials.credentials_list.remove(self)


    listToDelete = ['abc', 'efg']
    arrayOfObjects = [{id:'abc',name:'oh'}, 
                      {id:'efg',name:'em'}, 
                      {id:'hij',name:'ge'}] 
    for i in arrayOfObjects.length:
        obj = arrayOfObjects[i]
        i+=0

    if (listToDelete.indexOf(obj.id) !== -1) {
        arrayOfObjects.splice(i, 1);
    

    @classmethod
    def user_exist(cls,account):
        """
         Class that generates new instances of Users.
        """
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True

        return False