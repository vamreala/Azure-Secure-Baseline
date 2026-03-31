# Azure-Secure-Baseline
## Zero Trust Web App

### The Problem: 
In traditional software development, apps often connect to databases or vaults using Connection Strings or API Keys hardocoded into the source code. 
The Risk:
If a developer accidentally pushes that coded to Github, or if a hacker gains access to the server's files, they steal the these secret keys. 
Whats the problem with using Keys? 
Rotating these passwords is a nightmare coz yo have to update and redeploy every single app that uses them. 
The Gap:
If someone uses a shared password to steal data, it is nearly impossible to tell which app/person was responsible. 

### The Solution:
I replaced the concept of passwords with an Identity.

#### Infrastructure as Code (Bicep):
I used Bicep to programmatically define a User-Assigned Managed Identity. This created a standalone "Digital ID" in Azure that exists independently of the code. 
<img width="1342" height="919" alt="image" src="https://github.com/user-attachments/assets/a8fe2db6-333f-4b74-94e6-92753d599583" />

#### Least Priviledge RBAC:
Instead of making the app a global admin, I used RBAC to give the identity exactly one permission (Key Vault Secret Officer). This ensure that even if the app is compromised, it can't delete the vault or change security settings. 
<img width="1308" height="619" alt="image" src="https://github.com/user-attachments/assets/bf9ea4f6-365e-43a9-a49e-75543ee1c788" />

#### Passwordless Authentication (Azure SDK):
I wrote a python code "app.py" using the DefaultAzureCredential library. This allowed the app to automatically present its ID card to the Azure backbone to get a temporary, short-lived token. 
<img width="1326" height="824" alt="image" src="https://github.com/user-attachments/assets/b9b4fea3-7d2f-454a-bc70-3b71c720c59a" />

### Results :)
No passwords in app.py. No connections strings in the environment variables. 
<img width="1410" height="760" alt="image" src="https://github.com/user-attachments/assets/4e1cb668-d2d7-4f4c-95e0-3d32fcd873a6" />

## Milestones:
☑️ Proved hat the logic works ona developer machine using personal Azure CLI credentials.
☑️ Successfully hosted the solution on Azure App Service (Linux).
☑️ Diagnosed and resolved Identity Scoping (400 errors) and Environment Mismatches using Azure Log stream. This demonstrated real-world cloud troubleshooting skills. 

Codes attached ---> 
the bicep file used to deploy;
the app.py code & requirements.txt 
