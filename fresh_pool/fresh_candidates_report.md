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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=201ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=201ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=220ms, nekobox=189ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-71MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-59MS`
8. `AKUN-007-DEV-VLESS-WS-71MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-71MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-65MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-87MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-70MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-75MS` (url=197ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-81MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-77MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-008500-VLESS-WS-78MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-75MS` (url=202ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-76MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-74MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-101MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-90MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-78MS` (url=198ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-110MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-119MS` (url=213ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
