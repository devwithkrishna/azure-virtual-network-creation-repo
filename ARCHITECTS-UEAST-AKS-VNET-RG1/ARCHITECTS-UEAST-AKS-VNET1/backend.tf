terraform {
  backend "azurerm" {
    resource_group_name  = "ARCHITECTS-STORAGE-RG"
    storage_account_name = "techarchitectssa"
    container_name       = "tfstatefiles"
    key                  = "ARCHITECTS-UEAST-AKS-VNET-RG1-ARCHITECTS-UEAST-AKS-VNET1.tfstate"
  }
}