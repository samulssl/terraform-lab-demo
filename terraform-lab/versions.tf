terraform {
  required_version = ">= 1.9.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.9"
    }
  }
}

provider "docker" {
  host = var.docker_host
}
