terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = var.project_dev_name
  region  = var.project_dev_region
}
resource "google_storage_bucket" "dev-bucket" {
  name          = var.bucket_dev_name
  location      = var.bucket_dev_location
  storage_class = var.bucket_dev_storage_class
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }
}