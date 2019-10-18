# Linkerd2 Mockups

## Dashboard

Using a modern version of hugo extended, run:

```bash
hugo serve
```

Then go to [localhost:1313](http://localhost:1313).

Note: this is not meant to be a comprehensive, live mockup. Many of the existing features of the dashboard have not been mocked or thought about. Be prepared to ask questions.

## CLI

This is in progress. To run a current experiment:

```bash
./tools/cli.py edges/pod.yaml
```

Note: I'm not currently tracking the python dependencies required and have not put a docker image together to manage that. It'll happen eventually...

## Outstanding

### Smaller

- Text selector for namespace dropdown

### Sections

- Cron Jobs
- Replica Sets
- Ingress
- Service Accounts
- Service Profiles

### Design Refreshes

- Empty states
- Detail view
    - Show details for what options are being used (tracing, debug, ....)
- List view
- Control Plane
    - Show install config
    - Add something about trust roots.
    - Should check run here as well?
- Tap (add headers)

### Long Term

- Configuration of external services
- Tracing
- Edges (audit)
- Time slider for current data
