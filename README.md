## Standard K8s cluster

See a similar [pulumi example](https://github.com/pulumi/examples/tree/master/gcp-ts-k8s-ruby-on-rails-postgresql)
Set the required configuration variables for this program after a `set +o history` to hide secrets.

Then, simply do the following:

```
npm install
pulumi up
```

## Alternative, simplified Cloud Run

[Gooogle Cloud Build]( https://cloud.google.com/cloud-build/) configured for this repository with CI/CD and published as Cloud Run web app.


## Continuous Delivery

with `pulumi.sh` and `cloudbuild.yaml`, CD is fully automated.

Start with `pulumi stack init dev` and configure the secret passwords substitution in the build trigger, then enjoy the CI/CD full automation for a complete Kubernetes Cluster.

## Cloud Build

### Substitution variables

![Secrets](https://user-images.githubusercontent.com/3272563/154686677-5a1ccff5-a6cc-4acb-9fc4-8de8fca31a72.jpg)

### Build log details

![CloudBuild](https://user-images.githubusercontent.com/3272563/154686450-5f962ba1-bf22-4cb8-9148-f4093e4b3bdb.jpg)
