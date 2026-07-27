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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=229ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=199ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=220ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=222ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=229ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-106MS` (url=219ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=227ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS` (url=217ms, nekobox=256ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-113MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-79MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-81MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-118MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-112MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-99MS` (url=228ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-120MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-122MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-SKK-VLESS-WS-147MS` (url=290ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-126MS` (url=279ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-165MS` (url=273ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-390MS` (url=823ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-363MS` (url=828ms, status=HTTP 204)
25. `AKUN-029-SUKARIO-VLESS-WS-637MS` (url=1081ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
