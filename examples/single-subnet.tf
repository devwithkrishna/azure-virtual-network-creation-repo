module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-terraform-modules.git//virtual-network?ref=feature/user-assigned-managed-identity"

  # Optional variables

  application_name    = "devwithkrishna"
  environment         = "dev"
  temporary           = "true"
  location            = "southindia"
  resource_group_name = "architects-south-india-vnet-rg"
  subnet_cidrs        = ["10.247.0.0/24", "10.247.0.1/24"]
  vnet_address_space  = ["10.247.0.0/23"]
  vnet_name           = "architects-south-india-vnet"
}