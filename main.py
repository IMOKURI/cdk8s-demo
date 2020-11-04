#!/usr/bin/env python
from cdk8s import App, Chart
from constructs import Construct

from webservice import WebService


class MyChart(Chart):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here

        WebService(self, "hello", image="paulbouwer/hello-kubernetes:1.7", replicas=2)
        WebService(self, "ghost", image="ghost", container_port=2368)


app = App()
MyChart(app, "cdk8s-demo")

app.synth()
