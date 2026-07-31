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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=309ms, nekobox=197ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-86MS`
3. `AKUN-002-DEV-VLESS-WS-90MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-111MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS`
7. `AKUN-006-DEV-VLESS-WS-82MS`
8. `AKUN-007-008500-VLESS-WS-81MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-117MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=358ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-186MS` (url=356ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-101MS` (url=291ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-180MS` (url=449ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-118MS` (url=313ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-81MS` (url=337ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-86MS` (url=346ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-90MS` (url=318ms, status=HTTP 204)
21. `AKUN-021-NET-141-11-202-0-23-VLESS-WS-329MS` (url=682ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-88MS` (url=516ms, status=HTTP 204)
23. `AKUN-024-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-559MS` (url=1326ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-576MS` (url=981ms, status=HTTP 204)
25. `AKUN-026-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-570MS` (url=1186ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
