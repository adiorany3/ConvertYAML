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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=213ms, nekobox=250ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS`
4. `AKUN-004-ZVC-VLESS-WS-86MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS`
6. `AKUN-007-UNKNOWN-VLESS-WS-78MS` (url=229ms, nekobox=5157ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-107MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-126MS`
12. `AKUN-013-NODEHOST-VLESS-WS-128MS` (url=226ms, status=HTTP 204)
13. `AKUN-014-ORG-VLESS-WS-88MS` (url=233ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-129MS` (url=251ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=242ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-118MS` (url=233ms, status=HTTP 204)
17. `AKUN-018-ES-FORNEX-20160629-VLESS-WS-139MS` (url=205ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-237MS` (url=447ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-250MS` (url=683ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-243MS` (url=527ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-241MS` (url=509ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-269MS` (url=579ms, status=HTTP 204)
23. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-287MS` (url=590ms, status=HTTP 204)
24. `AKUN-026-NET-89-116-72-0-24-VLESS-WS-349MS` (url=625ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-459MS` (url=725ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
