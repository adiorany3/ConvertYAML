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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-MVPS-NET-VLESS-WS-75MS` (url=218ms, nekobox=263ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-81MS` (url=222ms, nekobox=249ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-97MS` (url=238ms, nekobox=250ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-83MS` (url=214ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS` (url=232ms, nekobox=243ms, status=yes)
6. `AKUN-006-OPENAI-VLESS-WS-87MS` (url=208ms, nekobox=230ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=227ms, nekobox=295ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=206ms, nekobox=242ms, status=yes)
9. `AKUN-009-EU-VLESS-WS-91MS` (url=211ms, nekobox=295ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=216ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-NATO-US-2-VLESS-WS-115MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-89MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=276ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-252MS` (url=549ms, status=HTTP 204)
18. `AKUN-021-CONFLU-VLESS-WS-357MS` (url=734ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-376MS` (url=709ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-465MS` (url=1010ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-664MS` (url=1530ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-688MS` (url=1214ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-644MS` (url=969ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-719MS` (url=1230ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-750MS` (url=1105ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
