# weather

## BACKEND CONFIGURATION
To run the app in uvicorn locally

```
$ cp backend/env.example backend/env
# edit backend/env with your config values
$ source backend/env
$ uvicorn backend.main:app --reload
```

