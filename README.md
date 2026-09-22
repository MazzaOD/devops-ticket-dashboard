# DevOps Command Centre

A modern DevOps dashboard built with FastAPI, designed to provide a centralized view of operational metrics, support activity, system health, and infrastructure insights.

![Python](https://img.shields.io/badge/Python-
![FastAPI](https://img.shields.io/badge/Fastramework-green
![Status](https://img.shields.io/badge/Status-Active-successOverview

The DevOps Command Centre was created to provide a single-pane-of-glass view of operational and support metrics.

The dashboard aggregates key information and presents it in a clean, modern interface, enabling teams to quickly identify issues, track trends, and monitor platform health.

This project was developed as a practical learning exercise to explore:

- DevOps principles
- Infrastructure monitoring
- Incident visibility
- Dashboard design
- API integration
- FastAPI development
- Data visualization

---

## Features

### Dashboard Metrics

- Open Support Tickets
- Closed Tickets
- Escalations
- Response Times
- System Health Indicators
- Operational KPIs

### Monitoring Features

- Real-time status updates
- Trend analysis
- Visual reporting
- Alert visibility
- Service overview panels

### Technical Features

- FastAPI backend
- Jinja2 templating
- Dynamic dashboard rendering
- REST API integration
- Responsive user interface
- Chart.js visualisations

---

## Technology Stack

### Backend

- FastAPI
- Python
- Jinja2 Templates
- Uvicorn

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### DevOps Concepts Demonstrated

- Monitoring & Observability
- Metrics Collection
- Dashboarding
- Service Status Monitoring
- Infrastructure Awareness
- Operational Reporting

---

## Project Structure

```text
devops-command-centre/
│
├── app.py
├── requirements.txt
├── templates/
│   └── dashboard.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── services/
├── api/
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/devops-command-centre.git

cd devops-command-centre
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn app:app --reload
```

Navigate to:

```text
http://127.0.0.1:8000
```

---

## Screenshots

Add screenshots here once available.

### Dashboard Overview

```text
docs/images/dashboard-overview.png
```

### Service Health View

```text
docs/images/service-health.png
```

---

## Future Improvements

Planned enhancements include:

- Docker containerisation
- Terraform infrastructure deployment
- Redis caching
- New Relic integration
- ClickHouse analytics
- Authentication and RBAC
- CI/CD pipelines
- Automated health checks
- Prometheus metrics
- Grafana integration

---

## Learning Objectives

This project was created to gain hands-on experience with technologies and concepts commonly found in DevOps and DevSecOps environments.

Key areas include:

- Infrastructure as Code concepts
- Monitoring and observability
- Deployment automation
- System administration
- API development
- Dashboard reporting
- Operational troubleshooting

---

## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## Author

**Mary O'Donnell**

Technical Support Technician with an interest in DevOps, DevSecOps, automation, infrastructure, monitoring, and platform engineering.

GitHub: https://github.com/yourusername

---

## License

This project is released under the MIT License.

