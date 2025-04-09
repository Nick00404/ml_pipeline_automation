provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "mlops_instance" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
  tags = {
    Name = "MLOpsInstance"
  }
}
