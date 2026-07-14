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
1. `AKUN-001-GO-DADDY-COM-LLC-VLESS-WS-60MS` (url=218ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS`
4. `AKUN-004-HOSTWINDS-17-7-VLESS-WS-67MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=225ms, nekobox=7177ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-79MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-69MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-83MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
12. `AKUN-013-466688-VLESS-WS-80MS` (url=228ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-82MS` (url=221ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-90MS` (url=262ms, status=HTTP 204)
16. `AKUN-017-HETZNER-VLESS-WS-103MS` (url=214ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=224ms, status=HTTP 204)
18. `AKUN-019-PUBLICDOMAINREGISTRY-NET-VLESS-WS-99MS` (url=236ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-127MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-88MS` (url=228ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-73MS` (url=266ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-79MS` (url=229ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-196MS` (url=317ms, status=HTTP 204)
25. `AKUN-026-POLICE-VLESS-WS-110MS` (url=259ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
