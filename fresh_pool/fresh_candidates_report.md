# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-116MS` (url=667ms, nekobox=219ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-101MS`
3. `AKUN-002-ZVC-VLESS-WS-104MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-113MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-121MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-106MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-121MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-115MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=295ms, nekobox=229ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-134MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=302ms, nekobox=222ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-123MS`
14. `AKUN-015-DEV-VLESS-WS-119MS` (url=312ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-116MS` (url=338ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=298ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-119MS` (url=285ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-155MS` (url=338ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=288ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-147MS` (url=295ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-156MS` (url=312ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-171MS` (url=364ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-320MS` (url=696ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-330MS` (url=1348ms, status=HTTP 204)
25. `AKUN-027-IRANHONY-VLESS-WS-437MS` (url=569ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
