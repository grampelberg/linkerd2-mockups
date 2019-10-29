---
type: deployments
layout: single

name: emoji
golden:
- name: Inbound
  tooltip: All traffic received by this resource
  rows:
  - name: deploy/web
    success: 100
    rps: 1.97
    p50: 1 ms
    p95: 2 ms
    p99: 2 ms
  - name: deploy/linkerd-prometheus
    success: 99.23
    rps: 1.00
    p50: 10 ms
    p95: 15 ms
    p99: 1 s
  - name: statefulset/extremely-long-totally-reasonable-name
    success: 0
    rps: 19,284.01
    p50: 3 min
    p95: 1 hr
    p99: 203 hr
- name: Outbound
  tooltip: All traffic originating with this resource.
  rows:
  - name: deploy/web
    success: 100
    rps: 1.97
    p50: 1 ms
    p95: 2 ms
    p99: 2 ms
  - name: deploy/linkerd-prometheus
    success: 99.23
    rps: 1.00
    p50: 10 ms
    p95: 15 ms
    p99: 1 s
  - name: statefulset/extremely-long-totally-reasonable-name
    success: 0
    rps: 19,284.01
    p50: 3 min
    p95: 1 hr
    p99: 203 hr
- name: Pods
  tooltip: Golden metrics for each pod in this deployment.
  rows:
  - name: emoji-5d7c44b496-4j72b
    success: 100.00
    rps: 0.3
    p50: 1 ms
    p95: 4 ms
    p99: 10 ms
live:
- name: Inbound
  tooltip: Real time requests and responses sent to this resource.
  rows:
  - resources:
    - deploy/linkerd-prometheus
    - deploy/linkerd-web
    method: GET
    path: /metrics
    count: 16
    best: 3 ms
    worst: 6 ms
    last: 3 ms
    success: 100
  - resources:
    - 10.138.0.19
    - 10.138.0.20
    - job/ping-a-lot
    method: GET
    path: /ping
    count: 10
    best: 519 µs
    worst: 3 ms
    last: 519 µs
    success: 100
  - resources:
    - 10.138.0.19
    method: GET
    path: /ready
    count: 3
    best: 1 ms
    worst: 8 ms
    last: 2 ms
    success: 100
  - resources:
    - statefulset/extremely-long-totally-reasonable-name
    path: /foobar
    count: 1
    best: 30 s
    worst: 30 s
    last: 30 s
    success: 0
- name: Outbound
  tooltip: Real time requests and responses issued from this resource.
  rows:
  - resources:
    - deploy/linkerd-controller
    method: POST
    path: /api/v1/StatSummary
    count: 2,134
    best: 2 ms
    worst: 463 ms
    last: 230 ms
    success: 80
  - resources:
    - deploy/linkerd-controller
    method: POST
    path: /api/v1/ListPods
    count: 117
    best: 5 ms
    worst: 411 ms
    last: 67 ms
    success: 100
  - resources:
    - deploy/linkerd-controller
    method: POST
    path: /api/v1/Edges
    count: 52
    best: 39 ms
    worst: 395 ms
    last: 152 ms
    success: 99
  - resources:
    - deploy/prometheus
    method: HEAD
    path: /this/is/also/a/really/long/path/with/numbers/and/letters
    count: 1
    best: 10 ms
    worst: 10 ms
    last: 10 ms
    success: 100
---
