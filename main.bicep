// 1. SCOPE: Deploying to a Resource Group
targetScope = 'resourceGroup'

// 2. PARAMETERS: Using my verified allowed region
param location string = 'polandcentral' 
param vaultName string = 'sec-vlt-${uniqueString(resourceGroup().id)}'

// 3. THE IDENTITY: The "ID Card" for my apps
resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'web-app-identity'
  location: location
}

// 4. THE VAULT: The "Secure Safe" for secrets
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: vaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true // 2026 Security standard: Role-Based Access
    enabledForDeployment: true
    enabledForTemplateDeployment: true
  }
}

// 5. OUTPUTS: For verification
output vaultUri string = keyVault.properties.vaultUri
