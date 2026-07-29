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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS` (url=905ms, nekobox=311ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-104MS` (url=923ms, nekobox=357ms, status=yes)
3. `AKUN-003-LEVIKOGJGFDD-VLESS-WS-106MS` (url=328ms, nekobox=945ms, status=yes)
4. `AKUN-004-ES-FORNEX-20160629-VLESS-WS-110MS` (url=905ms, nekobox=356ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-104MS` (url=947ms, nekobox=371ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-116MS` (url=761ms, nekobox=217ms, status=no)
7. `AKUN-006-1PASSWORD-VLESS-WS-122MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-122MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS`
11. `AKUN-010-HOSTINGER-VLESS-WS-126MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-145MS` (url=347ms, status=HTTP 204)
14. `AKUN-014-LEVIKOGJGFDD-VLESS-WS-183MS` (url=971ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-106MS` (url=274ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-168MS` (url=1054ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-299MS` (url=1373ms, status=HTTP 204)
18. `AKUN-018-LEVIKOGJGFDD-VLESS-WS-303MS` (url=1673ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-152MS` (url=288ms, status=HTTP 204)
20. `AKUN-021-LEVIKOGJGFDD-VLESS-WS-100MS` (url=911ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-109MS` (url=320ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-561MS` (url=1715ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-215MS` (url=306ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-125MS` (url=284ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-153MS` (url=1145ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
