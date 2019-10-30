---
type: deployments
layout: single

name: emoji
golden:
- name: Inbound
  tooltip: All traffic received by this resource
  rows:
  - name: web
    type: deploy
    success: 100
    rps: 1.97
    p50: 1 ms
    p95: 2 ms
    p99: 2 ms
  - name: linkerd-prometheus
    type: deploy
    success: 99.23
    rps: 1.00
    p50: 10 ms
    p95: 15 ms
    p99: 1 s
  - name: extremely-long-totally-reasonable-name
    type: sts
    success: 0
    rps: 19,284.01
    p50: 3 min
    p95: 1 hr
    p99: 203 hr
- name: Outbound
  tooltip: All traffic originating with this resource.
  rows:
  - name: web
    type: deploy
    success: 100
    rps: 1.97
    p50: 1 ms
    p95: 2 ms
    p99: 2 ms
  - name: linkerd-prometheus
    type: deploy
    success: 99.23
    rps: 1.00
    p50: 10 ms
    p95: 15 ms
    p99: 1 s
  - name: extremely-long-totally-reasonable-name
    type: sts
    success: 0
    rps: 19,284.01
    p50: 3 min
    p95: 1 hr
    p99: 203 hr
live:
- name: Inbound
  tooltip: Real time requests and responses sent to this resource.
  rows:
  - resources:
    - name: linkerd-prometheus
      type: deploy
    - name: linkerd-web
      type: deploy
    method: GET
    path: /metrics
    count: 16
    best: 3 ms
    worst: 6 ms
    last: 3 ms
    success: 100
    service: emoji-svc
  - resources:
    - name: 10.138.0.19
      type: ip
    - name: 10.138.0.20
      type: ip
    - name: ping-a-lot
      type: job
    method: GET
    path: /ping
    count: 10
    best: 519 µs
    worst: 3 ms
    last: 519 µs
    success: 100
    service: emoji-svc
  - resources:
    - name: 10.138.0.19
      type: ip
    method: GET
    path: /ready
    count: 3
    best: 1 ms
    worst: 8 ms
    last: 2 ms
    success: 100
    service: emoji-svc
  - resources:
    - name: extremely-long-totally-reasonable-name
      type: sts
    path: /foobar
    method: POST
    count: 1
    best: 30 s
    worst: 30 s
    last: 30 s
    success: 0
    service: emoji-svc
- name: Outbound
  tooltip: Real time requests and responses issued from this resource.
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
  - resources:
    - name: linkerd-controller
      type: deploy
    method: POST
    path: /api/v1/ListPods
    count: 117
    best: 5 ms
    worst: 411 ms
    last: 67 ms
    success: 100
    service: linkerd-controller
  - resources:
    - name: linkerd-controller
      type: deploy
    method: POST
    path: /api/v1/Edges
    count: 52
    best: 39 ms
    worst: 395 ms
    last: 152 ms
    success: 99
    service: linkerd-controller
  - resources:
    - name: linkerd-prometheus
      type: deploy
    method: HEAD
    path: /this/is/also/a/really/long/path/with/numbers/and/letters/and/other/things/too
    count: 1
    best: 10 ms
    worst: 10 ms
    last: 10 ms
    success: 100
    service: linkerd-controller
routes:
- name: GET /api/v1/query
  service: linkerd-prometheus
  success: 100
  rps: 42.5
  p50: 87 ms
  p95: 188 ms
  p99: 199 ms
- name: GET /api/v1/query_range
  service: linkerd-prometheus
- name: GET /api/v1/series
  service: linkerd-prometheus
- name: [DEFAULT]
  service: linkerd-prometheus
---
