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
1. `AKUN-001-WPENG-VLESS-WS-61MS` (url=217ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=226ms, nekobox=265ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-61MS` (url=218ms, nekobox=234ms, status=yes)
5. `AKUN-005-WEYRO-NET-VLESS-WS-69MS` (url=226ms, nekobox=266ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-62MS` (url=209ms, nekobox=244ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=209ms, nekobox=259ms, status=yes)
8. `AKUN-008-SSL-1134-VLESS-WS-77MS` (url=228ms, nekobox=253ms, status=yes)
9. `AKUN-009-OVH-VLESS-WS-70MS` (url=224ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS` (url=208ms, nekobox=234ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-66MS` (url=225ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-67MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-152MS` (url=225ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-343MS` (url=744ms, status=HTTP 204)
16. `AKUN-018-SPEEDTEST-VLESS-WS-347MS` (url=769ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-369MS` (url=818ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-389MS` (url=853ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-372MS` (url=883ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-393MS` (url=871ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-348MS` (url=734ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-666MS` (url=1089ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-697MS` (url=1119ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-678MS` (url=1077ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-700MS` (url=1163ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
