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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=210ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=220ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=239ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-69MS` (url=215ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=215ms, nekobox=238ms, status=yes)
6. `AKUN-006-WEYRO-NET-VLESS-WS-80MS` (url=229ms, nekobox=236ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-81MS` (url=215ms, nekobox=259ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-80MS` (url=199ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS` (url=219ms, nekobox=234ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-99MS` (url=228ms, nekobox=238ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-66MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-116MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-111MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-PAGES-VLESS-WS-122MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-131MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-117MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-118MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-INTERNETWORKS-45-131-6-0-VLESS-WS-141MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-239MS` (url=498ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-231MS` (url=501ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-244MS` (url=586ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-252MS` (url=543ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-243MS` (url=547ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-265MS` (url=556ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-278MS` (url=546ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
