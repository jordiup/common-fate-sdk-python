# common-fate-sdk-python

A python SDK for the common-fate API

# Tooling

We use https://github.com/OpenAPITools/openapi-generator to generate the python sdk

# Installation

To install, run brew install openapi-generator

Here is an example usage to generate a Ruby client:

openapi-generator generate -i https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml -g ruby -o /tmp/test/

To reinstall with the latest master, run brew uninstall openapi-generator && brew install --HEAD openapi-generator

To install OpenJDK (pre-requisites), please run

brew tap AdoptOpenJDK/openjdk
brew install --cask adoptopenjdk12
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-12.0.2.jdk/Contents/Home/

To install Maven, please run

brew install maven

# Generate

To generate the SDK
There was an error with the tooling but this fixed the issue https://github.com/OpenAPITools/openapi-generator/issues/11763#issuecomment-1098337960

locally, I have the common-fate repo in the same folder as this repo, so relative paths work for the openapi.yml file.

changes the `-i ../granted-approvals/openapi.yml` to point to your local copy of the common fate repo

```bash
_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -g python -i ../granted-approvals/openapi.yml -o ./output
```
