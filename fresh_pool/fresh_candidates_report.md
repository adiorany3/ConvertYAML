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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=219ms, nekobox=257ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-84MS` (url=230ms, nekobox=267ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=229ms, nekobox=256ms, status=yes)
5. `AKUN-005-ICOOK-VLESS-WS-72MS` (url=216ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=230ms, nekobox=257ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-71MS` (url=215ms, nekobox=263ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-82MS` (url=211ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=229ms, nekobox=254ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-95MS` (url=237ms, nekobox=228ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-HOSTINGER-VLESS-WS-85MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-104MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-134MS` (url=245ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-143MS` (url=421ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-163MS` (url=372ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-153MS` (url=419ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-134MS` (url=423ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-187MS` (url=403ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-249MS` (url=564ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-356MS` (url=759ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-691MS` (url=1178ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-654MS` (url=1047ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-756MS` (url=1315ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
