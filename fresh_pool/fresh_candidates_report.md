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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=207ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=230ms, nekobox=261ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=220ms, nekobox=260ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-78MS` (url=216ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=205ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS` (url=232ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=209ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=222ms, nekobox=248ms, status=yes)
10. `AKUN-010-CZ-LOTUNA-19970206-VLESS-WS-103MS` (url=215ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-129MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-154MS` (url=274ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-82MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-125MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-POLICE-VLESS-WS-160MS` (url=240ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-POLICE-VLESS-WS-132MS` (url=249ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-174MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-134MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-243MS` (url=515ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-257MS` (url=587ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
