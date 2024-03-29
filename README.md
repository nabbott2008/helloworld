# Hello World Helm Chart

This is a basic demonstration Helm chart but can double up as a chart to server basic web pages from any docker container.

## Pre Requisites:

* Kubernetes 1.16 with nginx ingress enabled:

* https://kubernetes.github.io/ingress-nginx/deploy/

* Helm 2.15.1

### Installing the Chart

To install the chart with the release name `helloworld` in the default
namespace:

```
$ git clone https://github.com/nabbott2008/helloworld.git
$ helm install --name helloworld helloworld
```


| Parameter                                      | Description                                                                                                                                                              | Default                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `image.repository`                                       | Image repository                                                                                                                                               | `never152/helloworld`                                            
|`image.tag`| Image tag                                    |         `develop`                                                                                                         |
| `image.pullPolicy`                              | Image pull policy                                                                                                                                              | `IfNotPresent`                                                     |
| `replicaCount`                                     | Number of replicas to run                                                                                                                                                           | `3`                                                                |
| `ingress.host`                                     | Ingress host header                                                                                                                                                           | `test.com`   
| `service.port`                                     | Port service is listening on                                                                                                                                                         | `80` 
| `target.port`                                     | Port container is listening on                                                                                                                                                          |`5000` |

### Testing on Minikube

If you have installed the chart in Minikube, and used default values, you can test with this curl from the host machine:

```
$ curl -H "Host: test.com" $(minikube ip)
```

### Using as template web service chart

The values above allow you to use this Helm chart as a basic web service chart.

You can use any docker image you require as long as it's serving HTTP requests.

Ensure you change the port ports appropriately depending on what port your docker container listens on.
