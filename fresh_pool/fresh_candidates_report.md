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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=221ms, nekobox=244ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-68MS` (url=209ms, nekobox=227ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=207ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=219ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=200ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=218ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-120MS` (url=207ms, nekobox=231ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS` (url=226ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-88MS` (url=229ms, nekobox=260ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-121MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-117MS` (url=245ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-116MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-111MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-98MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-138MS` (url=196ms, status=HTTP 204)
17. `AKUN-018-ZVC-VLESS-WS-110MS` (url=253ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-136MS` (url=227ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-251MS` (url=503ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-252MS` (url=558ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-271MS` (url=1168ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-252MS` (url=570ms, status=HTTP 204)
23. `AKUN-025-SPEEDTEST-VLESS-WS-260MS` (url=555ms, status=HTTP 204)
24. `AKUN-026-SPEEDTEST-VLESS-WS-290MS` (url=735ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-114MS` (url=535ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
