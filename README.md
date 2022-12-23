# common-fate-sdk-python

A python SDK for the common-fate API

To generate the SDK
There was an error with the tooling but this fixed the issue https://github.com/OpenAPITools/openapi-generator/issues/11763#issuecomment-1098337960

locally, I have the common-fate repo in the same folder as this repo, so relative paths work for the openapi.yml file.

changes the `-i ../granted-approvals/openapi.yml` to point to your local copy of the common fate repo

```
_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -g python -i ../granted-approvals/openapi.yml -o ./output
```
