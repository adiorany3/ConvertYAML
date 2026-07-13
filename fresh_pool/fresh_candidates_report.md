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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=227ms, nekobox=276ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, nekobox=277ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=234ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-80MS` (url=234ms, nekobox=274ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-87MS` (url=252ms, nekobox=257ms, status=yes)
7. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-73MS` (url=233ms, nekobox=298ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=263ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-72MS` (url=248ms, nekobox=264ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=241ms, nekobox=268ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-74MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-76MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-71MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-100MS` (url=239ms, status=HTTP 204)
19. `AKUN-019-OVH-VLESS-WS-97MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-CONFLU-VLESS-WS-261MS` (url=615ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-89MS` (url=281ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-89MS` (url=245ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-286MS` (url=736ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-118MS` (url=294ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-247MS` (url=359ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
