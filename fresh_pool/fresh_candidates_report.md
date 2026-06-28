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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-134MS` (url=265ms, nekobox=289ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-139MS` (url=299ms, nekobox=334ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS` (url=254ms, nekobox=277ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-149MS` (url=239ms, nekobox=285ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-134MS` (url=281ms, nekobox=298ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-144MS` (url=247ms, nekobox=299ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-139MS` (url=291ms, nekobox=291ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-142MS` (url=244ms, nekobox=298ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-136MS` (url=269ms, nekobox=311ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-137MS` (url=314ms, nekobox=313ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-155MS` (url=250ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-155MS` (url=278ms, status=HTTP 204)
13. `AKUN-013-ZOOM-VLESS-WS-159MS` (url=304ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-170MS` (url=280ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-161MS` (url=273ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-171MS` (url=278ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-185MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-159MS` (url=261ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-163MS` (url=255ms, status=HTTP 204)
20. `AKUN-020-MYBB-VLESS-WS-139MS` (url=250ms, status=HTTP 204)
21. `AKUN-021-COMPREND-NET-VLESS-WS-185MS` (url=260ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-285MS` (url=495ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-350MS` (url=666ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-344MS` (url=671ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-371MS` (url=796ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
