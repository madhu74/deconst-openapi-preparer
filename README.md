# Deconst OPENAPI Preparer
OPENAPI (json) :point_right: :wrench: :point_right: .json

The *deconst OPENAPI preparer* builds [OPENAPI](https://github.com/OAI/OpenAPI-Specification) into custom JSON metadata envelopes. It's intended to be used within a CI system to present content to the rest of build pipeline.

This preparer is part of [deconst](https://github.com/deconst), an end-to-end documentation delivery system.

## Testing

Currently, the Docker image needs to be build manually as it is not yet up on quay.io or another Docker image library. Change into your clone of this repo and run the following command to build the image:

```bash
docker build . --no-cache --tag deconstopenapipreparer:latest
```

## Running locally

To run the OPENAPI preparer locally, you'll need to install:

*   [Docker](https://docs.docker.com/installation/#installation) for your platform.

Once you have Docker set up, export any desired configuration variables and run `deconst-preparer-sphinx.sh` with the absolute path to any openapi-based (json format) content repository.

```bash
./deconst-preparer-openapi.sh /absolute/path/to/content-repo
```

## Configuration

### Environment variables

The following values may be present in the environment:

*   `CONTENT_ROOT` is a path containing OPENAPI.json content to prepare. *Default: $(pwd)*
*   `ENVELOPE_DIR` is the destination directory for metadata envelopes. *Default: $(pwd)/_build/deconst-envelopes/*
*   `ASSET_DIR` is the destination directory for referenced assets. *Default: $(pwd)/_build/deconst-assets/*
*   `CONTENT_ID_BASE` is a prefix that's unique among the content repositories associated with the target deconst instance. Our convention is to use the base URL of the GitHub repository. *Default: Read from _deconst.json*

### Build system

By default, the preparer uses the [openapi-generator](https://github.com/OpenAPITools/openapi-generator) library to generate HTML from Openapi.json and then uses Python to translate those HTML files to JSON envelopes.