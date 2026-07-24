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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=219ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=237ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=224ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-73MS` (url=202ms, nekobox=247ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=228ms, nekobox=259ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=223ms, nekobox=248ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-92MS` (url=219ms, nekobox=247ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-85MS` (url=223ms, nekobox=256ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-74MS` (url=226ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=226ms, nekobox=247ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-87MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-94MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-GOOGLE-VLESS-WS-113MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-97MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=232ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=286ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-120MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-144MS` (url=255ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-74MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-179MS` (url=384ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-155MS` (url=376ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-347MS` (url=796ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
