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
1. `AKUN-001-RU-BEGET-VLESS-WS-90MS` (url=232ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=216ms, nekobox=259ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=205ms, nekobox=245ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=226ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=213ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=218ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=212ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=232ms, nekobox=312ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=217ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-134MS` (url=218ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-99MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-142MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-98MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-139MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-143MS` (url=333ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-104MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-111MS` (url=252ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-161MS` (url=309ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-149MS` (url=254ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-180MS` (url=328ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-192MS` (url=322ms, status=HTTP 204)
23. `AKUN-023-US-VLESS-WS-164MS` (url=251ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-172MS` (url=278ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-133MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
