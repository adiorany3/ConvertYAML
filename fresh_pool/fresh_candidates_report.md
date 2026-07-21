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
1. `AKUN-001-ALIBABA-VLESS-WS-61MS` (url=218ms, nekobox=253ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS` (url=216ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=214ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=220ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=221ms, nekobox=244ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=231ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=218ms, nekobox=243ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS` (url=233ms, nekobox=240ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-82MS` (url=196ms, nekobox=273ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS` (url=260ms, nekobox=238ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-111MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-79MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-98MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-110MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-86MS` (url=201ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-122MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-136MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-85MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-99MS` (url=218ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-99MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-115MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-94MS` (url=207ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-343MS` (url=4321ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-347MS` (url=792ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-364MS` (url=762ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
