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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=240ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=254ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=208ms, nekobox=272ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, nekobox=284ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-62MS` (url=213ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-76MS` (url=272ms, nekobox=274ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS` (url=206ms, nekobox=260ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=214ms, nekobox=260ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=209ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-75MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-77MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-85MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-74MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-367MS` (url=723ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-73MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-80MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-408MS` (url=958ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-411MS` (url=845ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-82MS` (url=221ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-82MS` (url=287ms, status=HTTP 204)
23. `AKUN-023-OPENAI-VLESS-WS-74MS` (url=233ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-390MS` (url=851ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-383MS` (url=759ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
