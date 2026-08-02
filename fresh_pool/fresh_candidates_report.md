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
1. `AKUN-001-UNKNOWN-VLESS-WS-53MS` (url=217ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=224ms, nekobox=174ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-56MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-58MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-97MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-105MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-79MS` (url=225ms, nekobox=184ms, status=no)
12. `AKUN-012-DEV-VLESS-WS-89MS` (url=210ms, nekobox=7177ms, status=no)
13. `AKUN-010-UNKNOWN-VLESS-WS-67MS`
14. `AKUN-014-UNKNOWN-VLESS-WS-94MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CHATGPT-VLESS-WS-117MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-139MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-300MS` (url=582ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-497MS` (url=989ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-518MS` (url=1031ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-604MS` (url=1048ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-662MS` (url=1090ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-650MS` (url=956ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-660MS` (url=1063ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-657MS` (url=1071ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
