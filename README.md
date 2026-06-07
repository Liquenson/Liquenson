<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,50:1B3A5C,100:2E86AB&height=180&section=header&text=Rubén%20Alexis%20Liquenson&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=DevOps%20Engineer%20·%20Cloud%20·%20Kubernetes%20·%20GitOps&descAlignY=58&descSize=15&descColor=A8D8EA" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rubén_Liquenson-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ruben-alexis-liquenson-490961269)
[![Website](https://img.shields.io/badge/Website-lracloudops.com-CC0000?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.lracloudops.com/)
[![Instagram](https://img.shields.io/badge/Instagram-@lracloudops-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/lracloudops/)
[![Email](https://img.shields.io/badge/Email-liquenson.cloud@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:liquenson.cloud@gmail.com)
[![Location](https://img.shields.io/badge/Las_Palmas_de_Gran_Canaria-España-FF6B6B?style=for-the-badge&logo=googlemaps&logoColor=white)](#)

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=14&pause=1000&color=2E86AB&center=true&vCenter=true&width=620&lines=AWS+EKS+%7C+Terraform+%7C+Jenkins+CI%2FCD;Kubernetes+on-premise+con+kubeadm+%2B+Calico;Ansible+via+AWS+SSM+%7C+sin+SSH+%7C+sin+bastión;GitOps+%7C+IAM+como+código+%7C+roles+asumibles" />

</div>

---

## $ whoami

DevOps Engineer con **4+ años** diseñando y operando infraestructuras cloud en AWS de nivel productivo. Construyo pipelines GitOps completos — desde el commit hasta el despliegue en Kubernetes — con infraestructura como código, seguridad desde el diseño y observabilidad integrada.

Experiencia en entornos regulados (salud, finanzas). Fundador de **[LRA Cloud Operations](https://www.lracloudops.com/)** — consultoría DevOps & Cloud. Abierto a posiciones **DevOps · Cloud Engineer · SRE**.

---

## $ tech-stack --list

<table>
<tr>
<td valign="top" width="33%">

**Cloud & IaC**
```
AWS  EKS · ECR · IAM · VPC
     KMS · CloudWatch · CloudTrail
Terraform 1.9  (módulos · S3 backend)
Linux  RHEL · Ubuntu · Amazon Linux
```

</td>
<td valign="top" width="33%">

**Contenedores & Orquestación**
```
Docker 29.x
Kubernetes  EKS + kubeadm on-premise
Helm Charts  (values por entorno)
ArgoCD  (GitOps)
Calico CNI · containerd CRI
```

</td>
<td valign="top" width="33%">

**CI/CD & Automatización**
```
Jenkins 2.x  (pipelines multi-stage)
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
Metrics Server  (kubectl top)
CloudWatch Container Insights
```

</td>
<td valign="top">

**Seguridad**
```
IAM roles asumibles  (sts:AssumeRole)
EKS Access Entries
Identidades como código
firewalld · SSH hardening
```

</td>
<td valign="top">

**Lenguajes**
```
Python 3.11  (Flask · pytest)
Bash  (scripting · automatización)
HCL  (Terraform)
YAML  (K8s · Ansible · CI/CD)
```

</td>
</tr>
</table>

---

## $ ls -la projects/

### [gitops-stack](https://github.com/Liquenson/gitops-stack) — Pipeline GitOps en AWS EKS

Pipeline CI/CD de nivel productivo sobre AWS EKS. Git como única fuente de verdad para código, infraestructura, configuración y accesos.

```
Developer → PR → merge main
                     │
              Jenkins Pipeline
              ├── pytest          fail-fast
              ├── docker build    tag por BUILD_NUMBER
              ├── push ECR        autenticación temporal
              ├── terraform       plan → aprobación → apply (100 recursos)
              ├── ansible SSM     hardening · firewalld · CloudWatch agent
              └── kubectl         sts:AssumeRole → rolling update sin downtime
                                              │
                                     AWS EKS  gitops-stack-prod
```

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![AWS EKS](https://img.shields.io/badge/AWS_EKS-FF9900?logo=amazonaws&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

---

### [k8s-on-premise](https://github.com/lra-cloud-ops/k8s-on-premise) — Clúster Kubernetes from scratch

Clúster de 3 nodos montado desde cero sobre Ubuntu 22.04 con Vagrant. Sin servicios gestionados — cada componente instalado y configurado manualmente. Roadmap de 18 fases en progreso.

```
Vagrant (IaC)
├── master-node   192.168.56.10   Control Plane
├── worker-node1  192.168.56.11   Worker
└── worker-node2  192.168.56.12   Worker
       │
  kubeadm · Calico CNI · containerd · Helm · Metrics Server
  Kubernetes v1.31.14 · 3 nodos Ready ✅
```

**Roadmap:** `Longhorn` → `NGINX Ingress` → `cert-manager` → `PostgreSQL` → `Prometheus` → `Grafana` → `Loki` → `Jenkins` → `ArgoCD` → `Vault` → `Trivy` → `App real`

![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.31-326CE5?logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-v3.21-0F1689?logo=helm&logoColor=white)
![Calico](https://img.shields.io/badge/Calico-CNI-FB8C00)
![Vagrant](https://img.shields.io/badge/Vagrant-1563FF?logo=vagrant&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_22.04-E95420?logo=ubuntu&logoColor=white)

---

## $ git log --stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Liquenson&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true&bg_color=0D1B2A&title_color=2E86AB&icon_color=2E86AB&text_color=E8F4FD" height="155" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Liquenson&layout=compact&theme=github_dark&hide_border=true&bg_color=0D1B2A&title_color=2E86AB&text_color=E8F4FD" height="155" />

</div>

---

<div align="center">

**[lracloudops.com](https://www.lracloudops.com/)** · DevOps & Cloud Consulting · Las Palmas de Gran Canaria, España

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2E86AB,50:1B3A5C,100:0D1B2A&height=80&section=footer" />

<img src="https://komarev.com/ghpvc/?username=Liquenson&color=2E86AB&style=flat-square&label=Profile+views" />

</div>
