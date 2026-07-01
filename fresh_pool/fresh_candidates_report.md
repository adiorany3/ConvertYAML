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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=211ms, nekobox=237ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-68MS` (url=210ms, nekobox=235ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-76MS` (url=222ms, nekobox=228ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=221ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=206ms, nekobox=248ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-85MS` (url=217ms, nekobox=238ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-96MS` (url=214ms, nekobox=254ms, status=yes)
8. `AKUN-008-NETCUP-VLESS-WS-73MS` (url=211ms, nekobox=240ms, status=yes)
9. `AKUN-009-U1HOST-FRA-VLESS-WS-97MS` (url=220ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=213ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-102MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-108MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-84MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-114MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-98MS` (url=211ms, status=HTTP 204)
17. `AKUN-017-SPACECORE-VLESS-WS-88MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-84MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=208ms, status=HTTP 204)
20. `AKUN-020-NET-NL-VLESS-WS-82MS` (url=200ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-233MS` (url=496ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-245MS` (url=570ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-250MS` (url=496ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-255MS` (url=544ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-244MS` (url=546ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
