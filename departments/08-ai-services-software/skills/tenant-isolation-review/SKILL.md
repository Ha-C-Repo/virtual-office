---
name: tenant-isolation-review
description: Review code and schema for tenant (organization) isolation, object-level authorization and logging hygiene.
---
# Tenant Isolation Review

## When to use
Any new endpoint, query, background job, report or AI feature that reads customer data.

## Checklist
1. Every table has an organization/tenant column; every query filters on it.
2. Object access by id also checks that the object belongs to the caller's tenant (guard against insecure direct object references).
3. Background jobs and AI calls carry the tenant id and cannot read other tenants' data.
4. Caches, search indexes and file storage paths include the tenant.
5. Role-based access checked server-side, not only in the UI.
6. Subscription-tier gating enforced server-side.
7. Log lines include tenant id and never include personal data or secrets.
8. Customer-portal auth is separate from staff auth.

## Outputs
Findings list with route/file, issue, severity, fix. Zero tolerance: any cross-tenant read blocks release.
