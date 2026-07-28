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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=229ms, nekobox=216ms, status=no)
2. `AKUN-001-008500-VLESS-WS-80MS`
3. `AKUN-002-ZVC-VLESS-WS-74MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-75MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=226ms, nekobox=180ms, status=no)
7. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS` (url=224ms, nekobox=185ms, status=no)
8. `AKUN-005-UNKNOWN-VLESS-WS-112MS`
9. `AKUN-006-UNKNOWN-VLESS-WS-96MS`
10. `AKUN-007-UNKNOWN-VLESS-WS-86MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-99MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-94MS` (url=222ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-160MS` (url=273ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=328ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-159MS` (url=387ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-170MS` (url=269ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-230MS` (url=504ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-257MS` (url=2404ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-299MS` (url=550ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-293MS` (url=558ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-255MS` (url=283ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-448MS` (url=2022ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-436MS` (url=1056ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
