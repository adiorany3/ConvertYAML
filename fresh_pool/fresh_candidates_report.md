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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-80MS` (url=226ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=205ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=201ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=236ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-76MS` (url=223ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS` (url=213ms, nekobox=257ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=204ms, nekobox=263ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=222ms, nekobox=247ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-93MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-SHOPIFY-VLESS-WS-104MS` (url=233ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-108MS` (url=207ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-109MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-118MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-99MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-138MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-131MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-129MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-120MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-87MS` (url=240ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-88MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-93MS` (url=232ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-89MS` (url=226ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-237MS` (url=583ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
