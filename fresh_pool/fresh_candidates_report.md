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
1. `AKUN-001-ZVC-VLESS-WS-55MS` (url=220ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=211ms, nekobox=243ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-54MS` (url=215ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS` (url=210ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=215ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS` (url=217ms, nekobox=7177ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-62MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS`
9. `AKUN-008-DEV-VLESS-WS-64MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-107MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-71MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-113MS` (url=809ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-90MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-71MS` (url=333ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-117MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-88MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-81MS` (url=196ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-90MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-FMN5-RENTED-NET2-VLESS-WS-98MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-167MS` (url=214ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-133MS` (url=224ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-490MS` (url=878ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-594MS` (url=967ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
