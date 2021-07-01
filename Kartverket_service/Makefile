download-dependencies:
	wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/swagger-codegen-cli-3.0.25.jar -O swagger-codegen-cli.jar

generate: download-dependencies
	java -jar swagger-codegen-cli.jar generate -i https://ws.geonorge.no/adresser/v1/openapi.json -l python -o codegen