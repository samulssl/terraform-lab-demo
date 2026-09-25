output "pieza" {
  value = var.project_name
}

output "url" {
  value = "http://localhost:${var.host_port}/"
}

output "reversion" {
  value = "Restaurar la versión anterior de pieza/ y: terraform apply -auto-approve"
}
