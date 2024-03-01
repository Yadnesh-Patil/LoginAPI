# LoginAPI
Registration and login using DRF.

Register API
POST : http://127.0.0.1:8000/register/
Content :  
            {
              "username": "xyz",
              "password": "xyz1234",
              "email": "xyz@gmail.com",
              "age":20,
              "phone":"9797979797",
              "gender":"Male"
            }

Response :   
            {
            "Token":"xyz",
            "resp":"User Register"
            }




Login API
POST : http://127.0.0.1:8000/login/
Content :  
            {
              "username": "xyz",
              "password": "xyz1234",
            }

Response :   
            {
            "Token":"xyz",
            "username": "xyz",
            "email": "xyz@gmail.com",
            "phone":"9797979797",
            "gender":"Male",
            "age":20
            }
