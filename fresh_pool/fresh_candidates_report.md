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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=210ms, nekobox=232ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=224ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-63MS` (url=214ms, nekobox=229ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=236ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, nekobox=248ms, status=yes)
6. `AKUN-006-NET-82-21-84-0-24-VLESS-WS-86MS` (url=203ms, nekobox=247ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-71MS` (url=213ms, nekobox=226ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=210ms, nekobox=7172ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-78MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-86MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-MYBB-VLESS-WS-90MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-78MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-109MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-108MS` (url=199ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-118MS` (url=245ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-224MS` (url=474ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-225MS` (url=501ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=503ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-244MS` (url=968ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-250MS` (url=541ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
