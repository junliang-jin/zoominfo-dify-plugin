## Privacy

**Last Updated:** June 19, 2025
**Version:** 0.0.1

## Overview

This privacy policy describes how the ZoomInfo Dify Plugin ("the Plugin") collects, uses, stores, and protects your
information when you use it to connect to and query ZoomInfo data through the Dify platform.

## Information We Collect

### 1. Authentication Credentials

The Plugin collects and processes the following authentication information:

- **ZoomInfo Username**: Your ZoomInfo account username/email
- **ZoomInfo Password**: Your ZoomInfo account password

### 2. Session Data

During operation, the Plugin temporarily stores:

- **JWT Tokens**: Authentication tokens obtained from ZoomInfo for API access
- **Token Expiry Information**: Timestamps for session management and automatic refresh

### 3. Query Data

The Plugin processes:

- **Company Names**: Company names you search for in enrichment requests
- **Contact Information**: Names and company details for contact searches
- **Company IDs**: ZoomInfo company identifiers for news searches
- **Query Results**: Data returned from ZoomInfo based on your requests

### 4. Request Parameters

The Plugin handles:

- **Output Fields**: Specific data fields you request from ZoomInfo
- **Date Ranges**: Date filters for news searches
- **Pagination Parameters**: Page numbers and limits for result sets

## How We Use Your Information

### Authentication and Access

- Credentials are used exclusively to authenticate with ZoomInfo's API via JWT token exchange
- JWT tokens are used to make authorized API calls to retrieve data you request
- No credentials are transmitted to any third parties other than ZoomInfo's official API endpoints

### Data Retrieval

- Company, contact, and news queries are executed against ZoomInfo's API to retrieve the specific data you request
- Query results are returned to you through the Dify platform interface
- The Plugin only accesses data that your ZoomInfo account has permission to view

## Data Storage and Security

### Local Storage

- **JWT Tokens**: Temporarily stored in Dify's secure key-value storage system for up to 55 minutes
- **Credentials**: Stored securely within Dify's credential management system
- **No Persistent Data**: The Plugin does not permanently store your ZoomInfo data

### Security Measures

- All communications with ZoomInfo use HTTPS encryption
- JWT tokens are automatically refreshed when expired
- Stored tokens are cleared when they expire
- Credentials are handled through Dify's secure credential management system

### Data Retention

- JWT tokens are automatically deleted after 55 minutes or when they expire
- No query results are permanently stored by the Plugin
- Credentials are retained only as long as you keep the Plugin configured in your Dify workspace

## Data Sharing and Third Parties

### No Third-Party Sharing

- Your ZoomInfo credentials and data are never shared with third parties
- The Plugin only communicates with ZoomInfo's official API endpoints and the Dify platform
- No analytics, tracking, or data collection services are used

### ZoomInfo Integration

- The Plugin connects directly to ZoomInfo's API using official ZoomInfo endpoints
- All data access is subject to your ZoomInfo account's permissions and subscription limits
- The Plugin respects all ZoomInfo data access controls and usage policies

## Your Rights and Controls

### Access Control

- You control which ZoomInfo data the Plugin can access through your search queries
- The Plugin can only access data that your ZoomInfo account has permission to view
- You can revoke access at any time by removing the Plugin configuration from Dify

### Data Deletion

- You can delete stored credentials by removing the Plugin configuration
- JWT token data is automatically purged when tokens expire
- No permanent copies of your ZoomInfo data are retained

## Compliance and Standards

### Security Standards

- The Plugin follows secure coding practices for credential handling
- All API communications use industry-standard encryption (HTTPS/TLS)
- Session management follows JWT and API security best practices

### ZoomInfo Compliance

- The Plugin uses official ZoomInfo APIs and follows ZoomInfo security guidelines
- All data access respects ZoomInfo's terms of service and usage policies
- The Plugin operates within ZoomInfo API rate limits and subscription boundaries

## Logging and Monitoring

### Operational Logs

The Plugin generates logs for:

- Authentication attempts (without storing actual credentials)
- API request status and errors
- JWT token management activities
- Query execution metadata

### Log Security

- Logs do not contain sensitive credential information
- Only operational metadata is logged for troubleshooting purposes
- Logs are managed according to Dify platform policies

## Data Types and Usage

### Company Data

- Company information is retrieved based on your search queries
- Data includes business details, financial information, and contact counts
- All company data access is subject to your ZoomInfo subscription permissions

### Contact Data

- Contact information is retrieved for specific individuals you search for
- Data includes professional contact details and job information
- Contact data access respects privacy regulations and ZoomInfo's compliance policies

### News Data

- News articles are retrieved for companies you specify
- Data includes article titles, sources, and publication dates
- News data is publicly available information aggregated by ZoomInfo

## Changes to This Privacy Policy

We may update this privacy policy from time to time. When we do:

- The "Last Updated" date at the top of this policy will be revised
- Significant changes will be communicated through appropriate channels
- Continued use of the Plugin after changes constitutes acceptance of the updated policy

## Contact Information

For questions about this privacy policy or the Plugin's data practices:

- **Plugin Author**: eric-2369
- **Repository**: https://github.com/Eric-2369/zoominfo-dify-plugin
- **Issues**: Please report privacy concerns through the GitHub repository issues

## Disclaimer

This Plugin is provided "as is" without warranties. Users are responsible for:

- Ensuring compliance with their organization's data policies
- Managing their ZoomInfo credentials securely
- Understanding their ZoomInfo account's data access permissions and subscription limits
- Complying with applicable data protection regulations (GDPR, CCPA, etc.)
- Adhering to ZoomInfo's terms of service and acceptable use policies

By using this Plugin, you acknowledge that you have read and understood this privacy policy and agree to its terms.
