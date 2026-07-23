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
1. `AKUN-001-CCWU-VLESS-WS-74MS` (url=244ms, nekobox=271ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-74MS` (url=235ms, nekobox=278ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-76MS` (url=270ms, nekobox=279ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-79MS` (url=301ms, nekobox=269ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=256ms, nekobox=273ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-88MS` (url=262ms, nekobox=280ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-87MS` (url=235ms, nekobox=276ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, nekobox=276ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=251ms, nekobox=284ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-77MS` (url=243ms, nekobox=278ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-88MS` (url=268ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-84MS` (url=304ms, status=HTTP 204)
15. `AKUN-015-SHOPIFY-VLESS-WS-86MS` (url=257ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-81MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-96MS` (url=197ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-96MS` (url=242ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-92MS` (url=248ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-96MS` (url=245ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-87MS` (url=278ms, status=HTTP 204)
23. `AKUN-023-MYBB-VLESS-WS-98MS` (url=278ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-77MS` (url=268ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-97MS` (url=248ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
