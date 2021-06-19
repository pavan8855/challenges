terraform {
  required_version = ">= 0.12, < 0.15"
}

provider "aws" {
  region = var.region

  # Allow any 3.x version of the AWS provider
  version = var.version
}

module "vpc" {
  source = "./vpc" 
}

module "db" {
  source = "./db"
}

module "app" {
  source  = "./app"  
}