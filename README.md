## Standard K8s cluster

See a similar [pulumi example](https://github.com/pulumi/examples/tree/master/gcp-ts-k8s-ruby-on-rails-postgresql)
Set the required configuration variables for this program after a `set +o history` to hide secrets.

Then, simply do the following:

```
npm install
pulumi up
```

## Alternative, simplified Cloud Run

[Gooogle Cloud Build]( https://cloud.google.com/cloud-build/) configured for this repository with CI/CD and published as Cloud Run [web app](https://flask-sqlserver-cloudrun-p63nwudoyq-uc.a.run.app/).


## Continuous Delivery

with `pulumi.sh` and `cloudbuild.yaml`, CD is fully automated.

Start with `pulumi stack init dev` and configure the secret passwords substitution in the build trigger, then enjoy the CI/CD full automation for a complete Kubernetes Cluster.
