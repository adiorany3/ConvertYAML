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
1. `AKUN-001-UNKNOWN-VLESS-WS-124MS` (url=246ms, nekobox=283ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-129MS` (url=263ms, nekobox=291ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-116MS` (url=264ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS` (url=256ms, nekobox=279ms, status=yes)
5. `AKUN-005-EU-VLESS-WS-124MS` (url=732ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-178MS` (url=275ms, nekobox=350ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-199MS` (url=296ms, nekobox=387ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-137MS` (url=309ms, nekobox=428ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=275ms, nekobox=282ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-174MS` (url=362ms, nekobox=357ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-257MS` (url=313ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-136MS` (url=262ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-150MS` (url=325ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-411MS` (url=2888ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-439MS` (url=876ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-541MS` (url=960ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-702MS` (url=1124ms, status=HTTP 204)
18. `AKUN-020-HOSTES-LLC-VLESS-WS-756MS` (url=1224ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-257MS` (url=752ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-726MS` (url=1148ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-468MS` (url=828ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-361MS` (url=1549ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-843MS` (url=1398ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-823MS` (url=1303ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-862MS` (url=4597ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
