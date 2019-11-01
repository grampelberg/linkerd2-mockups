---
type: deployments
layout: single

name: quiet

state:
- name: Desired
  value: 1
  tooltip: FIXME
- name: Current
  value: 1
  tooltip: FIXME
- name: Up-to-date
  value: 1
  tooltip: FIXME
- name: Available
  value: 1
  tooltip: FIXME
services:
- quiet
- quiet-canary
- quiet-primary

golden:
- name: Inbound
- name: Outbound
  rows:
  - name: linkerd-controller
    type: deploy
    success: 100
    rps: 1.97
    p50: 1 ms
    p95: 2 ms
    p99: 2 ms
edges:
- name: Inbound
  rows:
  - name: 10.1.3.2
    type: ip
    protocol: TCP
    connections: 3
    read: 0 B/s
    write: 300 B/s
    secured: false
- name: Outbound
live:
- name: Inbound
- name: Outbound
  rows:
  - resources:
    - name: linkerd-controller
      type: deploy
    method: POST
    path: /api/v1/StatSummary
    count: 2,134
    best: 2 ms
    worst: 463 ms
    last: 230 ms
    success: 80
    service: linkerd-controller
---
