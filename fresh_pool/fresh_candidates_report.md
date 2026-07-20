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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=228ms, nekobox=7176ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS`
4. `AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-86MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
7. `AKUN-006-ZVC-VLESS-WS-82MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-81MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=202ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-97MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-115MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-89MS` (url=236ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-107MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-243MS` (url=520ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-264MS` (url=660ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-272MS` (url=382ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-259MS` (url=523ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-89MS` (url=676ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-430MS` (url=1283ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
