# Patch WARM-UP Stabil-Responsif

Patch ini dibuat untuk mengurangi delay saat node baru dipakai, tanpa membebani router dengan health-check terlalu agresif ke semua node.

## Perubahan inti

- Menambahkan group `WARM-UP` bertipe `url-test`.
- `WARM-UP` hanya berisi 7 node otomatis terbaik berdasarkan delay di nama node.
- `WARM-UP` memakai:
  - `interval: 15`
  - `timeout: 3000`
  - `tolerance: 30`
  - `lazy: false`
  - `max-failed-times: 2`
- `GLOBAL`, `PROXY`, `SOCIAL-MEDIA`, `YOUTUBE`, `EDUKASI`, dan `STREAMING` sekarang menaruh `WARM-UP` di pilihan awal.
- `STREAMING-FAST` disederhanakan menjadi pool kecil yang sama-sama cepat, bukan semua node + manual, agar ping hijau lebih ringan dan stabil.
- `AUTO-FAST` tetap mengecek semua node otomatis, tetapi `timeout` dipangkas ke 3000 ms agar node mati tidak menahan koneksi terlalu lama.
- `FALLBACK` dijadikan cadangan aman dengan `interval: 60` dan `timeout: 5000`.
- `LOAD-BALANCE` hanya memakai pool cepat dan interval 90 detik, cocok untuk browsing/download, bukan jalur default streaming.
- Manual node tetap tidak mengurangi kuota otomatis dan tetap masuk `MANUAL` serta `FALLBACK`, tetapi tidak lagi dipaksa masuk `STREAMING-FAST` agar health-check tidak terlalu berat.

## Env baru di workflow

```yaml
WARMUP_INTERVAL: "15"
WARMUP_TIMEOUT_MS: "3000"
FAST_HEALTH_TIMEOUT_MS: "3000"
FALLBACK_INTERVAL: "60"
WARMUP_NODE_LIMIT: "7"
WARMUP_MAX_DELAY_MS: "180"
BALANCE_INTERVAL: "90"
```

## Hasil validasi

- Python compile: OK.
- YAML parse: OK.
- Referensi proxy/proxy-group: OK.
- Android YAML tetap tanpa `rule-providers`, `redir-port`, dan `tproxy-port`.
