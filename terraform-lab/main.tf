terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

resource "random_pet" "api_server" {
  length    = 2
  separator = "-"
}

output "api_server_name" {
  value       = "api-orders-${random_pet.api_server.id}"
  description = "Nombre unico asignado al contenedor de la API"
}
