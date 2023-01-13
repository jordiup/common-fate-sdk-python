generate:
	_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -g python -i ../granted-approvals/openapi.yml --package-name jhc_cf_sdk_test

generate-on-ci:
	_JAVA_OPTIONS="--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED" openapi-generator generate -g python -i ./ci-temp/openapi.yml --package-name jhc_cf_sdk_test