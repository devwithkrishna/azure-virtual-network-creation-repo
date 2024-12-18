module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-virtual-network-terraform-module"

  # variables passed to the module
  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "TRUE"
  location            = "centralindia"
  resource_group_name = "test-vnet-rg"
  vnet_name           = "test-vnet"
  subnet_cidrs        = ["10.219.40.0/25"]
  vnet_address_space  = ["10.219.40.0/25"]

}