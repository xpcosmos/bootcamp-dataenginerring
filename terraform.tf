terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = "test-dev--mikeias-d-s-o"
  region  = "us-central1"
}
resource "google_storage_bucket" "dev-bucket" {
  name          = "test-dev--mikeiascamp--dev-bucket"
  location      = "US"
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