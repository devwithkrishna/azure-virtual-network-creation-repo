module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-virtual-network-terraform-module"

  # variables passed to the module
  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "TRUE"
  location            = "centralindia"
  resource_group_name = "ARCHITECTS-CENTRAL-INDIA-AKS-VNET-RG"
  vnet_name           = "ARCHITECTS-CENTRAL-INDIA-AKS-VNET"
  subnet_cidrs = ["10.247.8.0/24", "10.247.9.192/26"]
  vnet_address_space  = ["10.247.8.0/23"]

}