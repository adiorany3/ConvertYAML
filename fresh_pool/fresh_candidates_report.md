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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=208ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=211ms, nekobox=190ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-80MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=203ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-99MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-81MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-97MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-116MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-73MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-135MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-78MS` (url=220ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-137MS` (url=246ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-134MS` (url=361ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-93MS` (url=236ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-116MS` (url=230ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
