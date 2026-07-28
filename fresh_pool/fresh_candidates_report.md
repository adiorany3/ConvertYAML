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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=197ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=219ms, nekobox=256ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=214ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=228ms, nekobox=251ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-84MS` (url=219ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=227ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS` (url=219ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=199ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS` (url=202ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=197ms, nekobox=250ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-76MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-LEVIKOGJGFDD-VLESS-WS-118MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-91MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-120MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-ZOOM-VLESS-WS-57MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-145MS` (url=233ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-174MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-63MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-91MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-150MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-090227-VLESS-WS-280MS` (url=588ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-382MS` (url=2076ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-354MS` (url=746ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-559MS` (url=983ms, status=HTTP 204)
25. `AKUN-026-SUKARIO-VLESS-WS-696MS` (url=1067ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
