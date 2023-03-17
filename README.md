# Requirements

- Docker
- Eslint

# Setup

1. Init configuration
    ```bash
    ./cmd init
    ```

2. Build docker images
    ```bash
    ./cmd docker build
    ```
    
3. Start docker services
    ```bash
    ./cmd docker up
    ```

4. Serve frontend
    ```bash
    ./cmd node serve
    ```


5. Serve backend
    ```bash
    ./cmd app install
    ./cmd app serve
    ./cmd app start uvicorn
    ```

6. Manage supervisord
    ```bash
    ./cmd app status all
    ```