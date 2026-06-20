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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-132MS` (url=267ms, nekobox=303ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS` (url=265ms, nekobox=292ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-135MS` (url=267ms, nekobox=303ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-137MS` (url=272ms, nekobox=290ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-143MS` (url=265ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-137MS` (url=240ms, nekobox=227ms, status=no)
7. `AKUN-006-ADF-VLESS-WS-141MS`
8. `AKUN-007-MYBB-VLESS-WS-189MS`
9. `AKUN-008-MEDIUM-VLESS-WS-167MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-169MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-132MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-131MS` (url=258ms, status=HTTP 204)
13. `AKUN-014-008500-VLESS-WS-140MS` (url=242ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-359MS` (url=704ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-150MS` (url=291ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-397MS` (url=790ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-385MS` (url=775ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-141MS` (url=274ms, status=HTTP 204)
19. `AKUN-021-US-VLESS-WS-136MS` (url=277ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-584MS` (url=747ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-380MS` (url=773ms, status=HTTP 204)
22. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-643MS` (url=2924ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-373MS` (url=711ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-388MS` (url=780ms, status=HTTP 204)
25. `AKUN-029-BROADNNET-KR-VLESS-WS-700MS` (url=943ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
