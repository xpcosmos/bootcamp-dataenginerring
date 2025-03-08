variable "bucket_dev_name" {
  description = "Bucket para testes e desenvolvimentos"
  default = "test-dev--mikeiascamp--dev-bucket"
}

variable "bucket_dev_storage_class" {
  description = "Class de armazenamento para bucket de desenvolvimento"
  default = "STANDARD"
}

variable "bucket_dev_location" {
  description = "Localização para bucket de desenvolvimento"
  default = "US"
}

variable "project_dev_name" {
  description = "Nome do projeto"
  default = "test-dev--mikeias-d-s-o"
}

variable "project_dev_region" {
  description = "Região do projeto"
  default = "us-central1"
}