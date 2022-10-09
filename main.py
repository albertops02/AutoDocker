import time
import docker
import infraestructura
import os
client = docker.from_env()
image = 'httpd'
binding = {80: 8080}

def runcontainerwithport(image, binding):
    container = client.containers.run(image, detach=True, ports=binding)
    print("Container started with ID: {}".format(container.id))

def pullimage(imagename):
    image = client.images.pull(imagename)
    print(image.id)    

print("Downloading Image...")
infraestructura.pullimage(image)
time.sleep(3)
print("Image downloaded")
print("Running container..")
infraestructura.runcontainerwithport(image, binding)
time.sleep(3)
print("Container running with the port binding " + str(binding))