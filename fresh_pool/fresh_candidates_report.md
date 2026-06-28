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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=210ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=234ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=225ms, nekobox=186ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS`
8. `AKUN-007-DE-XTOM-20210903-VLESS-WS-79MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
10. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-74MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-105MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-96MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=198ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-117MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-US-VLESS-WS-118MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-104MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-ADF-VLESS-WS-71MS` (url=203ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-90MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-155MS` (url=227ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-246MS` (url=557ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-227MS` (url=487ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-252MS` (url=548ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-275MS` (url=551ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-251MS` (url=495ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
