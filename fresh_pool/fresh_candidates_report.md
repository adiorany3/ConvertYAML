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
1. `AKUN-001-DIGITALOCEAN-VLESS-WS-73MS` (url=248ms, nekobox=275ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-72MS` (url=232ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=290ms, nekobox=264ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=241ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=274ms, nekobox=183ms, status=no)
6. `AKUN-005-156-246-89-0-156-246-89-VLESS-WS-71MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-88MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-72MS`
10. `AKUN-009-US-VLESS-WS-73MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-78MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-70MS` (url=394ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=286ms, status=HTTP 204)
16. `AKUN-016-CLOUDWEBMANAGE-EU-FR-VLESS-WS-142MS` (url=247ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-71MS` (url=257ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-80MS` (url=281ms, status=HTTP 204)
19. `AKUN-020-1PASSWORD-VLESS-WS-70MS` (url=251ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-268MS` (url=560ms, status=HTTP 204)
21. `AKUN-022-CONFLU-VLESS-WS-271MS` (url=587ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-287MS` (url=545ms, status=HTTP 204)
23. `AKUN-025-WPENG-VLESS-WS-299MS` (url=619ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-309MS` (url=640ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-304MS` (url=661ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
