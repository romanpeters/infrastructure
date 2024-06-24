server {
    listen 443 ssl;
    server_name ebooks.romanpeters.nl library.romanpeters.nl;

    ssl_certificate /etc/letsencrypt/live/romanpeters.nl/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/romanpeters.nl/privkey.pem;

    proxy_buffer_size 128k;
    proxy_buffers 4 256k;
    proxy_busy_buffers_size 256k;

    client_body_in_file_only clean;
    client_body_buffer_size 32K;
    client_max_body_size 300M;
    sendfile on;
    send_timeout 300s;

    location / {
	proxy_bind              $server_addr;
        proxy_pass http://10.10.20.25:8083;
        proxy_set_header        Host            $http_host;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Scheme        $scheme;
    }
}
