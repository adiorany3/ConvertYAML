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
1. `AKUN-001-090227-VLESS-WS-61MS` (url=203ms, nekobox=243ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=224ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-66MS` (url=224ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=238ms, nekobox=231ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=208ms, nekobox=254ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=202ms, nekobox=248ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-71MS` (url=222ms, nekobox=258ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=205ms, nekobox=242ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-95MS` (url=231ms, nekobox=227ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=212ms, nekobox=231ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-134MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-190MS` (url=199ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-374MS` (url=735ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-347MS` (url=768ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-388MS` (url=810ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-399MS` (url=869ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-407MS` (url=841ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-363MS` (url=791ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-404MS` (url=818ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-735MS` (url=1177ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-647MS` (url=1052ms, status=HTTP 204)
23. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-702MS` (url=1260ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-823MS` (url=1864ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-861MS` (url=1266ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
