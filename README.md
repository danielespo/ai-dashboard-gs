# GreatSky AI Dashboard - Weekend Prototype

A minimal monitoring dashboard prototype showcasing AI inference performance metrics, trading signals, and CNN-to-superconducting circuit mapping visualizations.

## Quick Start

```bash
# Clone and setup
git clone <your-repo>
cd greatsky-weekend

# Start monitoring stack
docker-compose up -d

# Access dashboards
open http://localhost:3001  # Grafana (admin/greatsky123)
open http://localhost:9090  # Prometheus
```

## What This Demonstrates

- **Low latency inference monitoring** (microsecond precision)
- **Real-time trading signal visualization** 
- **CNN weight-to-SSC mapping progress**
- **High-frequency trading performance metrics**

## Architecture

```
Prometheus → Grafana → Custom Dashboards
     ↑
Fake metrics generators (simulating ML inference)
```

## Dashboards

1. **Inference Performance** - Latency histograms, throughput gauges
2. **Trading Metrics** - Signal processing speed, PnL charts  
3. **Model Health** - Accuracy drift, memory usage
4. **Circuit Mapping** - Superconducting parameter translation

## Development

```bash
# Stop services
docker-compose down

# View logs
docker-compose logs -f grafana

# Rebuild
docker-compose up --build -d
```

## Tech Stack

- **Monitoring**: Prometheus + Grafana
- **Deployment**: Docker Compose
- **Focus**: Real-time performance visualization for HFT AI systems


Built for GreatSky, superconducting neural networks as a plug-and-play replacement of low latency FPGA DSP and algorithmic trading pipelines.