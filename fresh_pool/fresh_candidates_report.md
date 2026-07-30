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
1. `AKUN-001-ICOOK-VLESS-WS-76MS` (url=210ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=226ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=226ms, nekobox=186ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-99MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-101MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-118MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-90MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-104MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-136MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-176MS` (url=317ms, status=HTTP 204)
16. `AKUN-017-090227-VLESS-WS-175MS` (url=375ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-203MS` (url=281ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-235MS` (url=485ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-245MS` (url=3160ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-319MS` (url=733ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-392MS` (url=676ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-421MS` (url=704ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-401MS` (url=668ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-535MS` (url=848ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-524MS` (url=862ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
