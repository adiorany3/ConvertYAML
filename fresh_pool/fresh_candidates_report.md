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
1. `AKUN-001-DEV-VLESS-WS-69MS` (url=214ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-85MS` (url=212ms, nekobox=230ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-79MS` (url=227ms, nekobox=226ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=218ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=232ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, nekobox=261ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-78MS` (url=200ms, nekobox=235ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-85MS` (url=224ms, nekobox=7177ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-93MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS`
12. `AKUN-012-DEV-VLESS-WS-77MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-81MS` (url=254ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-75MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=476ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-94MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-117MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-105MS` (url=239ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-112MS` (url=196ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-118MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-120MS` (url=218ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-154MS` (url=282ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-76MS` (url=232ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-74MS` (url=228ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
