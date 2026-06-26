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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=212ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=222ms, nekobox=255ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=225ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=200ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=219ms, nekobox=227ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS` (url=214ms, nekobox=258ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=224ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS` (url=205ms, nekobox=247ms, status=yes)
9. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-78MS` (url=240ms, nekobox=230ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=194ms, nekobox=269ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-128MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-112MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-150MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-84MS` (url=219ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-357MS` (url=749ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-400MS` (url=819ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-386MS` (url=649ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-407MS` (url=852ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-362MS` (url=740ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-128MS` (url=388ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-454MS` (url=852ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-72MS` (url=539ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
