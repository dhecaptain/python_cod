import pandas as pd

def create_profile():
        user_profile ={}
        user_profile["first_name"] =input("enter first name:")
        user_profile["last_name"]=input("enter last name:")
        user_profile["email"]=input("enter email: ")
        user_profile["password"]=input("enter password: ")
        
        return user_profile

if __name__ == "__main__":
        my_profile=create_profile()
        
        print("Profile created")
        for key,value in my_profile.items():
                print(key,"=",value)
        
        dt=pd.DataFrame(my_profile)
        print(dt)
