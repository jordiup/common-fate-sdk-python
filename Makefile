generate:
	_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -g python -i ../granted-approvals/openapi.yml