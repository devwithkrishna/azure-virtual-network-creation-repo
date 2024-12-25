module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-virtual-network-terraform-module"

  # variables passed to the module
  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "FALSE"
  location            = "centralindia"
  resource_group_name = "ARCHITECTS-CENTRAL-INDIA-AKS-VNET-RG"
  vnet_name           = "ARCHITECTS-CENTRAL-INDIA-AKS-VNET"
  subnet_cidrs = ["10.247.8.0/23"]
  vnet_address_space  = ["10.247.8.0/23"]

}