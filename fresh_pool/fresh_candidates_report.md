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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=227ms, nekobox=255ms, status=yes)
2. `AKUN-002-OPENAI-VLESS-WS-88MS` (url=223ms, nekobox=238ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-90MS` (url=229ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=214ms, nekobox=258ms, status=yes)
5. `AKUN-005-008500-VLESS-WS-85MS` (url=205ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=197ms, status=no)
7. `AKUN-006-DEV-VLESS-WS-79MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-114MS`
9. `AKUN-008-U1HOST-FRA-VLESS-WS-121MS`
10. `AKUN-009-HOSTOFF-NET-VLESS-WS-122MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-138MS`
12. `AKUN-012-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-97MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-NETCUP-VLESS-WS-95MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-DIGITALOCEAN-VLESS-WS-123MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-NET-NL-VLESS-WS-103MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-255MS` (url=516ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-261MS` (url=565ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-273MS` (url=577ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-267MS` (url=575ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-272MS` (url=585ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-240MS` (url=537ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=220ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-319MS` (url=510ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-392MS` (url=683ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
