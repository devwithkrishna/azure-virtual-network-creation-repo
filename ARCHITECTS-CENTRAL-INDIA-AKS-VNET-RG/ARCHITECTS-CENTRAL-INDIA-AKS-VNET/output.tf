output "vnet_resource_group_name" {
  description = "Azure resource group name"
  value = module.vnet.vnet_resource_group_name
}

output "vnet_location" {
  description = "Azure virtual network location"
  value = module.vnet.vnet_location
}

output "vnet_environment" {
  description = "Azure virtual network environment"
  value = module.vnet.vnet_environment
}

output "vnet_name" {
  description = "Azure virtual network name"
  value = module.vnet.vnet_name
}

output "vnet_address_range" {
  description = "Azure virtual network address range"
  value = module.vnet.vnet_address_range
}

output "current_subscription_display_name" {
  description = "Azure subscription name"
  value = module.vnet.current_subscription_display_name
}

