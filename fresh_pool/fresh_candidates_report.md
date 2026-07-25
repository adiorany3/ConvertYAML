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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-95MS`
2. `AKUN-002-DEV-VLESS-WS-91MS`
3. `AKUN-003-ZVC-VLESS-WS-84MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-159MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-145MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-118MS`
7. `AKUN-007-ZVC-VLESS-WS-111MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-156MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=285ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-121MS` (url=286ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=278ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-312MS` (url=609ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-312MS` (url=603ms, status=HTTP 204)
16. `AKUN-017-DEV-VLESS-WS-320MS` (url=3285ms, status=HTTP 204)
17. `AKUN-018-DEV-VLESS-WS-302MS` (url=3600ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-302MS` (url=1647ms, status=HTTP 204)
19. `AKUN-020-DEV-VLESS-WS-312MS` (url=2153ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-308MS` (url=1640ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-298MS` (url=707ms, status=HTTP 204)
22. `AKUN-023-DEV-VLESS-WS-86MS` (url=690ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-99MS` (url=321ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-574MS` (url=990ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-575MS` (url=913ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
