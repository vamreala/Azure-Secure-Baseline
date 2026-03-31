from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Your specific Vault URL
vault_url = "https://sec-vlt-iucu5oltitgw6.vault.azure.net/"

print("--- Identity-over-Password Proof ---")

try:
    print("Step 1: Requesting token via DefaultAzureCredential...")
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    print(f"Step 2: Connecting to Vault: {vault_url}")
    
    # Fetching the secret
    secret_name = "MyFirstSecret"
    retrieved_secret = client.get_secret(secret_name)

    print("---------------------------------------")
    print(f"SUCCESS! Secret Name: {retrieved_secret.name}")
    print(f"SUCCESS! Secret Value: {retrieved_secret.value}")
    print("---------------------------------------")
    print("PROJECT COMPLETE: Zero Trust Identity Verified.")

except Exception as e:
    print(f"\nOops! Something went wrong:\n{e}")
