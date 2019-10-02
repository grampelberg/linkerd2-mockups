---
type: deployments
layout: single
breadcrumb:
- emoji

inbound:
- name: deploy/web
  success: 100.00%
  rps: 1.97
  p50: 1 ms
  p95: 2 ms
  p99: 2 ms
- name: deploy/linkerd-prometheus
  success: 100%
  rps: 1
  p50: 10 ms
  p95: 15 ms
  p99: 1 s
---
