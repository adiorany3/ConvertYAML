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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=260ms, nekobox=270ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-85MS` (url=241ms, nekobox=276ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-84MS` (url=230ms, nekobox=272ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=254ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=275ms, nekobox=289ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-107MS` (url=237ms, nekobox=284ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, nekobox=260ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=250ms, nekobox=274ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-89MS` (url=269ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=246ms, status=HTTP 204)
13. `AKUN-013-WEYRO-NET-VLESS-WS-111MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-114MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-96MS` (url=276ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-110MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-1PASSWORD-VLESS-WS-91MS` (url=279ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-106MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-101MS` (url=256ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-193MS` (url=605ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-154MS` (url=303ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-97MS` (url=237ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-254MS` (url=566ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-265MS` (url=564ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-265MS` (url=572ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
