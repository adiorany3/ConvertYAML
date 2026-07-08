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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=224ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=221ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=228ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=198ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=215ms, nekobox=249ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=226ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=212ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=219ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-67MS` (url=222ms, nekobox=228ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-79MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-102MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-80MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-71MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=201ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-352MS` (url=782ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-346MS` (url=789ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-361MS` (url=750ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-390MS` (url=847ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-415MS` (url=864ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-636MS` (url=1155ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-819MS` (url=1425ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-716MS` (url=1153ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
