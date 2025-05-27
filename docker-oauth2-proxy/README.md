# oauth2-proxy

## Description

oauth2 Proxy service

## Setup

Copy the file `env-example` to `.env` and replace the variable values

- Use the following command to generate a cookie secret

```sh
python -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
```

- update to your domain and port.
- This example is prepared for Google OAuth.
  - You need to create an OAuth ID and secret go to `https://console.cloud.google.com/apis/dashboard` if you don't have one already
- If you are using a different OAuth provider check the reference link for specific configurations
- To finish replace auth_users with the list of email addresses you will allow

Just run docker compose

```sh
docker-compose up -d
```

This will start the oauth-proxy service you will need some configuration on your webserver to proxy autentications for this service.

The following is an example for Nginx

```conf
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name mydomain.com;
    ssl_certificate /etc/nginx/ssl/mydomain/fullchain.cer;
    ssl_certificate_key /etc/nginx/ssl/mydomain/private.key;
    root /usr/share/nginx/html;

    if ($host != $server_name) {
        return 404;
    }
    add_header Strict-Transport-Security "max-age=31536000;  includeSubDomains " always;

   location / {
        try_files $uri $uri/ =404;
        auth_request /oauth2/auth;
        error_page 401 = /oauth2/sign_in?rd=https://$host$request_uri;
        auth_request_set $user   $upstream_http_x_auth_request_user;
        auth_request_set $email  $upstream_http_x_auth_request_email;
        proxy_set_header X-User  $user;
        proxy_set_header X-Email $email;
        auth_request_set $auth_cookie $upstream_http_set_cookie;
        add_header Set-Cookie $auth_cookie;
    }
    location /oauth2/ {
        proxy_pass http://127.0.0.1:4180;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Auth-Request-Redirect $scheme://$host$request_uri;
    }
    location /oauth2/auth {
        proxy_pass http://127.0.0.1:4180;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header Content-Length   "";
        proxy_pass_request_body off;
    }
}
```

**NOTE:** This example configuration considers the service running in port `4180`

## Connect

Upon restarting nginx you should be requested to auth in Google for default location and be redirected

## References

- <https://oauth2-proxy.github.io/oauth2-proxy/7.1.x/configuration/overview>

## Metadata

**Last Verified:** 2025/05/28
