# Rubén Alexis Liquenson — DevOps Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/ruben-alexis-liquenson-490961269)
[![Website](https://img.shields.io/badge/lracloudops.com-CC0000?logo=googlechrome&logoColor=white)](https://www.lracloudops.com/)
[![Instagram](https://img.shields.io/badge/@lracloudops-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/lracloudops/)
[![Email](https://img.shields.io/badge/liquenson.cloud@gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:liquenson.cloud@gmail.com)

DevOps Engineer con 4+ años diseñando y operando infraestructuras cloud en AWS de nivel productivo. Fundador de [LRA Cloud Operations](https://www.lracloudops.com/) — consultoría DevOps & Cloud con sede en Las Palmas de Gran Canaria, España.

Construyo pipelines GitOps completos con infraestructura como código, seguridad desde el diseño y observabilidad integrada. Experiencia en entornos regulados (salud, finanzas). Abierto a posiciones **DevOps · Cloud Engineer · SRE**.

---

## Stack

| Área | Tecnologías |
|---|---|
| **Cloud** | AWS — EKS · ECR · IAM · VPC · KMS · CloudWatch · CloudTrail |
| **IaC** | Terraform 1.9 (módulos, S3 backend) · Vagrant |
| **Contenedores** | Docker · Kubernetes (EKS + kubeadm on-premise) · Helm · containerd |
| **Networking** | Calico CNI · NGINX Ingress · cert-manager |
| **CI/CD** | Jenkins · GitHub Actions · ArgoCD (GitOps) |
| **Config Management** | Ansible via AWS SSM (sin SSH, sin bastión) |
| **Observabilidad** | Prometheus · Grafana · Metrics Server · CloudWatch Container Insights |
| **Seguridad** | IAM roles asumibles (sts:AssumeRole) · EKS Access Entries · SonarQube · Trivy |
| **Lenguajes** | Python 3.11 · Bash · HCL · YAML |
| **OS** | RHEL · Ubuntu · Amazon Linux 2023 |

---

## Proyectos

### [gitops-stack](https://github.com/Liquenson/gitops-stack)

Pipeline CI/CD de nivel productivo sobre AWS EKS. Git como única fuente de verdad para código, infraestructura, configuración y accesos.

```
Developer → PR → merge main
                     │
              Jenkins (7 stages)
              ├── pytest              tests unitarios — fail-fast
              ├── docker build        imagen con tag BUILD_NUMBER
              ├── push ECR            autenticación temporal AWS
              ├── terraform plan/apply 100 recursos — VPC · EKS · KMS · IAM
              ├── ansible SSM         hardening · firewalld · CloudWatch agent
              └── kubectl apply       sts:AssumeRole → rolling update sin downtime
                                                │
                                       AWS EKS  gitops-stack-prod
                                       2 réplicas · self-healing · multi-AZ
```

Aspectos destacados: cero credenciales estáticas, identidades IAM como código en `users.tf`, branch protection con PR obligatorio, auditoría completa con CloudTrail por `jenkins-deploy-{BUILD_NUMBER}`.

---

### [k8s-on-premise](https://github.com/lra-cloud-ops/k8s-on-premise)

Clúster Kubernetes de 3 nodos desplegado desde cero sobre Ubuntu 22.04 con Vagrant y kubeadm. Sin servicios gestionados — cada componente instalado y configurado manualmente. Proyecto en progreso con roadmap de 18 fases.

```
Vagrant (IaC)
├── master-node   192.168.56.10   Control Plane — apiserver · etcd · scheduler · controller
├── worker-node1  192.168.56.11   Worker
└── worker-node2  192.168.56.12   Worker

Stack actual: kubeadm · Calico CNI · containerd · Helm · Metrics Server
Versión: Kubernetes v1.31.14 · 3 nodos Ready
```

Roadmap: `Longhorn` → `NGINX Ingress` → `cert-manager` → `PostgreSQL` → `Prometheus` → `Grafana` → `Loki` → `Alertmanager` → `Harbor` → `Jenkins` → `SonarQube` → `ArgoCD` → `Vault` → `Trivy` → `Velero` → `App real (React + FastAPI)` → `OpenTelemetry + Jaeger`

---

## Contacto

- **Web:** [lracloudops.com](https://www.lracloudops.com/)
- **LinkedIn:** [ruben-alexis-liquenson](https://linkedin.com/in/ruben-alexis-liquenson-490961269)
- **Instagram:** [@lracloudops](https://www.instagram.com/lracloudops/)
- **Email:** liquenson.cloud@gmail.com
- **Ubicación:** Las Palmas de Gran Canaria, España
