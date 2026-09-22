from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psutil

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    data = {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "open_tickets": 17,
        "critical_tickets": 3,
        "resolved_tickets": 42,
        "events": [
            "Ticket #231 Created",
            "Deployment Successful",
            "Container Restarted",
            "Health Check Passed",
            "Grafana Dashboard Updated"
        ]
    }

    print("data type:", type(data))
    print("data:", data)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            **data
        }
    )




@app.get("/health")
def health():
    return {
        "status": "healthy"
    }