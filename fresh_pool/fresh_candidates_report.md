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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=258ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=273ms, nekobox=309ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=277ms, nekobox=322ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-81MS` (url=245ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=244ms, nekobox=190ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
7. `AKUN-007-DEV-VLESS-WS-93MS` (url=266ms, nekobox=195ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS`
9. `AKUN-010-DEV-VLESS-WS-86MS` (url=268ms, nekobox=196ms, status=no)
10. `AKUN-011-DEV-VLESS-WS-82MS` (url=255ms, nekobox=206ms, status=no)
11. `AKUN-012-DEV-VLESS-WS-84MS` (url=264ms, nekobox=190ms, status=no)
12. `AKUN-007-466688-VLESS-WS-94MS`
13. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
14. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS`
15. `AKUN-016-CLOUDFLARE-VLESS-WS-95MS` (url=241ms, nekobox=7177ms, status=no)
16. `AKUN-010-ZVC-VLESS-WS-95MS`
17. `AKUN-018-CLOUDFLARE-VLESS-WS-154MS` (url=280ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-124MS` (url=256ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-268MS` (url=627ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-277MS` (url=658ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-292MS` (url=683ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-256MS` (url=1571ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-256MS` (url=594ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-306MS` (url=673ms, status=HTTP 204)
25. `AKUN-026-HETZNER-VLESS-WS-98MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
