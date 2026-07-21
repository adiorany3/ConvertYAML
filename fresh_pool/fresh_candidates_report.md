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
1. `AKUN-001-ORACLE-VLESS-WS-66MS` (url=238ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=243ms, nekobox=258ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=235ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=247ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=236ms, nekobox=270ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-86MS` (url=230ms, nekobox=262ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=276ms, nekobox=188ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS`
10. `AKUN-009-WPENG-VLESS-WS-113MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS`
12. `AKUN-013-ZVC-VLESS-WS-86MS` (url=239ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-127MS` (url=291ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=247ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-133MS` (url=234ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-117MS` (url=256ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-75MS` (url=256ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-128MS` (url=274ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=257ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-131MS` (url=258ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-126MS` (url=269ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-137MS` (url=243ms, status=HTTP 204)
23. `AKUN-024-PAGES-VLESS-WS-116MS` (url=248ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-112MS` (url=303ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-96MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
