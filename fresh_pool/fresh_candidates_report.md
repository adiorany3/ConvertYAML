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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=215ms, nekobox=265ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=213ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=215ms, nekobox=243ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-77MS` (url=235ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=238ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=277ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=226ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS` (url=244ms, nekobox=268ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS` (url=240ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=240ms, nekobox=277ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-73MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-98MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-72MS` (url=248ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-84MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-MEDIUM-VLESS-WS-74MS` (url=324ms, status=HTTP 204)
18. `AKUN-018-MYBB-VLESS-WS-89MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-106MS` (url=286ms, status=HTTP 204)
20. `AKUN-020-1PASSWORD-VLESS-WS-74MS` (url=240ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-188MS` (url=363ms, status=HTTP 204)
22. `AKUN-022-SHOPIFY-VLESS-WS-178MS` (url=342ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-84MS` (url=271ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-336MS` (url=815ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-354MS` (url=790ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
