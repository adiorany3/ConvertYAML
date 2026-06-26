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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=240ms, nekobox=254ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-78MS` (url=229ms, nekobox=246ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-80MS` (url=205ms, nekobox=231ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=226ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=212ms, nekobox=253ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=231ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=202ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=220ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-125MS` (url=212ms, nekobox=253ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-106MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-137MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-159MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-165MS` (url=247ms, status=HTTP 204)
16. `AKUN-016-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-64MS` (url=198ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-180MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-345MS` (url=647ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-373MS` (url=768ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-387MS` (url=879ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-396MS` (url=855ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-422MS` (url=846ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-393MS` (url=884ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-717MS` (url=1108ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-391MS` (url=989ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
