# Patch Streaming Fast

Patch ini menambahkan grup khusus `STREAMING-FAST` untuk OpenClash.

Tujuannya:

- Traffic web streaming masuk ke grup `STREAMING`.
- `STREAMING` memilih `STREAMING-FAST` sebagai prioritas pertama.
- `STREAMING-FAST` memakai `url-test` sendiri dengan `STREAMING_TEST_URL`, sehingga node streaming bisa berbeda dari `AUTO-FAST`, `GLOBAL`, `FALLBACK`, atau `LOAD-BALANCE`.
- Mode `Lite` tetap punya rule domain streaming agar traffic Netflix, Disney+, Prime Video, Spotify, Twitch, Vidio, Vision+, dan layanan streaming lain tidak jatuh ke `MATCH,GLOBAL`.

Env yang ditambahkan di workflow:

```yaml
STREAMING_TEST_URL: "https://www.netflix.com/"
STREAMING_EXPECTED_STATUS: "200/204/301/302/403"
STREAMING_URLTEST_INTERVAL: "60"
STREAMING_TOLERANCE: "5"
STREAMING_HEALTH_TIMEOUT_MS: "6000"
```

Kalau Netflix test terasa kurang cocok di jaringan tertentu, ubah `STREAMING_TEST_URL` ke:

```yaml
STREAMING_TEST_URL: "https://www.gstatic.com/generate_204"
```
