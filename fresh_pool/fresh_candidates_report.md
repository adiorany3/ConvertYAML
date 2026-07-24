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
1. `AKUN-001-UNKNOWN-VLESS-WS-53MS` (url=215ms, nekobox=262ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-55MS` (url=225ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-57MS` (url=212ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=218ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=216ms, nekobox=267ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS` (url=219ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-56MS` (url=216ms, nekobox=267ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=238ms, nekobox=264ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=238ms, nekobox=247ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-56MS` (url=220ms, nekobox=272ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-71MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-69MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=269ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-103MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-104MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-61MS` (url=241ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-128MS` (url=237ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-55MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-146MS` (url=238ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-136MS` (url=488ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-56MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-344MS` (url=759ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-337MS` (url=719ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
