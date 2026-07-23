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
1. `AKUN-001-UNKNOWN-VLESS-WS-68MS` (url=227ms, nekobox=262ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS` (url=265ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=243ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=236ms, nekobox=265ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-75MS` (url=231ms, nekobox=332ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=403ms, nekobox=286ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=266ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=273ms, nekobox=255ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-80MS` (url=346ms, nekobox=268ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-99MS` (url=223ms, nekobox=261ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=261ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=256ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-98MS` (url=362ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-80MS` (url=266ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=237ms, status=HTTP 204)
17. `AKUN-017-LEVIKOGJGFDD-VLESS-WS-94MS` (url=282ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-105MS` (url=257ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-75MS` (url=295ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-128MS` (url=403ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-81MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-137MS` (url=346ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-99MS` (url=296ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-143MS` (url=443ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-163MS` (url=362ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
