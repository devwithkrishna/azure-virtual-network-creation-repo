module "vnet" {
  source = "git::https://github.com/devwithkrishna/azure-virtual-network-terraform-module"

  # variables passed to the module
  application_name    = "devwithkrishna"
  environment         = "DEV"
  temporary           = "TRUE"
  location            = "centralindia"
  resource_group_name = "test-on-test"
  vnet_name           = "testontest"
  subnet_cidrs = ["10.250.0.0/25", "10.250.0.128/28"]
  vnet_address_space  = ["10.250.0.0/24"]

}