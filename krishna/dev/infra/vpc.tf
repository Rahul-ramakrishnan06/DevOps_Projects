module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "6.0.1"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]

  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform = "true"
    Environment = "dev"
  }
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "imported-vpc"
  cidr = data.aws_vpc.existing.cidr_block

  azs             = slice(data.aws_availability_zones.available.names, 0, length(data.aws_subnets.public.ids))
  public_subnets  = data.aws_subnets.public.ids
  private_subnets = data.aws_subnets.private.ids

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Owner       = "Rahul"
    Environment = "prod"
  }
}
