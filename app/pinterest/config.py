PAGE_SIZE = 200
QUERY = "software engineer"
PRIMARY_CITY = '="São Paulo"'
URL_TEMPLATE = "https://jobsapi-google.m-cloud.io/api/job/search?pageSize={page_size}&offset=0&companyName=companies%2F201fe4ec-50f6-4262-92bf-3f1779cdcc41&query={query}&orderBy=relevance%20desc"
URL_TEMPLATE_CITY = "https://jobsapi-google.m-cloud.io/api/job/search?pageSize={page_size}&offset=0&companyName=companies%2F201fe4ec-50f6-4262-92bf-3f1779cdcc41&query={query}&customAttributeFilter=primary_city{primary_city}&orderBy=relevance%20desc"
TIMEOUT = 10
