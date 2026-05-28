<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,50:1B3A5C,100:2E86AB&height=200&section=header&text=Rubén%20Alexis%20Liquenson&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=DevOps%20Engineer%20·%20Cloud%20·%20AWS%20·%20Kubernetes%20·%20GitOps&descAlignY=58&descSize=16&descColor=A8D8EA" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rubén_Liquenson-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ruben-alexis-liquenson-490961269)
[![GitHub](https://img.shields.io/badge/GitHub-Liquenson-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Liquenson)
[![Email](https://img.shields.io/badge/Email-liquenson.cloud@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:liquenson.cloud@gmail.com)
[![Location](https://img.shields.io/badge/Las_Palmas_de_Gran_Canaria-España-FF6B6B?style=for-the-badge&logo=googlemaps&logoColor=white)](#)

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&pause=1000&color=2E86AB&center=true&vCenter=true&width=600&lines=AWS+EKS+%7C+Terraform+%7C+Jenkins+CI%2FCD;Kubernetes+on-premise+con+kubeadm+%2B+Calico;Ansible+via+AWS+SSM+%7C+sin+SSH+%7C+sin+bastión;GitOps+%7C+IAM+como+código+%7C+roles+asumibles;4%2B+años+en+entornos+cloud+productivos" alt="Typing SVG" />

</div>

---

## `$ whoami`

DevOps Engineer con más de **4 años** diseñando y operando infraestructuras cloud en AWS de nivel productivo. Construyo pipelines GitOps completos — desde el commit hasta el despliegue en Kubernetes — con infraestructura como código, seguridad desde el diseño y observabilidad integrada.

Experiencia en entornos regulados (salud, finanzas). Actualmente en remoto para **Nibble Tech LLC** (New York). Abierto a posiciones **DevOps · Cloud Engineer · SRE**.

---

## `$ tech-stack --list`

<table>
<tr>
<td valign="top" width="33%">

**Cloud & IaC**
```
AWS EKS · ECR · IAM · VPC
KMS · CloudWatch · CloudTrail
Terraform 1.9  (módulos, S3 backend)
Linux  RHEL · Ubuntu · Amazon Linux 2023
```

</td>
<td valign="top" width="33%">

**Contenedores & Orquestación**
```
Docker 29.x
Kubernetes  EKS + kubeadm on-premise
Helm Charts  (values por entorno)
ArgoCD  (GitOps continuo)
Calico  (CNI)  containerd  (CRI)
```

</td>
<td valign="top" width="33%">

**CI/CD & Config Management**
```
Jenkins 2.555  (7-stage pipeline)
GitHub Actions
Ansible  via AWS SSM  (sin SSH)
SonarQube  (análisis estático)
```

</td>
</tr>
<tr>
<td valign="top">

**Observabilidad**
```
Prometheus + Grafana
CloudWatch Container Insights
CloudTrail  (auditoría completa)
```

</td>
<td valign="top">

**Seguridad & Accesos**
```
IAM roles asumibles  (sts:AssumeRole)
EKS Access Entries
Grupos + políticas como código
firewalld · SSH hardening
```

</td>
<td valign="top">

**Lenguajes**
```
Python 3.11  (Flask · pytest)
Bash  (scripting · automatización)
HCL  (Terraform)
YAML  (K8s · Ansible · GitHub Actions)
```

</td>
</tr>
</table>

---

## `$ ls -la projects/`

### [`gitops-stack`](https://github.com/Liquenson/gitops-stack) — Pipeline GitOps en AWS EKS

> Pipeline CI/CD de nivel productivo que automatiza el ciclo de vida completo del software en AWS EKS siguiendo el patrón GitOps. Git es la única fuente de verdad para código, infraestructura, configuración y accesos.

```
Developer → PR → merge main
                     │
              Jenkins Pipeline
              ├── 1. pytest          fail-fast — no builds si los tests fallan
              ├── 2. docker build    caché de capas · tag único por BUILD_NUMBER
              ├── 3. push ECR        registry privado · autenticación temporal
              ├── 4. terraform       plan → aprobación humana → apply (100 recursos)
              ├── 5. ansible SSM     hardening · firewalld · CloudWatch agent
              └── 6. kubectl         sts:AssumeRole → rolling update sin downtime
                                              │
                                     AWS EKS  gitops-stack-prod
                                     2 réplicas · self-healing · multi-AZ
```

<details>
<summary><b>Highlights técnicos</b></summary>
<br/>

| Área | Implementación |
|------|---------------|
| **Seguridad IAM** | `sts:AssumeRole` → `eks-admin-role` — cero credenciales estáticas. EKS Access Entry apunta al **rol**, nunca al usuario |
| **Infraestructura** | 100 recursos Terraform: VPC multi-AZ, EKS 1.35, KMS, CloudWatch, CloudTrail, backend S3 |
| **Identidades IAM** | 5 grupos + 22 usuarios gestionados como código en `users.tf` — PR obligatorio para cambios |
| **Config Management** | Ansible via AWS SSM sin SSH — nodos en subredes privadas sin IP pública |
| **Fix en producción** | `immediate: yes` en firewalld — mantiene sesión SSM activa durante hardening |
| **Auditoría** | CloudTrail registra cada `jenkins-deploy-{BUILD_NUMBER}` con timestamp y rol |
| **Branch Protection** | Push directo a `main` bloqueado — PR + status checks obligatorios |

</details>

![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform&logoColor=white)
![AWS EKS](https://img.shields.io/badge/AWS-EKS-FF9900?logo=amazonaws&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-SSM-EE0000?logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ECR-2496ED?logo=docker&logoColor=white)

---

### `kubernetes-onpremise` — Cluster real con kubeadm

> Cluster Kubernetes de 3 nodos montado desde cero sobre VMs Ubuntu 22.04 gestionadas con Vagrant. Sin servicios gestionados — cada componente instalado y configurado manualmente.

```
Vagrant (IaC local)
    ├── master-node   192.168.56.10   control plane
    │                                 etcd · api-server · scheduler · controller-manager
    ├── worker-node1  192.168.56.11   worker
    └── worker-node2  192.168.56.12   worker
                │
         kubeadm + Calico CNI
         containerd (SystemdCgroup=true)
         Kubernetes v1.31.14 · 3 nodos Ready ✅
```

<details>
<summary><b>Configuración de nodos</b></summary>
<br/>

```bash
# Requisitos previos en los 3 nodos
sudo swapoff -a                              # K8s no funciona con swap activo
echo "overlay\nbr_netfilter" | sudo tee /etc/modules-load.d/k8s.conf
sudo sysctl net.ipv4.ip_forward=1            # Routing entre pods

# containerd con SystemdCgroup=true
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# kubeadm init en el master
sudo kubeadm init \
  --apiserver-advertise-address=192.168.56.10 \
  --pod-network-cidr=192.168.0.0/16          # requerido por Calico

# Instalar CNI
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
```

</details>

**Roadmap:** aplicación multi-tier → Ingress NGINX + TLS → Persistent Volumes → RBAC → Prometheus + Grafana → HPA

![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.31-326CE5?logo=kubernetes&logoColor=white)
![VirtualBox](https://img.shields.io/badge/VirtualBox-7.2-183A61?logo=virtualbox&logoColor=white)
![Vagrant](https://img.shields.io/badge/Vagrant-2.4.9-1563FF?logo=vagrant&logoColor=white)
![Calico](https://img.shields.io/badge/Calico-CNI-FB8C00)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?logo=ubuntu&logoColor=white)

---

## `$ git log --stats`

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Liquenson&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true&bg_color=0D1B2A&title_color=2E86AB&icon_color=2E86AB&text_color=E8F4FD" height="160" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Liquenson&layout=compact&theme=github_dark&hide_border=true&bg_color=0D1B2A&title_color=2E86AB&text_color=E8F4FD" height="160" />

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2E86AB,50:1B3A5C,100:0D1B2A&height=100&section=footer" />

<img src="https://komarev.com/ghpvc/?username=Liquenson&color=2E86AB&style=flat-square&label=Profile+views" />

</div>
