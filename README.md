# Secure-Redundancy-IaC

## Project Overview
This project demonstrates an automated **DevSecOps pipeline** for securing Infrastructure as Code (IaC). 

## Key Features
* **Automated Security Gates:** Uses GitHub Actions to scan Python-based network blueprints for vulnerabilities.
* **Vulnerability Detection:** Successfully identified and blocked insecure code (e.g., dangerous `eval()` functions).
* **Compliance-as-Code:** Ensuring all network configurations meet security standards before deployment.

## Tools Used
* **GitHub Actions:** CI/CD Automation
* **Bandit:** Static Analysis Security Testing (SAST)
* **Python:** Network Infrastructure Scripting
