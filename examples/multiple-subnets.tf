module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-terraform-modules.git//virtual-network?ref=feature/user-assigned-managed-identity"

  # Optional variables

  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "true"
  location            = "southindia"
  resource_group_name = "architectsds-south-india-VNET-rg"
  subnet_cidrs        = ["10.247.0.0/24", "10.247.1.0/24"]
  vnet_address_space  = ["10.247.0.0/23"]
  vnet_name           = "architectsds-south-india-VNET"
}

##############################################################################################################################
# Based on the number of subnet_cidrs values provided, that many subnets will be created
#
# Lets say this is the subnet_cidrs = ["10.247.0.0/24", "10.247.1.0/24"] then 2 subnets will be created with cidr values 
#
# "10.247.0.0/24" and "10.247.1.0/24" respectively
#
# subnet_cidrs is a mandatory field
#
###############################################################################################################################
