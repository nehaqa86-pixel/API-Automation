# GoRest API Tests

## Folder Structure

```
api_tests/
├── config/
│   └── config.py        # base_url and auth_token
├── tests/
│   └── test_users.py    # all test functions (GET, POST, PUT, DELETE, negative)
├── utils/
│   └── helpers.py       # generate_random_email()
└── README.md
```

## How to Run

```bash
cd api_tests
python tests/test_users.py
```
