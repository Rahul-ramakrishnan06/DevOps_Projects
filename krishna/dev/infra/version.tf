terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "my-terraform-state-bucket"  # Replace with your S3 bucket name
    key            = "dev/terraform.tfstate"      # Path inside the bucket for this module
    region         = "ap-south-1"                 # AWS region where the bucket is created                        
  }
}
