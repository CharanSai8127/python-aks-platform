# Azure AKS Progressive Delivery Platform

Production-grade Kubernetes platform built on Azure Kubernetes Service (AKS) implementing progressive delivery, automated deployment analysis, traffic-aware releases, and self-healing rollback mechanisms.

This project demonstrates how modern platform teams can reduce deployment risk by combining GitOps, Argo Rollouts, Gateway API, observability, and metrics-driven decision making into a closed-loop deployment system.

Instead of treating deployments as simple automation workflows, the platform continuously evaluates system health during releases and automatically determines whether a rollout should continue, pause, or rollback.

## Key Capabilities

* Progressive delivery using Argo Rollouts
* Canary deployment strategies
* Metrics-driven deployment validation
* Automated rollback on failure conditions
* GitOps-based deployment management using Argo CD
* Traffic-aware releases through Gateway API
* Observability with Prometheus, Grafana, and Alertmanager
* Deployment intelligence through automated analysis
* Horizontal Pod Autoscaler (HPA)
* Self-adaptive release management

## Technology Stack

Azure AKS • Kubernetes • Argo CD • Argo Rollouts • Gateway API • Prometheus • Grafana • Alertmanager • GitOps • Canary Deployments • Progressive Delivery • Platform Engineering
