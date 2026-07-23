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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=222ms, nekobox=264ms, status=yes)
2. `AKUN-002-GOV-VLESS-WS-63MS` (url=215ms, nekobox=249ms, status=yes)
3. `AKUN-003-HETZNER-VLESS-WS-65MS` (url=235ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=252ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=213ms, nekobox=249ms, status=yes)
6. `AKUN-006-HETZNER-VLESS-WS-61MS` (url=222ms, nekobox=257ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-68MS` (url=230ms, nekobox=260ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-78MS` (url=246ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=215ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, nekobox=263ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-94MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-91MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-135MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-HETZNER-VLESS-WS-86MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=253ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-110MS` (url=226ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-105MS` (url=233ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-140MS` (url=271ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-87MS` (url=229ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-87MS` (url=209ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-120MS` (url=230ms, status=HTTP 204)
24. `AKUN-025-ZVC-VLESS-WS-67MS` (url=198ms, status=HTTP 204)
25. `AKUN-026-INTERNETWORKS-45-131-210-VLESS-WS-340MS` (url=2963ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
