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
1. `AKUN-001-VULTR-VLESS-WS-67MS` (url=239ms, nekobox=272ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=225ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=225ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=331ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=227ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=267ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=274ms, nekobox=288ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=240ms, nekobox=270ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=223ms, nekobox=263ms, status=yes)
10. `AKUN-010-IDC-SG-VLESS-WS-108MS` (url=252ms, nekobox=303ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-114MS` (url=268ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-78MS` (url=240ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-97MS` (url=270ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-92MS` (url=261ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-193MS` (url=406ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-199MS` (url=600ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-244MS` (url=628ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-268MS` (url=583ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-285MS` (url=566ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-287MS` (url=628ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-297MS` (url=724ms, status=HTTP 204)
24. `AKUN-027-SPEEDTEST-VLESS-WS-330MS` (url=567ms, status=HTTP 204)
25. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-516MS` (url=936ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
