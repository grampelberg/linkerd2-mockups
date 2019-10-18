---
type: deployments
layout: single

name: emoji
inbound:
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
---
