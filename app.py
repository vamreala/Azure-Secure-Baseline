from flask import Flask
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

@app.route("/")
def index():
    try:
        # 1. Pull the Vault URL from the App Settings we set in Step 3
        vault_url = os.environ.get("VAULT_URL")
        
        # 2. THE IDENTITY MAGIC: 
        # DefaultAzureCredential will automatically detect the 
        # Tell the app exactly which ID to use
        credential = DefaultAzureCredential(managed_identity_client_id="385449eb-1d00-49ed-bd1a-2e8d4b0b9164")
        client = SecretClient(vault_url=vault_url, credential=credential)
        
        # 3. Request the secret from the vault
        secret_name = "MyFirstSecret"
        retrieved_secret = client.get_secret(secret_name)
        
        # 4. Return a clean, dark-themed UI (AMBV Style)
        return f"""
        <html>
            <head><title>AMBV | Secure Portal</title></head>
            <body style="background-color: #222222; color: #f8f8f8; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
                <div style="border: 1px solid #444; padding: 40px; border-radius: 8px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
                    <h1 style="letter-spacing: 2px; text-transform: uppercase;">Identity Verified</h1>
                    <hr style="border: 0; border-top: 1px solid #444; margin: 20px 0;">
                    <p style="font-size: 1.2rem;">Vault Secret: <span style="color: #00ff00; font-weight: bold;">{retrieved_secret.value}</span></p>
                    <p style="font-size: 0.8rem; color: #888; margin-top: 20px;">Zero-Trust Architecture | Identity-over-Password</p>
                </div>
            </body>
        </html>
        """
    except Exception as e:
        return f"<body style='background:#222; color:#ff5555; padding:20px;'><h1>Security Error</h1><p>{str(e)}</p></body>"

if __name__ == "__main__":
    # Local dev tip: Flask usually runs on port 5000 or 8000
    app.run()