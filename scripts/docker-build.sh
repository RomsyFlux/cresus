#!/bin/bash
# Docker build script

set -e

VERSION=${1:-latest}
REGISTRY=${2:-cresus}

echo "🐳 Building Docker image..."
echo "Version: $VERSION"
echo "Registry: $REGISTRY"

# Build image
docker build \
  -t $REGISTRY/cresus:$VERSION \
  -t $REGISTRY/cresus:latest \
  -f docker/Dockerfile \
  .

echo "✅ Docker image built successfully"
echo ""
echo "To push to registry:"
echo "  docker push $REGISTRY/cresus:$VERSION"
echo "  docker push $REGISTRY/cresus:latest"
