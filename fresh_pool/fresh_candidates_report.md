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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=232ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=232ms, nekobox=255ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-85MS` (url=227ms, nekobox=245ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-91MS` (url=232ms, nekobox=241ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=209ms, nekobox=254ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=229ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=221ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=230ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=218ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-113MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-110MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-102MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-95MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-122MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-119MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-104MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-93MS` (url=235ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-120MS` (url=221ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-272MS` (url=561ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-273MS` (url=589ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-253MS` (url=529ms, status=HTTP 204)
23. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-283MS` (url=562ms, status=HTTP 204)
24. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-223MS` (url=495ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-276MS` (url=547ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
