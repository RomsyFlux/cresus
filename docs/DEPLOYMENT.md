# Deployment Guide

## Prerequisites

- Docker and Docker Compose
- PostgreSQL 15+
- Redis 7+
- API Keys (Notion, Google Sheets, OpenAI/Anthropic)

## Local Development

### 1. Clone Repository

```bash
git clone https://github.com/RomsyFlux/cresus.git
cd cresus
```

### 2. Environment Configuration

```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
- `DATABASE_URL`
- `REDIS_URL`
- `SECRET_KEY`
- `NOTION_API_KEY`
- `GOOGLE_SHEETS_CREDENTIALS_PATH`
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`

### 3. Start Services

```bash
# Using Docker Compose
docker-compose up -d

# Or locally
make install
make migrate
make run-dev
```

### 4. Access Application

- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## Production Deployment

### AWS Deployment

#### 1. Infrastructure Setup

```bash
# Using Terraform or Pulumi
cd infrastructure/
pulumi up
```

This creates:
- VPC with public and private subnets
- RDS PostgreSQL instance
- ElastiCache Redis cluster
- ECS cluster with Fargate
- Application Load Balancer
- S3 bucket for data storage

#### 2. Database Migration

```bash
# Run migrations
docker run -e DATABASE_URL=$PROD_DB_URL cresus:latest alembic upgrade head
```

#### 3. Deploy Application

```bash
# Build and push Docker image
docker build -t cresus:latest -f docker/Dockerfile .
docker tag cresus:latest $REGISTRY/cresus:latest
docker push $REGISTRY/cresus:latest

# Update ECS service
aws ecs update-service --cluster cresus-cluster --service cresus-api --force-new-deployment
```

### Environment Variables for Production

```bash
ENVIRONMENT=production
DEBUG=false
DATABASE_URL=postgresql://user:pass@rds-endpoint:5432/cresus
REDIS_URL=redis://elasticache-endpoint:6379
SECRET_KEY=<strong-random-key>
ALLOWED_HOSTS=api.cresus.ai
CORS_ORIGINS=https://cresus.ai
```

## Monitoring

### Health Checks

```bash
curl http://localhost:8000/health
```

### Logs

```bash
# Docker logs
docker-compose logs -f app

# AWS CloudWatch
aws logs tail /ecs/cresus-api --follow
```

### Metrics

- Application metrics: New Relic
- Error tracking: Sentry
- Uptime monitoring: UptimeRobot

## Backup and Recovery

### Database Backup

```bash
# Manual backup
pg_dump -h localhost -U postgres cresus > backup.sql

# Automated backups (AWS RDS)
aws rds create-db-snapshot --db-instance-identifier cresus-db --db-snapshot-identifier cresus-backup-$(date +%Y%m%d)
```

### Restore

```bash
psql -h localhost -U postgres cresus < backup.sql
```

## Scaling

### Horizontal Scaling

```bash
# Scale ECS service
aws ecs update-service --cluster cresus-cluster --service cresus-api --desired-count 5

# Auto-scaling configuration
aws application-autoscaling register-scalable-target \
  --service-namespace ecs \
  --scalable-dimension ecs:service:DesiredCount \
  --resource-id service/cresus-cluster/cresus-api \
  --min-capacity 2 \
  --max-capacity 10
```

### Database Scaling

```bash
# Upgrade instance class
aws rds modify-db-instance --db-instance-identifier cresus-db --db-instance-class db.t3.large --apply-immediately
```

## Security

### SSL/TLS

- Use AWS Certificate Manager for SSL certificates
- Configure HTTPS on Application Load Balancer
- Force HTTPS redirects

### Secrets Management

```bash
# Store secrets in AWS Secrets Manager
aws secretsmanager create-secret --name cresus/api-keys --secret-string file://secrets.json
```

### Network Security

- VPC with private subnets for database and Redis
- Security groups with minimal access
- WAF rules for API protection

## Troubleshooting

### Application won't start

1. Check environment variables
2. Verify database connectivity
3. Check logs for errors

### Slow API responses

1. Check database query performance
2. Monitor Redis cache hit rate
3. Review API rate limiting settings

### Database connection errors

1. Verify connection string
2. Check security group rules
3. Confirm database is running

## Rollback

```bash
# Rollback to previous version
aws ecs update-service --cluster cresus-cluster --service cresus-api --task-definition cresus-api:PREVIOUS_VERSION

# Rollback database migration
alembic downgrade -1
```
