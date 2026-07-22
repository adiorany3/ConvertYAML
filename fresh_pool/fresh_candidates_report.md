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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=209ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=226ms, nekobox=246ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-73MS` (url=224ms, nekobox=184ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-79MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-82MS`
9. `AKUN-008-EE-WELCOMEHOST-20190515-VLESS-WS-84MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-71MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=256ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-83MS` (url=220ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-112MS` (url=224ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-115MS` (url=211ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=222ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-148MS` (url=288ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-227MS` (url=498ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-228MS` (url=4804ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-258MS` (url=510ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-328MS` (url=620ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-297MS` (url=908ms, status=HTTP 204)
23. `AKUN-025-ZVC-VLESS-WS-66MS` (url=224ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-480MS` (url=1004ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-496MS` (url=1200ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
