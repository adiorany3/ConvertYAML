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
1. `AKUN-001-GOV-VLESS-WS-122MS` (url=249ms, nekobox=281ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-126MS` (url=258ms, nekobox=281ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-127MS` (url=263ms, nekobox=288ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-123MS` (url=258ms, nekobox=289ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-132MS` (url=269ms, nekobox=280ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-139MS` (url=248ms, nekobox=290ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-142MS` (url=309ms, nekobox=282ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-144MS` (url=251ms, nekobox=291ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-149MS` (url=258ms, nekobox=310ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-147MS` (url=250ms, nekobox=290ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-154MS` (url=264ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-149MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-135MS` (url=251ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-199MS` (url=329ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-171MS` (url=280ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-135MS` (url=309ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-207MS` (url=350ms, status=HTTP 204)
19. `AKUN-019-SKK-VLESS-WS-293MS` (url=493ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-343MS` (url=1013ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-370MS` (url=4603ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-407MS` (url=774ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-646MS` (url=1112ms, status=HTTP 204)
24. `AKUN-025-SPEEDTEST-VLESS-WS-706MS` (url=949ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-806MS` (url=1352ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
