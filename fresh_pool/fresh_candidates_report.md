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
1. `AKUN-001-UNKNOWN-VLESS-WS-131MS` (url=289ms, nekobox=284ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-131MS` (url=274ms, nekobox=304ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-132MS` (url=260ms, nekobox=7172ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-136MS`
5. `AKUN-004-466688-VLESS-WS-137MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-138MS`
7. `AKUN-006-DIXONS-VLESS-WS-127MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-136MS`
9. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-144MS`
10. `AKUN-009-ZVC-VLESS-WS-139MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-142MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-140MS` (url=267ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-138MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-144MS` (url=284ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-141MS` (url=302ms, status=HTTP 204)
16. `AKUN-016-UK-GB-DCL-01-20191003-VLESS-WS-149MS` (url=280ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-163MS` (url=324ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-157MS` (url=299ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-159MS` (url=326ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-130MS` (url=264ms, status=HTTP 204)
21. `AKUN-021-CCWU-VLESS-WS-162MS` (url=270ms, status=HTTP 204)
22. `AKUN-022-WEBEX-VLESS-WS-139MS` (url=288ms, status=HTTP 204)
23. `AKUN-023-NEXUSMODS-VLESS-WS-170MS` (url=298ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-152MS` (url=282ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-171MS` (url=322ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
