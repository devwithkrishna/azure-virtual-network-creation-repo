module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-virtual-network-terraform-module"

  # variables passed to the module
  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "TRUE"
  location            = "centralindia"
  resource_group_name = "ARCHITECTS-UEAST-AKS-VNET-RG1"
  vnet_name           = "ARCHITECTS-UEAST-AKS-VNET1"
  subnet_cidrs = ["10.210.1.0/24"]
  vnet_address_space  = ["10.210.0.0/23"]

}