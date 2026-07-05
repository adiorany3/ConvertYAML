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
1. `AKUN-001-OVH-VLESS-WS-61MS` (url=225ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=231ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=215ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=226ms, nekobox=244ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-66MS` (url=223ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS` (url=212ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS` (url=215ms, nekobox=248ms, status=yes)
8. `AKUN-008-CELESTARA-VLESS-WS-66MS` (url=218ms, nekobox=237ms, status=yes)
9. `AKUN-009-OVH-VLESS-WS-66MS` (url=201ms, nekobox=242ms, status=yes)
10. `AKUN-010-OVH-VLESS-WS-75MS` (url=204ms, nekobox=258ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-82MS` (url=216ms, status=HTTP 204)
13. `AKUN-014-WPENG-VLESS-WS-67MS` (url=217ms, status=HTTP 204)
14. `AKUN-015-ALIBABA-VLESS-WS-86MS` (url=214ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-117MS` (url=216ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-348MS` (url=744ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-365MS` (url=746ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-355MS` (url=759ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-374MS` (url=883ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-377MS` (url=790ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-384MS` (url=813ms, status=HTTP 204)
23. `AKUN-024-OCTOPUSSS5-VLESS-WS-371MS` (url=829ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-360MS` (url=1083ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-653MS` (url=1148ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
