# zoominfo-dify-plugin

A comprehensive Dify plugin that enables comprehensive company, contact, and news data enrichment using ZoomInfo API
with intelligent JWT token management.

- **Author:** eric-2369
- **Version:** 0.0.1
- **Type:** tool

## Features

- **JWT Authentication**: Secure authentication using username and password with automatic JWT token management
- **Smart Token Management**: Automatic token storage in Dify's KV storage with 55-minute expiry detection
- **Auto Token Refresh**: Automatic token refresh on 4xx errors with retry mechanism
- **Comprehensive Logging**: Full logging integration with Dify's plugin logging system
- **Multi-language Support**: English, Chinese, and Portuguese interface support
- **High Performance**: Efficient session management and API call optimization
- **Company Enrichment**: Retrieve detailed company information including revenue, employee count, and industry data
- **Contact Enrichment**: Find contact information for specific individuals at companies
- **News Enrichment**: Get recent news articles related to companies

## Installation

1. Install the plugin in your Dify environment
2. Configure your ZoomInfo credentials in the plugin settings

## Configuration

### Required Credentials

1. **ZoomInfo Username**
    - Your ZoomInfo account username/email

2. **ZoomInfo Password**
    - Your ZoomInfo account password

### Getting ZoomInfo API Access

1. Log in to your ZoomInfo account
2. Ensure you have API access enabled for your subscription
3. Contact ZoomInfo support if you need API access activated

## Usage

### 1. Company Enrichment

Retrieve detailed company information by company name.

**Parameters:**

- `company_name`: The name of the company to enrich
- `output_fields`: Comma-separated list of up to 5 fields to retrieve

**Example Fields:**

```
Basic Info: id, name, website, ticker, logo, phone, fax
Location: street, city, state, zipCode, country, continent, metroArea
Business: revenue, employeeCount, industries, primaryIndustry, companyStatus, foundedYear
Financial: revenueRange, employeeRange, companyFunding, recentFundingAmount
```

**Example Usage:**

```
Company Name: "Microsoft Corporation"
Output Fields: "name,website,employeeCount,revenue,industries"
```

### 2. Contact Enrichment

Find contact information for specific individuals at companies.

**Parameters:**

- `first_name`: First name of the contact
- `last_name`: Last name of the contact
- `company_name`: Company where the contact works
- `output_fields`: Comma-separated list of up to 5 fields to retrieve

**Example Fields:**

```
Personal Info: id, firstName, lastName, salutation, suffix, picture
Contact: email, phone, directPhoneDoNotCall, mobilePhoneDoNotCall
Job: jobTitle, jobFunction, managementLevel, positionStartDate
Company: companyId, companyName, companyPhone, companyWebsite
```

**Example Usage:**

```
First Name: "John"
Last Name: "Doe"
Company Name: "Microsoft Corporation"
Output Fields: "firstName,lastName,email,jobTitle,companyName"
```

### 3. News Enrichment

Get recent news articles related to a company.

**Parameters:**

- `company_id`: ZoomInfo company ID (obtained from company enrichment)
- `limit`: Number of news articles to retrieve (1-50)
- `page`: Page number for pagination (start with 1)
- `date_min`: Start date in YYYY-MM-DD format
- `date_max`: End date in YYYY-MM-DD format

**Example Usage:**

```
Company ID: 12345678
Limit: 10
Page: 1
Start Date: "2024-01-01"
End Date: "2024-12-31"
```

## API Response Format

### Company Enrichment Response

```json
{
  "company_name": "Microsoft Corporation",
  "requested_fields": [
    "name",
    "website",
    "employeeCount",
    "revenue",
    "industries"
  ],
  "data": {
    "data": [
      {
        "id": 12345678,
        "name": "Microsoft Corporation",
        "website": "https://www.microsoft.com",
        "employeeCount": 221000,
        "revenue": 211915000000,
        "industries": [
          "Software",
          "Technology"
        ]
      }
    ]
  },
  "status": "success"
}
```

### Contact Enrichment Response

```json
{
  "contact_name": "John Doe",
  "company_name": "Microsoft Corporation",
  "requested_fields": [
    "firstName",
    "lastName",
    "email",
    "jobTitle",
    "companyName"
  ],
  "data": {
    "data": [
      {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@microsoft.com",
        "jobTitle": "Senior Software Engineer",
        "companyName": "Microsoft Corporation"
      }
    ]
  },
  "status": "success"
}
```

### News Enrichment Response

```json
{
  "company_id": 12345678,
  "limit": 10,
  "page": 1,
  "date_range": {
    "start": "2024-01-01",
    "end": "2024-12-31"
  },
  "data": {
    "data": [
      {
        "title": "Microsoft Announces New AI Initiative",
        "url": "https://example.com/news/microsoft-ai",
        "publishedDate": "2024-06-15",
        "source": "Tech News"
      }
    ]
  },
  "status": "success"
}
```

## Technical Architecture

### Session Management

- **JWT Authentication**: Uses ZoomInfo API for initial authentication with username/password
- **Token Storage**: Stores JWT tokens in Dify's KV storage for persistence
- **Automatic Refresh**: Monitors token expiry (55-minute safety margin) and refreshes automatically
- **Error Recovery**: Handles 4xx errors by refreshing tokens and retrying

### Security Features

- **Secure Credential Storage**: All credentials are securely stored in Dify
- **Token Expiry Management**: Proactive token refresh before expiry
- **Error Handling**: Comprehensive error handling with user-friendly messages

### Performance Optimization

- **Session Caching**: Reuses valid JWT tokens to minimize authentication calls
- **Efficient API Calls**: Optimized HTTP requests with proper timeouts
- **Memory Management**: Efficient memory usage in serverless environment

## Error Handling

The plugin provides comprehensive error handling for common scenarios:

- **Invalid Credentials**: Clear messages for authentication failures
- **Network Issues**: Timeout and connection error handling
- **API Parameter Errors**: Detailed error messages for invalid requests
- **Rate Limits**: Proper handling of ZoomInfo API limits
- **Token Expiry**: Automatic token refresh and retry
- **Data Not Found**: Graceful handling when companies/contacts are not found

## Logging

The plugin uses Dify's logging system to record:

- Authentication attempts and results
- API call executions for company, contact, and news enrichment
- Token refresh operations
- Error conditions and resolutions

## Troubleshooting

### Common Issues

1. **Authentication Failed**
    - Verify your ZoomInfo username and password
    - Ensure your account has API access enabled
    - Check if your ZoomInfo subscription includes API usage

2. **Company/Contact Not Found**
    - Verify the company name is spelled correctly
    - Try using the official company name
    - Ensure the contact exists in ZoomInfo's database

3. **Invalid Output Fields**
    - Check that field names are spelled correctly
    - Ensure you're not requesting more than 5 fields
    - Refer to the field lists in the usage section

4. **Network Timeouts**
    - Check your network connection
    - Ensure firewall allows outbound HTTPS connections to api.zoominfo.com

5. **News Enrichment Issues**
    - Ensure you have a valid company ID from company enrichment
    - Check that date format is YYYY-MM-DD
    - Verify date range is logical (start date before end date)

## Development

### Project Structure

```
zoominfo-dify-plugin/
├── manifest.yaml              # Plugin configuration
├── requirements.txt           # Python dependencies
├── provider/
│   ├── zoominfo.yaml         # Provider configuration
│   └── zoominfo.py           # Credential validation
├── tools/
│   ├── enrich_company.yaml   # Company enrichment tool configuration
│   ├── enrich_company.py     # Company enrichment implementation
│   ├── enrich_contact.yaml   # Contact enrichment tool configuration
│   ├── enrich_contact.py     # Contact enrichment implementation
│   ├── enrich_news.yaml      # News enrichment tool configuration
│   └── enrich_news.py        # News enrichment implementation
└── utils/
    └── session_manager.py     # JWT token management logic
```

### Key Components

- **ZoomInfoSessionManager**: Handles JWT authentication and token management
- **ZoomInfoProvider**: Validates credentials during plugin configuration
- **EnrichCompanyTool**: Retrieves company information with automatic error handling
- **EnrichContactTool**: Finds contact information with validation
- **EnrichNewsTool**: Fetches company news with date filtering

### API Endpoints Used

- **Authentication**: `https://api.zoominfo.com/authenticate`
- **Company Enrichment**: `https://api.zoominfo.com/enrich/company`
- **Contact Enrichment**: `https://api.zoominfo.com/enrich/contact`
- **News**: `https://api.zoominfo.com/enrich/news`

## License

This project is licensed under the terms specified in the LICENSE file.

## Support

For issues and questions:

1. Check the troubleshooting section above
2. Review ZoomInfo API documentation
3. Contact the plugin author

## Disclaimer

This plugin is provided "as is" without warranties. Users are responsible for:

- Ensuring compliance with ZoomInfo's terms of service
- Managing their ZoomInfo credentials securely
- Understanding their ZoomInfo subscription limits and permissions
- Complying with applicable data protection regulations
