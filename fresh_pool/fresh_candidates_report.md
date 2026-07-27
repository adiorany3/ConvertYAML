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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-101MS`
2. `AKUN-004-CLOUDFLARE-VLESS-WS-106MS` (url=283ms, nekobox=186ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-105MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-119MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-129MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-114MS`
9. `AKUN-008-ADF-VLESS-WS-95MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=279ms, nekobox=7172ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS`
13. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=308ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-99MS` (url=288ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-119MS` (url=288ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=386ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-283MS` (url=608ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-331MS` (url=637ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-333MS` (url=556ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=286ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-103MS` (url=276ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-192MS` (url=453ms, status=HTTP 204)
23. `AKUN-025-DEV-VLESS-WS-115MS` (url=619ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-551MS` (url=861ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-350MS` (url=589ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
