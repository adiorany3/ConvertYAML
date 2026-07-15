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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=240ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=259ms, nekobox=257ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=228ms, nekobox=280ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-76MS` (url=240ms, nekobox=271ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-74MS` (url=236ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=240ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=235ms, nekobox=258ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-86MS` (url=272ms, nekobox=265ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=232ms, nekobox=258ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS` (url=246ms, nekobox=282ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-76MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-80MS` (url=242ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-76MS` (url=247ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-126MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-101MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-84MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-150MS` (url=240ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-83MS` (url=257ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-118MS` (url=240ms, status=HTTP 204)
23. `AKUN-023-HETZNER-VLESS-WS-138MS` (url=279ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-151MS` (url=238ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-112MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
