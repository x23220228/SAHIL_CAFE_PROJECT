#!/bin/bash

# Run SonarScanner
$CODEBUILD_SRC_DIR/opt/sonar-scanner/bin/sonar-scanner \
  -Dsonar.projectKey=x23220228_SAHIL_CAFE_PROJECT \
  -Dsonar.organization=x23220228-sahil-shaikh \
  -Dsonar.projectName=SAHIL_CAFE_PROJECT \
  -Dsonar.projectVersion=1.0 \
  -Dsonar.python.version=3.8 \
  -Dsonar.sources=$CODEBUILD_SRC_DIR \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=dfaae103df5165b706b772497bac9ada0e655410
