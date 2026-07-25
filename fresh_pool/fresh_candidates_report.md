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
1. `AKUN-001-AMAZON-VLESS-WS-60MS` (url=227ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=221ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=248ms, nekobox=256ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-64MS` (url=224ms, nekobox=275ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=216ms, nekobox=270ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-75MS` (url=242ms, nekobox=258ms, status=yes)
7. `AKUN-007-GOOGLE-VLESS-WS-78MS` (url=234ms, nekobox=270ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-80MS` (url=222ms, nekobox=293ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-72MS` (url=275ms, nekobox=267ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-89MS` (url=261ms, nekobox=254ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-79MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-102MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-91MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-110MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-102MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-86MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-237MS` (url=549ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-247MS` (url=541ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-261MS` (url=601ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-304MS` (url=582ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-434MS` (url=697ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
