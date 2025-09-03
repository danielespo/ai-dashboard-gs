# Weekend dashboard

A minimal monitoring dashboard prototype with inference performance metrics, trading signals, and a CNN-to-superconducting circuit mapping mockup.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/danielespo/ai-dashboard-gs
cd greatsky-weekend

# Start monitoring stack
docker-compose up -d

# Access dashboards
open http://localhost:3001  # Grafana (admin/GS123)
open http://localhost:9090  # Prometheus
```

## What this shows

- **Monitor low latency inference**
- **Real-time trading signal visualization** 
- **CNN weight-to-SSC mapping mockup**

## Architecture

```
Prometheus → Grafana → Dashboards
     ↑
Fake metrics generators (simulating ML inference)
```

## Dashboards

1. **Inference lerformance** - Latency, throughput
2. **Trading mockup** - Signal processing speed, PnL charts 
3. **Model health** - Accuracy drift, memory usage

## Development

```bash
# Stop
docker-compose down

# View logs
docker-compose logs -f grafana

# Rebuild
docker-compose up --build -d
```

## Tech Stack

- **Monitoring**: Prometheus + Grafana
- **Deployment**: Docker
- **Focus**: Real-time performance visualization for HFT AI systems
