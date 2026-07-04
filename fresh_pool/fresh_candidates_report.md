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
1. `AKUN-001-ORACLE-VLESS-WS-62MS` (url=198ms, nekobox=229ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-64MS` (url=223ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=215ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=204ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=235ms, nekobox=269ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-62MS` (url=217ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS` (url=208ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=216ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=204ms, nekobox=229ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, nekobox=245ms, status=yes)
11. `AKUN-011-WEYRO-NET-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-79MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-84MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-OVH-VLESS-WS-108MS` (url=309ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=271ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-109MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=205ms, status=HTTP 204)
19. `AKUN-020-INTERNETWORKS-45-131-208-VLESS-WS-238MS` (url=526ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-228MS` (url=487ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-236MS` (url=544ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-239MS` (url=504ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-258MS` (url=535ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-268MS` (url=549ms, status=HTTP 204)
25. `AKUN-026-466688-VLESS-WS-228MS` (url=402ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
