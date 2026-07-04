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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=224ms, nekobox=263ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-82MS` (url=216ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, nekobox=259ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-85MS` (url=210ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=235ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=248ms, nekobox=257ms, status=yes)
8. `AKUN-008-DIGITALOCEAN-VLESS-WS-107MS` (url=249ms, nekobox=241ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS` (url=236ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=226ms, nekobox=255ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-96MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-89MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-96MS` (url=242ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-123MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-149MS` (url=200ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-240MS` (url=511ms, status=HTTP 204)
18. `AKUN-020-466688-VLESS-WS-230MS` (url=373ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-262MS` (url=504ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-250MS` (url=518ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-271MS` (url=557ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-288MS` (url=756ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-285MS` (url=600ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-285MS` (url=560ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-284MS` (url=1542ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
