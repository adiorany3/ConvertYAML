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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=215ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=221ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, nekobox=281ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-72MS` (url=226ms, nekobox=237ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-65MS` (url=210ms, nekobox=242ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-79MS` (url=212ms, nekobox=252ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-79MS` (url=201ms, nekobox=256ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-62MS` (url=206ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=206ms, nekobox=179ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-80MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-78MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-68MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-87MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-61MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-59MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-135MS` (url=258ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-87MS` (url=202ms, status=HTTP 204)
22. `AKUN-022-ADF-VLESS-WS-79MS` (url=196ms, status=HTTP 204)
23. `AKUN-023-COMPREND-NET-VLESS-WS-96MS` (url=214ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-357MS` (url=779ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-367MS` (url=713ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
