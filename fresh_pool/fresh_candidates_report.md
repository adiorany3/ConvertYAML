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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=203ms, nekobox=239ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=210ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=213ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=212ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=222ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=196ms, nekobox=189ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS`
8. `AKUN-007-VULTR-VLESS-WS-105MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS`
10. `AKUN-009-FMN5-RENTED-NET2-VLESS-WS-119MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-81MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-235MS` (url=497ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-244MS` (url=532ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-277MS` (url=603ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-279MS` (url=574ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-280MS` (url=591ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-242MS` (url=517ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-270MS` (url=579ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-400MS` (url=562ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-394MS` (url=567ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-431MS` (url=731ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-484MS` (url=563ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-585MS` (url=1390ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-674MS` (url=1217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
