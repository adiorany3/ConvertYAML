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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-UNKNOWN-VLESS-WS-98MS` (url=413ms, nekobox=370ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-105MS` (url=285ms, nekobox=324ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=284ms, nekobox=324ms, status=yes)
4. `AKUN-004-DIXONS-VLESS-WS-113MS` (url=294ms, nekobox=368ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=281ms, nekobox=357ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-102MS` (url=312ms, nekobox=294ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-115MS` (url=299ms, nekobox=407ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-119MS` (url=298ms, nekobox=323ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=298ms, nekobox=316ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-106MS` (url=315ms, nekobox=345ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-132MS` (url=314ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=351ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=358ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-150MS` (url=338ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-147MS` (url=350ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-157MS` (url=344ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=302ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-136MS` (url=307ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-126MS` (url=480ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-175MS` (url=352ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-154MS` (url=300ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-210MS` (url=429ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-131MS` (url=305ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-218MS` (url=568ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-181MS` (url=499ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
