terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = "test-dev--mikeias-d-s-o"
    region = "us-central1"
}