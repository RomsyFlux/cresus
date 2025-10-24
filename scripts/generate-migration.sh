#!/bin/bash
# Generate database migration

if [ -z "$1" ]; then
    echo "Usage: ./scripts/generate-migration.sh <migration_message>"
    exit 1
fi

MESSAGE=$1

echo "📝 Generating migration: $MESSAGE"
alembic revision --autogenerate -m "$MESSAGE"

echo "✅ Migration generated"
echo ""
echo "Review the migration file in alembic/versions/"
echo "Then run 'make migrate' to apply it"
