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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=223ms, nekobox=225ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=203ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, nekobox=263ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-68MS` (url=213ms, nekobox=248ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-77MS` (url=223ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, nekobox=246ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-65MS` (url=222ms, nekobox=226ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS` (url=221ms, nekobox=248ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-100MS` (url=213ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=221ms, nekobox=249ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-61MS` (url=329ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-132MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-133MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-108MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-138MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-ZOOM-VLESS-WS-87MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-97MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-90MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-111MS` (url=256ms, status=HTTP 204)
22. `AKUN-022-COMPREND-NET-VLESS-WS-94MS` (url=214ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-231MS` (url=491ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-227MS` (url=512ms, status=HTTP 204)
25. `AKUN-025-CELESTARA-VLESS-WS-251MS` (url=549ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
