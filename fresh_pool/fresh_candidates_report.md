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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=216ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=236ms, nekobox=248ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-57MS` (url=235ms, nekobox=279ms, status=yes)
4. `AKUN-004-CZ-LOTUNA-19970206-VLESS-WS-72MS` (url=218ms, nekobox=319ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=216ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=228ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=260ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=250ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=233ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=233ms, nekobox=276ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-78MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-67MS` (url=236ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-VOV-VLESS-WS-83MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-125MS` (url=258ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-66MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-113MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-129MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-ZOOM-VLESS-WS-80MS` (url=246ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-125MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS` (url=356ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-98MS` (url=242ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-367MS` (url=929ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-375MS` (url=808ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-370MS` (url=732ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
